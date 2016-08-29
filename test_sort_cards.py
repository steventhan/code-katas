import pytest

DECKS = [
    ('32456', '23456'),
    ('JKTQ', 'TJQK'),
    ('39A5T824Q7J6K', 'A23456789TJQK'),
    ('Q286JK395A47T', 'A23456789TJQK'),
    ('54TQKJ69327A8', 'A23456789TJQK')
]


@pytest.mark.parametrize('deck, sorted_deck', DECKS)
def test_sort_cards(deck, sorted_deck):
    from sort_cards import sort_cards
    assert list(sort_cards(deck)) == list(sorted_deck)
