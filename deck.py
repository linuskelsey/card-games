from card import Card

import random

class Deck:
	"""Default suits and ranking order."""
	suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
	ranks = [None, None] + [str(i) for i in range(2,11)] + ['Jack', 'Queen', 'King', 'Ace']

	def __init__(self, cards=[]):
		self.cards = cards
		self.size = len(cards)

	def verify(self):
		"""To verify if a deck is legal. Not too sure if this is actually a useful method."""

		answer = True
		for card in self.cards:
			if type(card) == Card and card.verify():
				continue
			else:
				answer = False
				break
		return answer

	def remove_rank(self, rank):
		"""For removing certain ranks for certain games, e.g. if a game doesn't use 2's through 8's. Both removes the rank from the deck's list of ranks as well as removing it from each card's list of valid ranks."""

		self.ranks[rank] = None
		for card in self.cards:
			card.ranks[rank] = None

	def generate(self):
		"""To generate the deck from the suits and ranks we have available to us. I.e. if you create an empty deck, then restrict the ranks, you can automatically create your deck using this method."""

		for suit in range(len(self.suits)):
			for rank in range(len(self.ranks)):
				if self.ranks[rank]:
					self.cards.append(Card(rank, suit))
		self.size=len(self.cards)

	def shuffle(self):
		"""Shuffles the cards in the deck."""
		new=[]

		while self.cards:
			choice=random.choice(self.cards)
			new.append(choice)
			self.cards.remove(choice)

		self.cards = new