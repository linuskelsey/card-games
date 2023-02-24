class Card:
	"""Default suits and ranking order."""
	suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
	ranks = [None, None] + [str(i) for i in range(2,11)] + ['Jack', 'Queen', 'King', 'Ace']

	def __init__(self, rank, suit):
		"""Rank and suit are integers, to allow easy ordering properties."""
		self.rank = rank
		self.suit = suit

	def verify(self):
		"""This method verifies a card is valid. Will be used before any other method is called."""

		answer = True
		try:
			rank = self.ranks[self.rank]
			suit = self.suits[self.suit]
			pass
		except IndexError:
			answer = False
		return answer

	def show(self):
		"""This method shows a card to the user."""

		if self.verify():
			rank = self.ranks[self.rank]
			suit = self.suits[self.suit]
			print(f'{rank} of {suit}')
		else:
			print('The card you wish to show does not exist!')

	def lower_than(self, c2):
		"""Compare ranks of two cards."""

		answer=True
		if self.verify() and c2.verify():
			if self.rank < c2.rank:
				pass
			else:
				answer=False
		else:
			raise ValueError('You are not comparing legal cards.')
		return answer

	def greater_than(self, c2):
		"""Compare ranks of two cards. (pt2)"""

		answer=True
		if self.verify() and c2.verify():
			if self.rank > c2.rank:
				pass
			else:
				answer=False
		else:
			raise ValueError('You are not comparing legal cards.')
		return answer

	def equal_to(self, c2):
		"""Compare ranks of two cards. (pt3)"""

		answer=True
		if self.verify() and c2.verify():
			if self.rank == c2.rank:
				pass
			else:
				answer=False
		else:
			raise ValueError('You are not comparing legal cards.')
		return answer