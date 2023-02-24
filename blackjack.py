from card import Card
from deck import Deck
from player import Player
from table import Table

def main(name):

	# INITIALISE DECK, PLAYERS AND TABLE.
	deck=Deck()
	deck.generate()
	players=[Player(name, [], False), Player("Dealer", [], True)]
	table=Table(deck,players)

	run=True

	while run:

		print("Let's play Blackjack!")
		table.deal()



# names=[]
# answer='y'
# name1=input("What is your name? ").title()
# names.append(name1)
# while answer.lower() not in ['n', 'no']:
# 	answer=input("Would anyone else like to play? ")
# 	if answer.lower() in ['y', 'yes']:
# 		namex=input("What is your name? ").title()
# 		names.append(namex)

# main(names)