import os
import random

run = True
main_menu = True
settings_menu = False
game = False
new_game_menu = False

tiles_amount = 10
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


def draw2dice():
    print("    _______         _______    ")
    print("  /\\       \\      /\\       \\   ")
    print(" /()\\   ()  \\    /()\\   ()  \\  ")
    print("/    \\_______\\  /    \\_______\\ ")
    print("\\    /()     /  \\    /()     / ")
    print(" \\()/   ()  /    \\()/   ()  /  ")
    print("  \\/_____()/      \\/_____()/   ")


def drawline():
    print("Xx------------------------------xX")


def drawlinelong():
    print(
        "Xx---------------------------------------------------------------------------------------------------------xX")


def clear():
    os.system("cls")


def draw_board():
    something = False
    tiles_per_column = 20
    space = 20

    for x in range(1, tiles_per_column + 1):
        for y in range(x, tiles_amount + 1, tiles_per_column):
            total_name_len = 0
            print(f"{y:3}", end=":")
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


def roll_dice(players_data):
    dice_roll = random.randint(1, 6)
    next_loc = players_data[current_player][0] + dice_roll
    # current_player_lucky_number = players_data[current_player][2]
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
        return True
    else:
        return False


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
        print("Current amount of tiles", tiles_amount)
        drawline()
        print("0 - Back to main menu")
        print("1 - Start Game")
        print("2 - Change amount of players")
        print("3 - Change amount of tiles")
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
                print("Max amount off characters is 4")
                drawline()
                name = input("# ")
                if name == "":
                    clear()
                    drawline()
                    print("Please enter something")
                    drawline()
                    input("> ")
                else:
                    if len(name) > 4:
                        clear()
                        drawline()
                        print("Name must be less than 4 characters")
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
                                drawline()
                                dest = input("# ")
                                try:
                                    lucky_number = int(dest)
                                    if lucky_number <= 0 or lucky_number >= tiles_amount:
                                        clear()
                                        drawline()
                                        print("Lucky number must be higher than 0 and less than", tiles_amount)
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
                print("Maximum amount of players is 4")
                drawline()
                print("Enter new player amount:")
                dest = input("# ")
                try:
                    number = int(dest)
                    if number < 2 or number > 4:
                        clear()
                        drawline()
                        print("Amount of players must be between 2 and 4")
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
                print("Minium amount of tiles 20")
                print("Maximum amount of tiles 100")
                drawline()
                print("Enter new amount of tiles:")
                dest = input("# ")
                try:
                    number = int(dest)
                    if number < 20 or number > 100:
                        clear()
                        drawline()
                        print("Amount of tiles must be between 20 and 100")
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
        else:
            clear()
            drawline()
            print("False input please enter 0, 1, 2, or 3")
            drawline()
            input("> ")

    current_player_amount = players_amount
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
            game_over = roll_dice(players_data)
            if game_over:
                game = False
                new_game_menu = True
                players_data = []
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
            print(players_data)
            del players_data[current_player]
            print(players_data)
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
        drawline()
        print("            GANZENBORD")
        drawline()
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
