from deck import Deck

class BlackjackPlayer:

    """ A class to model a blackjack player, with methods to see current scores, stick, twist and (maybe) split. """

    def __init__(self, feed_deck):
        self.feed = feed_deck
        self.deck = Deck(deck=[], full=False)
        self.feed.deal(self.deck, 2)

    def score_declare(self, dealer=False):
        scores = [0]
        for card in self.deck.cards:
            if card.rank != 'A':
                for i in range(len(scores)):
                    scores[i] += card.blkjck
            else:
                for i in range(len(scores)):
                    scores[i] = [scores[i] + 1, scores[i] + 11]
                    
                scores = [val for sub in scores for val in sub]
                scores = list(set(scores))
                    
        score_string = ''
        if len(scores) >= 2:
            for score in scores[:len(scores)-2]:
                score_string += str(score) + ', '
            score_string += str(scores[-2]) + ' and ' + str(scores[-1])
            if dealer:
                return "Dealer's scores are " + score_string + '.', scores
            return 'Your scores are ' + score_string + '.', scores
        else:
            score_string = str(scores[0])
            if dealer:
                return "Dealer's score is " + score_string + '.', scores
            return 'Your score is ' + score_string + '.', scores
            
    def hit(self):
        return self.feed.deal(self.deck)