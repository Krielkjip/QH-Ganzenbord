from functions import *
import random

# Set start Boolean values
run = True
main_menu = True
settings_menu = False
game = False
new_game_menu = False
double_trouble = True

# Set starter values for variables
tiles_amount = 63
players_amount = 2
players_data = []
current_player = 0
well_loc = 0
thorn_bush_loc = 0

# Main loop
while run:
    # Main menu loop
    while main_menu:
        user_input = main_menu_run()

        if user_input:
            # Changes current loop to settings menu loop
            main_menu = False
            settings_menu = True

    # Settings menu loop
    while settings_menu:
        draw_settings_menu(players_amount, tiles_amount, double_trouble)
        user_input = input("# ")

        # If User wants to quit to settings menu
        if user_input == "0":
            settings_menu = False
            main_menu = True
        # If User wants to start the game
        elif user_input == "1":
            # Create player list
            players_data = create_player_list_data(players_amount, tiles_amount)
            # Create location for well and bush and check so that they are not on the same tile
            while True:
                well_loc = random.randint(2, tiles_amount - 1)
                thorn_bush_loc = random.randint(9, tiles_amount - 1)
                if well_loc == thorn_bush_loc:
                    well_loc = random.randint(2, tiles_amount - 1)
                    thorn_bush_loc = random.randint(9, tiles_amount - 1)
                else:
                    break
            settings_menu = False
            game = True
        # If user wants to change amount of players
        elif user_input == "2":
            players_amount = update_players_amount()
        # If user wants to change the amount of tiles
        elif user_input == "3":
            tiles_amount = update_tiles_amount()
        # If user want to switch double trouble on/off
        elif user_input == "4":
            if double_trouble:
                double_trouble = False
            else:
                double_trouble = True
        else:
            invalid_input_message("Please enter 0, 1, 2, 3 or 4")

    # Define current amount of players
    current_player_amount = players_amount
    # Game loop
    while game:
        user_input = game_run(players_data, current_player, current_player_amount, tiles_amount, double_trouble,
                              well_loc,
                              thorn_bush_loc)
        # Go to new game menu loop
        if user_input[0]:
            game = False
            new_game_menu = True
            players_data = []
        else:
            current_player = user_input[1]
            current_player_amount = user_input[2]

    # New game menu loop
    while new_game_menu:
        user_input = new_game_menu_run()

        if user_input:
            new_game_menu = False
            settings_menu = True
