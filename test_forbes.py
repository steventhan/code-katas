import pytest


@pytest.fixture(scope='session')
def real_data():
    """Get data from json"""
    from forbes_40 import get_data
    return get_data('./forbes_billionaires_2016.json')

@pytest.fixture(scope='function')
def sample_data():
    """Create sample data"""
    return [
        {'age': 22},
        {'age': 40},
        {'age': 30},
        {'age': 19},
        {'age': 50},
        {'age': 55},
        {'age': 79},
    ]


@pytest.fixture(scope='function')
def fake_result():
    """Create fake result"""
    return ({
        'age': 23,
        'name': 'me',
        'net_worth (USD)': -10000
    },
    {
        'age': 32,
        'name': 'also me',
        'net_worth (USD)': -20000
    })


def test_read_file():
    from forbes_40 import get_data
    data = get_data('./forbes_billionaires_2016.json')
    assert len(data) == 40


def test_get_youngest_oldest(sample_data):
    from forbes_40 import get_youngest_oldest
    youngest, oldest = get_youngest_oldest(sample_data)
    assert youngest['age'] == 19
    assert oldest['age'] == 79



def test_get_youngest_oldest_ignore_invalid_age(sample_data):
    from forbes_40 import get_youngest_oldest
    youngest, oldest = get_youngest_oldest(sample_data)
    sample_data[0]['age'] = 0
    assert youngest['age'] == 19


def test_get_youngest_oldest_ignore_age_greater_than_79(sample_data):
    from forbes_40 import get_youngest_oldest
    youngest, oldest = get_youngest_oldest(sample_data)
    sample_data[0]['age'] = 80
    assert oldest['age'] == 79


def test_format_output(fake_result):
    from forbes_40 import format_output
    output = format_output(fake_result)
    assert 'Youngest billionaire is:' in output
