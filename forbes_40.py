#!/usr/bin/env python
import json


def get_data(file_path):
    """Read json file."""
    with open(file_path) as data:
        return json.load(data)


def get_youngest_oldest(billionaires):
    """Get youngest and oldest billionaires."""
    youngest = {'age': 80}
    oldest = {'age': 0}
    for person in billionaires:
        if person['age'] > oldest['age'] and person['age'] < 80:
            oldest = person
        elif person['age'] < youngest['age'] and person['age'] > 0:
            youngest = person
    return youngest, oldest

def format_output(data):
    output = 'Oldest billionaire under 80 is:\n'
    output += 'Name: {}\nAge: {}\nNet worth: {}\n'.format(
            data[1]['name'],
            data[1]['age'],
            data[1]['net_worth (USD)']
    )
    output += 'Youngest billionaire is:\n'
    output += 'Name: {}\nAge: {}\nNet worth: {}\n'.format(
            data[0]['name'],
            data[0]['age'],
            data[0]['net_worth (USD)']
    )
    return output


if __name__ == '__main__':
    print(format_output(get_youngest_oldest(get_data('./forbes_billionaires_2016.json'))))
