import pickle
import sys

sys.path.insert(1, '/Users/linuskelsey/Desktop/Coding/Python/projects/card_games/objects')

from deck import Deck
from pokerHand import PokerHand

def main():
    try:
        with open('5CPkrScore.dat', 'rb') as file:
            hiScore, name = pickle.load(file)
    except:
        hiScore, name = 0, ''

    chips = 3

    rules = input('\nWelcome to 5-Card Poker. Would you like to read the rules? (Y/N) ')
    if rules.title() == 'Y':
        print('\nThe dealer deals you 5 cards. After this deal, you may select whichever cards you want to keep to the next deal. All non-selected cards are swapped out for the next cards in the shuffled deck. The goal is to make tricks, as listed below before making your bet.')

    ent = input('\nTo begin, press enter. ')
    while ent != '':
        ent = input('Press enter to begin. ')

    while True:
        deck = Deck()
        deck.shuffle()

        if hiScore > 0:
            print(f'\nHigh Score: {name} - {hiScore}')

        # PAYOUT TABLE
        print('\n --- PAYOUTS ---')
        print('Royal Flush - 1000:1\nStraight Flush - 300:1\nFour of a Kind - 120:1\nFull House - 60:1\nFlush - 40:1\nStraight - 25:1\nThree of a Kind - 15:1\nTwo Pair - 8:1\nJacks or Better - 2:1')
        ent = input('\nTo continue, press enter. ')
        while ent != '':
            ent = input('Press enter to continue. ')

        bet = int(input(f'\nHow many chips would you like to bet? You have {chips} available. (Enter a number ≤{chips}) '))
        while bet > chips:
            bet = int(input(f'Please enter a number ≤{chips}. '))
        chips = chips - bet

        # initialise and display
        table = PokerHand(deck)
        print('\nYour initial cards are...')
        print(table.hand.display_deck())
        ent = input('To continue, press enter. ')
        while ent != '':
            ent = input('Press enter to continue. ')

        # select cards to carry through
        ids = []
        while True:
            id = input('\nEnter the number (1-5) of any cards you would like to swap, or press enter to continue to the next deal. ')
            while id != '':
                ids.append(int(id) - 1)
                id = input('Enter the number (1-5) of any cards you would like to swap, or press enter to continue to the next deal. ')
            cont = input('\nPress enter to continue to the next deal, or anything else to add new cards to swap. ')
            if cont == '':
                break
        
        # deal remaining cards
        for idx in ids:
            table.replaceCard(idx)
        print('\nYour final cards are...')
        print(table.hand.display_deck())

        print(f'You finish with {table.bestHand()[0]}')
        # do payout
        chips += table.bestHand()[1] * bet
        if chips > 0:
            again = input(f'\nEnter \'Y\' if you would like to play again, or anything else if you wish to cash out at {chips}. ')
            if again.title() == 'Y':
                continue
            else:
                if chips > hiScore:
                    print(f"\nCongratulations! You're cashing out a new high score of {chips}!")
                    name = input('Enter your name to associate with the high score: ').title()
                    with open('5CPkrScore.dat', 'wb') as file:
                        pickle.dump((chips, name), file)
                else:
                    print(f'\nThanks for playing, you cash out at {chips}.\nHigh Score: {hiScore} - {name}')
                break
        else:
            print('\nYou are out of chips. Try again later.')
            break

main()