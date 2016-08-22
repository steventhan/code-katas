import pytest

PARENTHESES_TABLE = [
    ('(this is a properly closed (string))', 0),
    ('string(str)string(str)str))', -1),
    ('(str((str', 1),
    ('()', 0),
    ('(', 1),
    (')', -1)
]


@pytest.mark.parametrize('string, result', PARENTHESES_TABLE)
def test_check_parentheses(string, result):
    """Test check_parentheses func with multiple params"""
    from check_parentheses import check_parentheses
    assert check_parentheses(string) == result
