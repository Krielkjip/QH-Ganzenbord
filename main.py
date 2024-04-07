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
            invalid_input_message("False input please enter 0, 1, 2, 3 or 4")

    current_player_amount = players_amount
    while game:
        print(players_data)
        clear()
        drawlinelong()
        draw_board(tiles_amount, players_data)
        drawlinelong()
        print("Current player:", players_data[current_player][1])
        drawline()
        print("0 - Quit Game")
        print("1 - Roll dice")
        print("2 - Give up")

        drawline()
        dest = input("# ")

        if dest == "0":
            game = False
            main_menu = True
            players_data = []
        elif dest == "1":
            if double_trouble:
                game_over = double_trouble_roll_dice(players_data, current_player, tiles_amount)
            else:
                game_over = roll_dice(players_data, current_player, tiles_amount)
            print(game_over)
            if game_over == 1:
                game = False
                new_game_menu = True
                players_data = []
            elif game_over == 2:
                del players_data[current_player]
                current_player -= 1
                current_player_amount -= 1
                if current_player > current_player_amount - 1:
                    current_player = 0

                if not players_data:
                    clear()
                    drawline()
                    print("Game Over")
                    print("All players have been disqualified")
                    drawline()
                    input("> ")
                    game = False
                    new_game_menu = True
            if current_player >= current_player_amount - 1:
                current_player = 0
            else:
                current_player += 1
        elif dest == "2":
            clear()
            drawline()
            print(players_data[current_player][1], "has given up")
            print(players_data[current_player][1], "is out of the game")
            drawline()
            input("> ")
            del players_data[current_player]
            current_player_amount -= 1
            if current_player > current_player_amount - 1:
                current_player -= 1

            if len(players_data) == 1:
                clear()
                drawline()
                print(players_data[current_player][1], "is the only one left")
                print(players_data[current_player][1], "HAS WON!")
                drawline()
                input("> ")
                game = False
                new_game_menu = True
                players_data = []
        else:
            clear()
            drawline()
            print("False input please enter 0, 1 or 2")
            drawline()
            input("> ")

    while new_game_menu:
        dest = new_game_menu_run()

        if dest:
            new_game_menu = False
            settings_menu = True
