import pickle
import sys
import time

sys.path.insert(1, '/Users/linuskelsey/Desktop/Coding/Python/projects/card_games/objects')

from deck import Deck
from blackjackPlayer import BlackjackPlayer

def main():
    try:
        with open('BlkJckScore.dat', 'rb') as file:
            hiScore, name = pickle.load(file)
    except:
        hiScore, name = 0, ''

    print('\nWelcome to BlackJack! Try to get as close to 21 as you can without exceeding it, and beat the dealer!\n\nStart with 10 chips and see how high you can go.')
    print(f'High Score: {hiScore} - {name}\n')

    chips = 10

    ans = input('Enter \'Y\' to play and anything else to leave. ')

    if ans.title() == 'Y':
        while True:

            deck = Deck()
            deck.shuffle()

            bet = int(input(f'\n\nHow many chips would you like to bet? You have {chips} available. (Enter a number ≤{chips}) '))
            while bet > chips:
                bet = int(input(f'Please enter a number ≤{chips}. '))
            chips = chips - bet

            print('\nPayouts:\n  -- Bust - 0:1\n  -- Push - 1:1\n  -- Blackjack Push - 1.5:1\n  -- Win - 2:1\n  -- Blackjack - 3:1')
            print('\nDealer deals!\n')

            # Initialise players (user and dealer)
            player = BlackjackPlayer(deck)
            dealer = BlackjackPlayer(deck)

            blackjack = False
            bust = False

            begin = input('Press enter to continue. ')
            while begin != '':
                begin = input('Press enter to continue. ')

            # player's action loop
            while True:
                # Show dealer's first card
                print("\nDealer's cards:")
                print(dealer.deck.display_last_n(1))
                print('(Dealer has one unrevealed card)')

                # show player's cards
                print('\nYour cards:')
                print(player.deck.display_deck())

                # Print player score(s)
                if 21 in player.score_declare()[1]:
                    print('\nBlackjack! Can the dealer match you? ')
                    blackjack = True
                    player_final = 21
                    # chip mechanics later
                    cont = input('Press enter to continue. ')
                    while cont != '':
                        cont = input('Press enter to continue. ')
                    break
                elif min(player.score_declare()[1]) > 21:
                    bust = True
                    break
                else:
                    print(player.score_declare()[0])

                # deal subsequent player's cards until stick or bust
                hit = input('\nWould you like to 1) hit or 2) stand? ')
                while hit not in ['1', '2']:
                    hit = input('Please enter 1 (hit) or 2 (stand). ')

                if hit == '1':
                    drawn = player.hit()
                    print(f'\nYou drew the {drawn}.')
                if hit == '2':
                    possibles = [x if x < 21 else 0 for x in player.score_declare()[1]]
                    player_final = max(possibles)
                    print(f'\nStood at {player_final}.')

                    cont = input('Press enter to continue. ')
                    while cont != '':
                        cont = input('Press enter to continue. ')
                    break
            
            # loop for bust (just end things)
            if bust:
                print(f'\nBusted at {min(player.score_declare()[1])}.')
            else:
                # dealer's action loop
                while True:
                    # reveal dealer's second card
                    print("\nDealer's cards:")
                    print(dealer.deck.display_deck())
                    print(dealer.score_declare(dealer=True)[0])

                    # show player's score
                    if blackjack:
                        print('\nYour score is 21.')
                    else:
                        print('\n' + player.score_declare()[0])

                    # deal subsequent dealer's cards until stick or bust
                    if min(dealer.score_declare(dealer=True)[1]) > 21:
                        # modify as f-string for actual chip amount.
                        if blackjack:
                            print('\nDealer busts, you win 3x the chips you bet!')
                            chips += 3 * bet
                        else:
                            print('\nDealer busts, you win 2x the chips you bet!')
                            chips += 2 * bet
                        break
                    elif 21 in dealer.score_declare(dealer=True)[1]:
                        # f-string
                        if blackjack:
                            print('\nDealer matches blackjack, you receive 1.5x the chips you bet!')
                            chips += int(1.5 * bet)
                        else:
                            print('\nDealer hits blackjack and wins.')
                        break
                    elif min(dealer.score_declare(dealer=True)[1]) < 17:
                        print('\nDealer hits.')
                        drawn = dealer.hit()
                        ent = input('Press enter to continue. ')
                        while ent != '':
                            ent = input('Press enter to continue. ')
                        if ent == '':
                            print(f'Dealer draws the {drawn}.')
                            continue
                    else:
                        possibles = [x if x < 21 else 0 for x in dealer.score_declare(dealer=True)[1]]
                        if blackjack:
                            print('\nDealer cannot make blackjack, you win 3x the chips you bet!')
                            chips += 3 * bet
                            break
                        if max(possibles) > player_final:
                            print(f'\nDealer stands at {max(possibles)} and wins.')
                        elif max(possibles) == player_final:
                            print(f'\nDealer pushes at {player_final} and you are returned your chips.')
                            chips += bet
                        else:
                            print(f'\nDealer stands at {max(possibles)} and you win 2x the chips you bet!')
                            chips += 2 * bet
                        break
            
            if chips > 0:
                if chips > hiScore:
                    print(f"\nCongratulations! You're cashing out a new high score of {chips}!")
                    name = input('Enter your name to associate with the high score: ').title()
                    with open('BlkJckScore.dat', 'wb') as file:
                        pickle.dump((chips, name), file)
                again = input(f'\nEnter \'Y\' if you would like to play again, or anything else if you wish to cash out at {chips}. ')
                if again.title() == 'Y':
                    continue
                else:
                    print(f'\nThanks for playing, you cash out at {chips}.\nHigh Score: {hiScore} - {name}')
                break
            else:
                print('\nYou are out of chips. Try again later.')
                break

main()