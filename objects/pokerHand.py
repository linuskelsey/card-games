from card import Card
from deck import Deck

class PokerHand:
    """ Class for a 5-Card Poker hand """

    def __init__(self, feed):
        self.hand = Deck(deck=[], full=False)
        self.feed = feed
        self.feed.deal(deck=self.hand, n=5)
        self.rankNumsOrdered = []
        self.rankCounts = {}
        for card in self.hand.cards:
            self.rankNumsOrdered.append(card.rankNums[card.rank])
            if card.rank in self.rankCounts.keys():
                self.rankCounts[card.rank] += 1
            else:
                self.rankCounts[card.rank] = 1
        self.rankNumsOrdered.sort()

    def update(self):
        self.rankNumsOrdered = []
        self.rankCounts = {}
        for card in self.hand.cards:
            self.rankNumsOrdered.append(card.rankNums[card.rank])
            if card.rank in self.rankCounts.keys():
                self.rankCounts[card.rank] += 1
            else:
                self.rankCounts[card.rank] = 1
        self.rankNumsOrdered.sort()

    def replaceCard(self, idx):
        card = self.feed.deal()
        self.hand.cards[idx] = card
        self.update()
        return

    def isRoyalFlush(self):
        if self.isStraightFlush() and 14 in self.rankNumsOrdered:
            return True
        else:
            return False
    
    def isStraightFlush(self):
        if self.isStraight() and self.isFlush():
            return True
        else:
            return False
    
    def isFourKind(self):
        if len(self.rankCounts.keys()) > 2:
            return False
        
        if 4 in list(self.rankCounts.values()):
            return True
        else:
            return False
    
    def isFullHouse(self):
        if len(self.rankCounts.keys()) > 2:
            return False
        
        if 3 in list(self.rankCounts.values()):
            return True
        else:
            return False
    
    def isFlush(self):
        suits = set([card.suit for card in self.hand.cards])
        if len(suits) == 1:
            return True
        else:
            return False
    
    def isStraight(self):
        for i in range(4):
            if self.rankNumsOrdered[i+1] != self.rankNumsOrdered[i] + 1:
                return False
        
        return True
    
    def isThreeKind(self):
        if not self.isFullHouse() and 3 in list(self.rankCounts.values()):
            return True
        else:
            return False
    
    def isTwoPair(self):
        if list(self.rankCounts.values()).count(2) == 2:
            return True
        else:
            return False
    
    def isJacksBetter(self):
        for k, v in self.rankCounts.items():
            if v == 2:
                if k == 'J' or k == 'Q' or k == 'K' or k == 'A':
                    return True
        
        return False
    
    def bestHand(self):
        if self.isRoyalFlush():
            return 'a Royal Flush!', 1000
        elif self.isStraightFlush():
            return 'a Straight Flush!', 300
        elif self.isFourKind():
            return 'Four of a Kind!', 120
        elif self.isFullHouse():
            return 'a Full House!', 60
        elif self.isFlush():
            return 'a Flush!', 40
        elif self.isStraight():
            return 'a Straight!', 25
        elif self.isThreeKind():
            return 'Three of a Kind!', 15
        elif self.isTwoPair():
            return 'Two Pair!', 8
        elif self.isJacksBetter():
            return 'a pair of Jacks or Better!', 2
        else:
            return 'nothing...', 0