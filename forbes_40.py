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


if __name__ == '__main__':
    print(get_youngest_oldest(get_data('./forbes_billionaires_2016.json')))
