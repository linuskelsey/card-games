class Card:

    """ Class for a card in various games, 52-card standard deck """

    suits = {
        'C': 'Clubs',
        'S': 'Spades',
        'D': 'Diamonds',
        'H': 'Hearts',
    }
    ranks = {
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine',
        '10': 'Ten',
        'J': 'Jack',
        'Q': 'Queen',
        'K': 'King',
        'A': 'Ace',
    }
    rankNums = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14,
    }
    blackjackNums = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 11,
    }

    def __init__(self, rank, suit):
        self.rank = str(rank)
        self.suit = suit
        self.rank_num = self.rankNums[self.rank]
        self.blkjck = self.blackjackNums[self.rank]

    def __str__(self):
        return f'{self.ranks[self.rank]} of {self.suits[self.suit]}'
    

    def draw(self):
        first = '\t+- - -+\n'
        second = f'\t|{self.rank}    |\n'
        if len(self.rank) == 2:
            second = f'\t|{self.rank}   |\n'
        third = f'\t|{self.suit}   {self.suit}|\n'
        fourth = f'\t|    {self.rank}|\n'

        return '\n' + first + second + third + fourth + first

    def short(self):
        return f'{self.rank}{self.suit}'