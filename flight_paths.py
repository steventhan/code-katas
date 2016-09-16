#!/usr/bin/env python

from __future__ import unicode_literals, print_function
import json
import sys
import networkx as nx


def calculate_distance(point1, point2):
    """
    Calculate the distance (in miles) between point1 and point2.
    point1 and point2 must have the format [latitude, longitude].
    The return value is a float.

    Modified and converted to Python from: http://www.movable-type.co.uk/scripts/latlong.html
    """
    import math

    def convert_to_radians(degrees):
        return degrees * math.pi / 180

    radius_earth = 6.371E3 # km
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])

    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])

    a = math.sin(0.5 * delta_phi)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(0.5 * delta_lam)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c / 1.60934  # convert km to miles


def get_data(file_path):
    with open(file_path) as data:
        return json.load(data)


def get_airports(data):
    airports = {}
    for i in data:
        airports[i['airport']] = i['lat_lon']
    return airports


def get_airports1(data):
    return {i['airport']: i['lat_lon'] for i in data}


def _get_small_sample():
    with open('./sample_data.json', 'w') as outfile:
        sample_data = []
        for i in range(10):
            sample_data.append(DATA[i])
        json.dump(sample_data, outfile)


def city_lookup(city, data):
    for c in data:
        if c['city'] == city:
            yield c


def city_lookup1(city, data): 
    return (i for i in data if i['city'] == city)


def get_city_airports(city, data):
    return (i['airport'] for i in data if i['city'] == city)


def build_airport_graph(data):
    airport_g = nx.DiGraph()
    for i in data:
        airport = i['airport']
        for a in i['destination_airports']:
            if AIRPORTS.get(airport, None) and AIRPORTS.get(a, None):
                airport_g.add_edge(
                    airport,
                    a,
                    distance=calculate_distance(
                        AIRPORTS[airport],
                        AIRPORTS[a]
                    )
                )
    return airport_g


def main(start=None, end=None):
    try:
        start, end = start.title(), end.title()
    except AttributeError as e:
        e.args = ('Enter city name(s) as string',)
        raise
    airport_g = build_airport_graph(DATA)
    for start_airport in get_city_airports(start, DATA):
        for end_airport in get_city_airports(end, DATA):
            yield (nx.shortest_path(
                      airport_g,
                      start_airport,
                      end_airport,
                      weight='distance'
                   ),
                   nx.shortest_path_length(
                       airport_g,
                       start_airport,
                       end_airport,
                       weight='distance'
                    ))


def format_output(result_generator):
    output = ''
    sorted_path_list = sorted(
            list(result_generator),
            key=lambda x: x[1]
            )
    output += 'Path with shortest distance:\n'
    try:
        output += 'Path: {}. Distance: {} km\n'.format(
            ' -> '.join(sorted_path_list[0][0]),
            sorted_path_list[0][1]
            )
    except IndexError:
        output += 'No path found'
    if len(sorted_path_list) > 1:
        output += '\nOther alternatives:\n'
        for path in sorted_path_list[1:]:
            output += 'Path: {}. Distance: {} km\n'.format(
                ' -> '.join(path[0]),
                path[1]
            )
    return output
 

DATA = get_data('./cities_with_airports.json')
AIRPORTS = get_airports(DATA)


if __name__ == '__main__':
    print(format_output(main(sys.argv[1], sys.argv[2])))
