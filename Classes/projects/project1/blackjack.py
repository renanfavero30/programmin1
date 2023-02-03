# import random number

# Include the file in the same folder here
from p1_random import P1Random

rng = P1Random() # outside the loop
# print(rng.next_int(13) + 1)

# Initiate the variables
game_continue = True
game_num = 0
player_wins = 0
dealer_wins = 0
tie_game = 0
player_percent = "{:.2%}".format(0)

# Control the number of games the player will play
while game_continue: # game #1, #2, #3

    # 1. Print the game number message
    game_num += 1
    print(f"START GAME #{game_num}")

    # 2. Deal a card to the player automatically
    player_hand = 0
    #DEAL A CARD
    card = rng.next_int(13) + 1
    if card == 1:
        print("Your card is a ACE!")
        card = 1
    elif 2 <= card <= 10:
        # Print the card value
        print(f"Your card is a {card}!")
    elif card == 11:
        print("Your card is a Jack!")
        card = 10
    elif card == 12:
        print("Your card is a QUEEN!")
        card = 10
    elif card == 13:
        print("Your card is a KING!")
        card = 10

    # 3. Add card number to the player hand value
    player_hand = player_hand + card

    #4. Print hand value
    print(f"Your hand is: {player_hand}")

    # 5. Keep playing the current game by prompting the player menu
    no_winner = True
    while no_winner:
        # Print the MENU options
        print("1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit")

        # ask/prompt player for an input to choose a menu option
        option = int(input("Choose an option: "))
        if option == 1:
            # Deal another card to the player
            # DEAL A CARD
            card = rng.next_int(13) + 1
            if card == 1:
                print("Your card is a ACE!")
                card = 1
            elif 2 <= card <= 10:
                # Print the card value
                print(f"Your card is a {card}!")
            elif card == 11:
                print("Your card is a Jack!")
                card = 10
            elif card == 12:
                print("Your card is a QUEEN!")
                card = 10
            elif card == 13:
                print("Your card is a KING!")
                card = 10

            # 3. Add card number to the player hand value
            player_hand = player_hand + card

            # 4. Print hand value
            print(f"Your hand is: {player_hand}")

            # 6. if player_hand == 21, print winnning message
            if player_hand == 21:
                print('BLACKJACK! You win!')

                # Update the number of player wins
                player_wins += 1
                no_winner = False

            # elif player_hend > 21, print losing message
            elif player_hand > 21:
                print('You exceeded 21! You lose.')
                # update the number of games dealer wins
                dealer_wins += 1
                no_winner = False

            # update stats
            player_percent = "{:.1%}".format(player_wins / game_num)
            continue

        elif option == 2:
            # deal a card to the dealer
            dealer_hand = rng.next_int(11) + 16

            # print dealer card
            print(f"Dealer's hand: {dealer_hand}")
            print(f"Your hand is: {player_hand}")
            # compare player hand with dealer hand value
            if dealer_hand > 21:
                print('You win!')
                player_wins += 1
            # compare player hand with dealer hand value
            elif dealer_hand == player_hand:
                tie_game += 1
                print("It's a tie! No one wins!")
            elif dealer_hand == 21:
                print('Dealer wins!')
                dealer_wins += 1
            else:
                if dealer_hand > player_hand:
                    print("Dealer wins!")
                    dealer_wins += 1
                else:
                    print("You win!")
                    player_wins += 1

            # update stats
            player_percent = "{:.1%}".format(player_wins / game_num)

            # and determine who wins the game
            # update the statistics (number of games player/dealer wins
            no_winner = False
        # option to show stats
        elif option == 3:
            # print stats: playerwins and dealer_wins
            print(f'Number of Player wins: {player_wins}')
            print(f'Number of Dealer wins: {dealer_wins}')
            print(f'Number of tie games: {tie_game}')
            print(f'Total # of games played is: {game_num-1}')
            print(f'Percentage of Player wins: {player_percent}')
        # option exit
        elif option == 4:
            no_winner = False # get outside of the inner while
            game_continue = False # get outside the outer while
        # option error
        else:
            print('Invalid input!\nPlease enter an integer value between 1 and 4.')




