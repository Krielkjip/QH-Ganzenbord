import os
import random

run = True
main_menu = True
settings_menu = False
game = False

tiles_amount = 20
players_amount = 2
players_data = []
current_player = 0


def drawdice():
    print("    _______    ")
    print("  /\\       \\   ")
    print(" /()\\   ()  \\  ")
    print("/    \\_______\\ ")
    print("\\    /()     / ")
    print(" \\()/   ()  /  ")
    print("  \\/_____()/   ")


def drawline():
    print("Xx------------------------------xX")


def drawlinelong():
    print("Xx------------------------------------------------------------------------------------------xX")


def clear():
    os.system("cls")


def draw_board():
    something = False
    tiles_per_column = 20
    space = 20

    for x in range(1, tiles_per_column + 1):
        for y in range(x, tiles_amount + 1, tiles_per_column):
            total_name_len = 0
            print(f"{y:2}", end=":")
            for player in players_data:
                if player[0] == y:
                    print(player[1], end=" ")
                    total_name_len += len(player[1]) + 1
                    something = True
            if something:
                for z in range(0, space - total_name_len):
                    print(" ", end="")
            else:
                for z in range(0, space):
                    print(" ", end="")

        print()


while run:
    while main_menu:
        clear()
        drawline()
        print("            GANZENBORD")
        drawline()
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
        drawline()
        print("0 - Back to main menu")
        print("1 - Start Game")
        print("2 - Change player amount")
        print("3 - Change tiles amount")
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
                            i += 1
                            players_data.append([1, name])
            print(players_data)

        elif dest == "2":
            pass
        elif dest == "3":
            pass
        else:
            clear()
            drawline()
            print("False input please enter 0, 1, 2, or 3")
            drawline()
            input("> ")

    while game:
        clear()
        drawlinelong()
        draw_board()
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
            dice_roll = random.randint(1, 6)
            next_loc = players_data[current_player][0] + dice_roll
            if next_loc > tiles_amount:
                clear()
                drawdice()
                drawline()
                print(players_data[current_player][1], "rolled a dice")
                print(players_data[current_player][1], "rolled", dice_roll)
                print(players_data[current_player][1], "moved to far and got thrown back")
                print(players_data[current_player][1], "moved to", tiles_amount - next_loc % tiles_amount)
                drawline()
                input("> ")
                players_data[current_player][0] = tiles_amount - next_loc % tiles_amount
            else:
                clear()
                drawdice()
                drawline()
                print(players_data[current_player][1], "rolled a dice")
                print(players_data[current_player][1], "rolled", dice_roll)
                print(players_data[current_player][1], "moved to", next_loc)
                drawline()
                input("> ")
                players_data[current_player][0] += dice_roll
            if next_loc == tiles_amount:
                clear()
                drawline()
                print(players_data[current_player][1], "HAS WON!")
                drawline()
                input("> ")
                game = False
                main_menu = True
                players_data = []

            if current_player == players_amount - 1:
                current_player = 0
            else:
                current_player += 1
        elif dest == "2":
            if current_player == players_amount - 1:
                winner = 0
            else:
                winner = 1

            clear()
            drawline()
            print(players_data[current_player][1], "has given up")
            print(players_data[current_player][1], "has lost")
            print(players_data[winner][1], "wins")
            drawline()
            input("> ")
            game = False
            main_menu = True
            players_data = []
        else:
            clear()
            drawline()
            print("False input please enter 0, 1 or 2")
            drawline()
            input("> ")
