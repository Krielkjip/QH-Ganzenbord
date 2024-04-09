from functions import *
import random

run = True
main_menu = True
settings_menu = False
game = False
new_game_menu = False
double_trouble = True

tiles_amount = 63
players_amount = 2
players_data = []
current_player = 0
well_loc = 0
thorn_bush_loc = 0

while run:
    while main_menu:
        user_input = main_menu_run()

        if user_input:
            main_menu = False
            settings_menu = True

    while settings_menu:
        draw_settings_menu(players_amount, tiles_amount, double_trouble)
        user_input = input("# ")

        if user_input == "0":
            settings_menu = False
            main_menu = True
        elif user_input == "1":
            players_data = create_player_list_data(players_amount, tiles_amount)
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
        elif user_input == "2":
            players_amount = update_players_amount()
        elif user_input == "3":
            tiles_amount = update_tiles_amount()
        elif user_input == "4":
            if double_trouble:
                double_trouble = False
            else:
                double_trouble = True
        else:
            invalid_input_message("Please enter 0, 1, 2, 3 or 4")

    current_player_amount = players_amount
    while game:
        user_input = game_run(players_data, current_player, current_player_amount, tiles_amount, double_trouble,
                              well_loc,
                              thorn_bush_loc)

        if user_input[0]:
            game = False
            new_game_menu = True
            players_data = []
        else:
            current_player = user_input[1]
            current_player_amount = user_input[2]

    while new_game_menu:
        user_input = new_game_menu_run()

        if user_input:
            new_game_menu = False
            settings_menu = True
