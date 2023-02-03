option = 1
game_continue = True
blackjack_game = True

while blackjack_game:
    print("game number: ", game_number)

    # for one specific game e.g., game #1
    while game_continue:
        option = int(input("what is your next option"))
        if option == 1:
            print("deal a new card to the player")
        elif option == 2:
            print("deal a card to the dealer")
            # compare player and dealer hands
        elif option == 3:
            print("print stats")
        elif option == 4:
            game_continue = False

