from card import Card
from deck import Deck

class Player:

	def __init__(self, name, hand, dealerCheck, stack=0):
		self.name = name
		self.hand = hand
		self.dealerCheck = dealerCheck
		self.stack = stack

	def reveal(self):
		"""Reveals all cards in the hand - useful for poker, after the river."""
		if self.hand:
			for card in self.hand:
				card.show()
		else:
			print("You have no cards to show...")

	def drawCard(self, card):
		"""Draws a card from the player's hand. Note that the argument must be given as self.hand[i] for some i, as the Card types are not identifiable in the correct way. Not sure how to fix this."""
		if card in self.hand:
			drawn = card
			index = self.hand.index(card)
			self.hand.remove(self.hand[index])
		else:
			raise NameError('Card is not in hand.')
		return drawn