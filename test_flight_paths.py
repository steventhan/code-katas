import pytest


@pytest.fixture(scope='session')
def sample_data():
    from flight_paths import get_data
    return get_data('./sample_data.json')


@pytest.fixture(scope='session')
def real_data():
    from flight_paths import get_data
    return get_data('./cities_with_airports.json')


def test_read_file():
    from flight_paths import get_data
    data = get_data('./sample_data.json')
    assert len(data) == 10
    assert data[0]['city'] == 'Goma'


def test_get_airports(sample_data):
    from flight_paths import get_airports
    airports = get_airports(sample_data)
    assert len(airports) == 10
    assert 'Pointe Noire Airport' in airports


def test_get_city_airports(sample_data):
    from flight_paths import get_city_airports
    airports = get_city_airports('Goma', sample_data)
    assert next(airports) == "Goma International Airport"


def test_build_airport_graph(sample_data):
    from flight_paths import build_airport_graph
    g = build_airport_graph(sample_data)
    assert 'Port-Gentil International Airport' in g.nodes()


def test_main_raise_error_if_wrong_type_input():
    from flight_paths import main
    with pytest.raises(AttributeError):
        next(main(3, 4))


def test_main(real_data):
    from flight_paths import main
    gen = main('san francisco', 'los angeles', real_data)
    assert 'San Francisco International Airport' in next(gen)[0]


def test_format_output_single(real_data):
    from flight_paths import main, format_output
    gen = main('san francisco', 'los angeles', real_data)
    assert 'Path with shortest distance' in format_output(gen)


def test_format_output_multiple(real_data):
    from flight_paths import main, format_output
    gen = main('san francisco', 'london', real_data)
    assert 'Other alternatives' in format_output(gen)


def test_format_output_no_path_found(sample_data):
    from flight_paths import main, format_output
    gen = main('san francisco', 'los angeles', sample_data)
    assert 'No path found' in format_output(gen)
