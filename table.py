from card import Card
from deck import Deck
from player import Player

class Table:

	def __init__(self, deck, players):
		self.deck = deck
		self.players = players

	def drawCard(self, card):
		"""Method to draw a card, as in poker or the like."""
		drawn = card
		index = self.deck.cards.index(card)
		self.deck.cards.remove(self.deck.cards[index])
		return drawn

	def setOrder(self):
		"""To set the 'deal' order."""
		for player in self.players:
			if not player.dealerCheck:
				pass
			else:
				ind = self.players.index(player)
				self.players = self.players[ind+1:] + self.players[:ind+1]

	def rotateDealer(self):
		"""To rotate the position of the dealer."""
		for player in self.players:
			if not self.dealerCheck:
				pass
			else:
				player.dealerCheck = False
				ind = self.players.index(player)
				self.players[ind+1].dealerCheck = True

	def deal(self, shuffle=True):
		"""Method to deal cards to each of the players at the table."""

		# First set the deal order.
		self.setOrder()

		# Determine whether deck needs shuffling before dealing. Default is True.
		if shuffle:
			self.deck.shuffle()

		# Loop through players each deal round.	
		for player in self.players:
			card = self.deck.cards.pop()
			player.hand.append(card)

		# Rotate the dealer.
		self.rotateDealer()