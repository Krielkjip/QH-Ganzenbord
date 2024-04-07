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
        clear()
        draw_title()
        print("0 - Quit Game")
        print("1 - Start Game")
        drawline()
        dest = input("# ")
        if dest == "0":
            quit()
        elif dest == "1":
            main_menu = False
            settings_menu = True
        else:
            clear()
            drawline()
            print("False input please enter 0 or 1")
            drawline()
            input("> ")

    while settings_menu:
        clear()
        drawline()
        print("Settings Menu")
        drawline()
        print("Current amount of players:", players_amount)
        print("Current amount of tiles", tiles_amount)
        if double_trouble:
            print("Double Trouble in turned on")
        else:
            print("Double Trouble is turned off")
        drawline()
        print("0 - Back to main menu")
        print("1 - Start Game")
        print("2 - Change amount of players")
        print("3 - Change amount of tiles")
        print("4 - Double Trouble on <-> off")
        drawline()
        dest = input("# ")

        if dest == "0":
            settings_menu = False
            main_menu = True
        elif dest == "1":
            settings_menu = False
            game = True
            # player_data = create_player_list_data(players_amount)
            i = 0
            while i < players_amount:
                correct_name = True
                clear()
                drawline()
                print("Enter player", i + 1, "name")
                print("Max amount off characters is 8")
                drawline()
                name = input("# ")
                if name == "":
                    clear()
                    drawline()
                    print("Please enter something")
                    drawline()
                    input("> ")
                else:
                    if len(name) > 8:
                        clear()
                        drawline()
                        print("Name must be less than 8 characters")
                        drawline()
                        input("> ")
                    else:
                        for item in players_data:
                            if item[1] == name:
                                clear()
                                drawline()
                                print("That name is already in use")
                                drawline()
                                input("> ")
                                correct_name = False
                        if correct_name:
                            while True:
                                clear()
                                drawline()
                                print(name, "enter your lucky number")
                                print("Lucky number must be higher than 1 and less than", tiles_amount)
                                drawline()
                                dest = input("# ")
                                try:
                                    lucky_number = int(dest)
                                    if lucky_number <= 1 or lucky_number >= tiles_amount:
                                        clear()
                                        drawline()
                                        print("Lucky number must be higher than 1 and less than", tiles_amount)
                                        drawline()
                                        input("> ")
                                    else:
                                        i += 1
                                        players_data.append([1, name, lucky_number])
                                        print(players_data)
                                        break
                                except ValueError:
                                    clear()
                                    drawline()
                                    print("Please enter a number")
                                    drawline()
                                    input("> ")
            print(players_data)

        elif dest == "2":
            while True:
                clear()
                drawline()
                print("Minium amount of players is 2")
                drawline()
                dest = input("# ")
                try:
                    number = int(dest)
                    if number < 2:
                        clear()
                        drawline()
                        print("Minimum amount of players is 2")
                        drawline()
                        input("> ")
                    else:
                        players_amount = number
                        break
                except ValueError:
                    clear()
                    drawline()
                    print("Please enter a number")
                    drawline()
                    input("> ")
        elif dest == "3":
            while True:
                clear()
                drawline()
                print("Minium amount of tiles 10")
                drawline()
                dest = input("# ")
                try:
                    number = int(dest)
                    if number < 10:
                        clear()
                        drawline()
                        print("Amount of tiles must be at least 10")
                        drawline()
                        input("> ")
                    else:
                        tiles_amount = number
                        break
                except ValueError:
                    clear()
                    drawline()
                    print("Please enter a number")
                    drawline()
                    input("> ")
        elif dest == "4":
            while True:
                clear()
                drawline()
                print("1 - Turn Double Trouble on")
                print("2 - Turn Double Trouble off")
                drawline()
                dest = input("# ")

                if dest == "1":
                    double_trouble = True
                    break
                elif dest == "2":
                    double_trouble = False
                    break
                else:
                    clear()
                    drawline()
                    print("Please enter 1 or 2")
                    drawline()
                    input("> ")

        else:
            clear()
            drawline()
            print("False input please enter 0, 1, 2, 3 or 4")
            drawline()
            input("> ")

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
        clear()
        draw_title()
        print("0 - Quit Game")
        print("1 - Start New Game")
        drawline()
        dest = input("# ")
        if dest == "0":
            quit()
        elif dest == "1":
            new_game_menu = False
            settings_menu = True
        else:
            clear()
            drawline()
            print("False input please enter 0 or 1")
            drawline()
            input("> ")
