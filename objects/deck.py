import random

from card import Card

class Deck:

    """ Class for deck of 52 cards for standard games """

    suits = ['C', 'S', 'D', 'H']
    ranks = list(range(2,11)) + ['J', 'Q', 'K', 'A']

    def __init__(self, deck=[], full=True):
        self.cards = []

        if full:
            for suit in self.suits:
                for rank in self.ranks:
                    self.cards.append(Card(rank, suit))
        if not full:
            self.cards = deck


    def deal(self, deck=None, n=1):
        for i in range(n):
            card = self.cards.pop(0)
            if deck is not None:
                deck.add_to_bottom(card)
        if n == 1:
            return card

    def shuffle(self):
        new = []
        while self.cards:
            card = self.cards.pop(random.choice(range(len(self.cards))))
            new.append(card)
        
        self.cards = new
        return
    
    def add_to_bottom(self, card):
        self.cards.append(card)

    def display_deck(self):
        first = '\t'
        second = '\t'
        third = '\t'
        fourth = '\t'

        for card in self.cards:
            first += '+- -'
            second += f'|{card.rank} '
            if len(card.rank) == 1:
                second += ' '
            third += f'|{card.suit}  '
            fourth += '|   '

        final = self.cards[-1]
        first += ' -+\n'
        second += '  |\n'
        third += f' {final.suit}|\n'
        if len(final.rank) == 1:
            fourth += ' '
        fourth += f'{final.rank}|\n'

        return '\n' + first + second + third + fourth + first

    def display_last_n(self, n):
        first = '\t'
        second = '\t'
        third = '\t'
        fourth = '\t'

        if len(self.cards) > n:
            i = len(self.cards) - n
            while i < len(self.cards):
                card = self.cards[i]

                first += '+- -'
                second += f'|{card.rank} '
                if len(card.rank) == 1:
                    second += ' '
                third += f'|{card.suit}  '
                fourth += '|   '

                i += 1

            first += ' -+\n'
            second += '  |\n'
            third += f' {card.suit}|\n'
            if len(card.rank) == 1:
                fourth += ' '
            fourth += f'{card.rank}|\n'

            out = '\n' + first + second + third + fourth + first

        else:
            out = self.display_deck()

        return out