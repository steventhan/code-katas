#!/usr/bin/env python
# -*- coding: utf -8 -*-
from __future__ import print_function


def get_side_lines(characters):
    """Get pyramid side lines."""
    if len(characters) < 1:
        raise ValueError('Pyramid can only be built with non-empty string.')
    lines = []
    num_characters = 1
    while len(characters) >= 1:
        lines.append(characters[-1] * num_characters)
        num_characters += 2
        characters = characters[:-1]
    return lines


def watch_pyramid_from_the_side(characters):
    """Get view from the side."""
    if not characters:
        return characters
    lines = get_side_lines(characters)
    line_width = len(lines[-1])
    output = ''
    for line in lines:
        if len(line) == line_width:
            output += line
        else:
            spaces = ' ' * int((line_width - len(line)) / 2)
            output += '{}{}{}\n'.format(spaces, line, spaces)
    return output


def watch_pyramid_from_above(characters):
    """Get view from above."""
    if not characters:
        return characters
    lines = get_side_lines(characters)
    line_width = len(lines[-1])
    lst = []
    for line in reversed(lines):
        if len(line) == line_width:
            lst.append(line)
        else:
            prev = lst[-1]
            cutoff = int((line_width - len(line)) / 2)
            left = prev[:cutoff]
            right = prev[-cutoff:]
            lst.append('{}{}{}'.format(left, line, right))
    output = ''
    for i in lst[:-1]:
        output += i + '\n'
    for idx, i in enumerate(reversed(lst)):
        if idx == len(lst) - 1:
            output += i
        else:
            output += i + '\n'
    return output


def count_visible_characters_of_the_pyramid(characters):
    """Returns number of visible chars."""
    if not characters:
        return -1
    lines = get_side_lines(characters)
    return len(lines[-1]) ** 2


def count_all_characters_of_the_pyramid(characters):
    """Returns number of all chars."""
    if not characters:
        return -1
    lines = get_side_lines(characters)
    total = 0
    for line in lines:
        total += len(line) ** 2
    return total
