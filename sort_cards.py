def sort_cards(cards):
    """Sort a deck of card"""
    def _get_rank(card):
        if card not in 'A23456789TJQK':
            raise TypeError('{} is not a card in deck'.format(card))
        if card == 'A':
            return 1
        elif card == 'T':
            return 10
        elif card == 'J':
            return 11
        elif card == 'Q':
            return 12
        elif card == 'K':
            return 13
        else:
            return int(card)
    return sorted(cards, key=lambda c: _get_rank(c))
