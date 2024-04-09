from functions import *

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
        dest = main_menu_run()

        if dest:
            main_menu = False
            settings_menu = True

    while settings_menu:
        clear()
        drawline()
        print("Settings Menu")
        drawline()
        print("Current amount of players:", players_amount)
        print("Current amount of tiles", tiles_amount)
        print("Double Trouble is", "on" if double_trouble else "off")
        drawline()
        print("0 - Back to main menu")
        print("1 - Start Game")
        print("2 - Change amount of players")
        print("3 - Change amount of tiles")
        print("4 - Toggle Double Trouble")
        drawline()
        dest = input("# ")

        if dest == "0":
            settings_menu = False
            main_menu = True
        elif dest == "1":
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
        elif dest == "2":
            players_amount = update_players_amount()
        elif dest == "3":
            tiles_amount = update_tiles_amount()
        elif dest == "4":
            if double_trouble:
                double_trouble = False
            else:
                double_trouble = True
        else:
            invalid_input_message("Please enter 0, 1, 2, 3 or 4")

    current_player_amount = players_amount
    while game:
        dest = game_run(players_data, current_player, current_player_amount, tiles_amount, double_trouble, well_loc,
                        thorn_bush_loc)

        if dest[0]:
            game = False
            new_game_menu = True
            players_data = []
        else:
            current_player = dest[1]
            current_player_amount = dest[2]

    while new_game_menu:
        dest = new_game_menu_run()

        if dest:
            new_game_menu = False
            settings_menu = True
