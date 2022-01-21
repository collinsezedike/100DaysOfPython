############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################


#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game. 
# I don't think I wanna do this.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
# There will be a problem in the rare case of two ace draws


#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

import random
from blackjack_art import logo


def deal_card(player):
    '''Deals a random card to the player that is passed as argument'''
    player.append(random.choice(cards))


def calculate_score(cards):
    '''Returns the sum of the cards a player has'''
    score = sum(cards)

    if score == 21 and len(cards) == 2:
        return 0     # 0 represents Blackjack
    elif score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return score


def compare(player1_score, player2_score):
    '''Returns the outcome from comparing the players' scores'''
    if player1_score == player2_score:
        return "It's a draw!"
    elif player2_score == 0:
        return "Computer got Blackjack. You lose."
    elif player1_score == 0:
        return "Blackjack! You win!"
    if player1_score > 21:
        return 'Bust. You lose.'
    elif player2_score > 21:
        return 'Computer busts. You win!'
    elif player1_score > player2_score:
        return 'You score more than computer. You win!'
    elif player1_score < player2_score:
        return 'Computer tops your score. You lose.'


game_lingo = """
Blackjack Lingo:

    Hit - means to take another card.
    Stand - means to take no more cards.
    Bust - means score is above 21.
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game_over = False
while not game_over:
    print(logo)
    print('Welcome! To the most widely played casino banking game in the world - BlackJack!')
    print(f'{game_lingo}')
    user_hand = []
    computer_hand = []
    bust = False
    
    for _ in range(2):
        deal_card(user_hand)
        deal_card(computer_hand)

    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)

    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
        print(f'\nYour final hand: {user_hand}, final score: {user_score}')
        print(f"Computer's final hand: {computer_hand}, computer's score: {computer_score}")
    else:
        print(f'Your cards: {user_hand}, current score: {user_score}')

    redraw = True
    while redraw and not game_over:
        print(f"Computer's first card: {computer_hand[0]}")

        hitorstand =input("\nType 'y' to Hit, type 'n' to Stand: ")
        if hitorstand == 'y':
            redraw = True
            deal_card(user_hand)
            user_score = calculate_score(user_hand)

            if user_score > 21:
                game_over = True
                print(f'\nYour final hand: {user_hand}, final score: {user_score}')
                while computer_score < 17:
                    deal_card(computer_hand)
                    computer_score = calculate_score(computer_hand)
                print(f"Computer's final hand: {computer_hand}, computer's score: {computer_score}")
            else:
                print(f'Your cards: {user_hand}, current score: {user_score}')

        else:
            redraw = False
            user_score = calculate_score(user_hand)
            print(f'\nYour final hand: {user_hand}, final score: {user_score}')
            
            while computer_score < 17:
                deal_card(computer_hand)
                computer_score = calculate_score(computer_hand)
            print(f"Computer's final hand: {computer_hand}, computer's final score: {computer_score}")
            
    judgement = compare(player1_score = user_score, player2_score = computer_score)
    print(judgement)

    if input("\nDo you want to play again? Type 'y' or 'n': ") == 'n':
        game_over = True
        print('Game over!')
    else:
        game_over = False