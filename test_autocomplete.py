from autocomplete import AutoCompleter


def test_no_completion():
    c = AutoCompleter(['co', 'cu', 'ca'])
    assert len(c('b')) == 0


def test_simple_case():
    c = AutoCompleter(['co', 'cu', 'ca'])
    assert len(c('c')) == 3
    assert ('cu' and 'co' and 'ca') in c('c')


def test_advanced_case():
    c = AutoCompleter(['co', 'cow', 'com', 'company', 'camera', 'python', 'py'])
    assert len(c('c')) == 5
    assert len(c('co')) == 4
