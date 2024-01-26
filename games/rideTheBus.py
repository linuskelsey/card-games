import pickle
import sys

sys.path.insert(1, '/Users/linuskelsey/Desktop/Coding/Python/projects/card_games/objects')

from deck import Deck


def main():
    try:
        with open('RtBscore.dat', 'rb') as file:
            hiScore = pickle.load(file)
    except:
        hiScore = 0

    while True:
        print('\nWelcome to this game of Ride the Bus! Answer these questions about a deck of cards correct to win the game :)\n')
        print(f'High Score: {hiScore}\n')

        deck = Deck()
        deck.shuffle()

        stack = Deck(full=False)
        guesses = 0

        print('\t--- Question 1. Red or Black? ---\n')
        while True:
            if deck.cards == []:
                print("Oh no! You've run out of cards! Please try again another time.")
                return
            

            ans = input('Will the next card be 1) Red, or 2) Black? ')
            while ans not in ['1', '2']:
                ans = input('Please enter 1 (red) or 2 (black). ')
            guesses += 1

            card = deck.deal()
            stack.add_to_bottom(card)
            print(stack.display_last_n(5))

            if card.suit in ['D', 'H']:
                if ans == '1':
                    print(f'Congratulations, you drew the {card}, so you guessed right!\n')
                    break
            if card.suit in ['C', 'S']:
                if ans == '2':
                    print(f'Congratulations, you drew the {card}, so you guessed right!\n')
                    break

            print(f"Unlucky, you drew the {card}. Let's give it another go, shall we?\n")
        

        print('\t--- Question 2. Higher or Lower? ---\n')
        while True:
            if deck.cards == []:
                print("Oh no! You've run out of cards! Please try again another time.")
                return
            
            ans = input('Will the next card be 1) higher or 2) lower than your previous card (with equality)? ')
            while ans not in ['1', '2']:
                ans = input('Please enter 1 (lower) or 2 (higher). ')
            guesses += 1

            card = deck.deal()
            stack.add_to_bottom(card)
            print(stack.display_last_n(5))

            if card.rank_num >= stack.cards[-2].rank_num:
                if ans == '1':
                    print(f'Congratulations, you drew the {card}, so you guessed right!\n')
                    break

            if card.rank_num <= stack.cards[-2].rank_num:
                if ans == '2':
                    print(f'Congratulations, you drew the {card}, so you guessed right!\n')
                    break
            
            print(f"Unlucky, you drew the {card}. Let's give it another go, shall we?\n")


        print('\t--- Question 3. In-between or Outside? ---\n')
        while True:
            if deck.cards == []:
                print("Oh no! You've run out of cards! Please try again another time.")
                return
            
            ans = input('Will the next card be 1) in between or 2) outside your last two in rank (with equality)? ')
            while ans not in ['1', '2']:
                ans = input('Please enter 1 (between) or 2 (outside). ')
            guesses += 1

            card = deck.deal()
            stack.add_to_bottom(card)
            print(stack.display_last_n(5))

            smaller = min(stack.cards[-3].rank_num, stack.cards[-2].rank_num)
            larger = max(stack.cards[-3].rank_num, stack.cards[-2].rank_num)
            betweens = list(range(smaller, larger+1))

            if card.rank_num in betweens:
                if ans == '1':
                    print(f'Congratulations, you drew the {card}, so you guessed right!\n')
                    break
                else:
                    print(f"Unlucky, you drew the {card}. Let's give it another go, shall we?\n")
                    continue

            if ans == '2':
                print(f'Congratulations, you drew the {card}, so you guessed right!\n')
                break

            print(f"Unlucky, you drew the {card}. Let's give it another go, shall we?\n")


        print('\t--- Question 4. Which Suit? ---\n')
        while True:
            if deck.cards == []:
                print("Oh no! You've run out of cards! Please try again another time.")
                return
            
            ans = input('Enter the initial of the suit of your next card. ')
            while ans.title() not in ['C', 'S', 'D', 'H']:
                ans = input('Please type one of C, S, D and H. ')
            ans = ans.title()
            guesses += 1

            card = deck.deal()
            stack.add_to_bottom(card)
            print(stack.display_last_n(5))

            if card.suit == ans:
                print(f'Congratulations, you drew the {card}, so you guessed right!\n')
                break

            print(f"Unlucky, you drew the {card}. Let's give it another go, shall we?\n")


        print('\t--- Question 5. Which Rank? ---\n')
        while True:
            if deck.cards == []:
                print("Oh no! You've run out of cards! Please try again another time.")
                return
            
            ans = input('Enter the rank of your next card. ')
            while ans.title() not in [str(x) for x in range(2,11)] + ['J', 'Q', 'K', 'A']:
                ans = input('Please enter a valid rank. ')
            ans = ans.title()
            guesses += 1

            card = deck.deal()
            stack.add_to_bottom(card)
            print(stack.display_last_n(5))

            if card.rank == ans:
                print(f'Congratulations, you drew the {card}, so you guessed right!\n')
                break

            print(f"Unlucky, you drew the {card}. Let's give it another go, shall we?\n")


        print('\t--- Question 6. Which Card? ---\n')
        while True:
            if deck.cards == []:
                print("Oh no! You've run out of cards! Please try again another time.")
                return
            
            rank = input('Enter the rank of your next card. ')
            suit = input('Enter the initial of the suit of your next card. ')
            while rank.title() not in [str(x) for x in range(2,11)] + ['J', 'Q', 'K', 'A']:
                rank = input('Please enter a valid rank. ')
            while suit.title() not in ['C', 'S', 'D', 'H']:
                suit = input('Please type one of C, S, D and H. ')
            rank = rank.title()
            suit = suit.title()
            guesses += 1

            card = deck.deal()
            stack.add_to_bottom(card)
            print(stack.display_last_n(5))

            if card.suit == suit and card.rank == rank:
                print(f'Congratulations, you drew the {card}, so you guessed right!\n')
                break

            print(f"Unlucky, you drew the {card}. Let's give it another go, shall we?\n")

        if guesses < hiScore or hiScore == 0:
            print(f'Congratulations! You finished the game in {guesses} guesses! New high score!')
            with open('RtBscore.dat', 'wb') as file:
                pickle.dump(guesses, file)
                hiScore = guesses
        else:
            print(f'Congratulations! You finished the game in {guesses} guesses!\nHigh score: {hiScore}')

        again = input('Play again? (Y/N) ')
        while again.title() not in ['Y', 'N']:
            again = input('Please enter Y or N. ')

        if again.title() == 'N':
            break
        
        print('\n')

    return

main()