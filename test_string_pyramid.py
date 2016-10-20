#!/usr/bin/env python
# -*- coding: utf -8 -*-
import pytest


def test_get_side_lines_empty_string():
    from string_pyramid import get_side_lines
    with pytest.raises(ValueError) as e:
        get_side_lines('')
    assert 'Pyramid can only be built with non-empty string.' in str(e)


def test_get_side_lines_good_string():
    from string_pyramid import get_side_lines
    lines = get_side_lines('abc')
    assert len(lines) == 3
    assert lines == ['c', 'bbb', 'aaaaa']


def test_watch_pyramid_from_the_side_empty_string():
    from string_pyramid import watch_pyramid_from_the_side
    assert watch_pyramid_from_the_side('') == ''


def test_watch_pyramid_from_the_side_good_string():
    from string_pyramid import watch_pyramid_from_the_side
    assert watch_pyramid_from_the_side('abc') == '  c  \n bbb \naaaaa'


def test_watch_pyramid_from_above_empty_string():
    from string_pyramid import watch_pyramid_from_above
    assert watch_pyramid_from_above('') == ''


def test_watch_pyramid_from_above_good_string():
    from string_pyramid import watch_pyramid_from_above
    assert watch_pyramid_from_above('abc') == '''\
aaaaa
abbba
abcba
abbba
aaaaa'''


def test_count_visible_characters_of_the_pyramid_empty_string():
    from string_pyramid import count_visible_characters_of_the_pyramid
    assert count_visible_characters_of_the_pyramid('') == -1


def test_count_visible_characters_of_the_pyramid_good_string():
    from string_pyramid import count_visible_characters_of_the_pyramid
    assert count_visible_characters_of_the_pyramid('abcd') == 49


def test_count_all_characters_of_the_pyramid_empty_string():
    from string_pyramid import count_all_characters_of_the_pyramid
    assert count_all_characters_of_the_pyramid('') == -1


def test_count_all_characters_of_the_pyramid_good_string():
    from string_pyramid import count_all_characters_of_the_pyramid
    assert count_all_characters_of_the_pyramid('abcd') == 84
