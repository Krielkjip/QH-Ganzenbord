import os

run = True
main_menu = True
settings_menu = False
game = False

tiles_amount = 63
players_amount = 2
players_data = []


def drawline():
    print("Xx------------------------------xX")


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
            for item in players_data:
                if item[0] == y:
                    print(item[1], end=" ")
                    total_name_len += len(item[1]) + 1
                    something = True
            if something:
                for i in range(0, space - total_name_len):
                    print(" ", end="")
            else:
                for i in range(0, space):
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
            x = 0
            while x < players_amount:
                clear()
                drawline()
                print("Enter player", x + 1, "name")
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
                        x += 1
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
        drawline()
        draw_board()
        drawline()
        print("0 - Quit Game")
        drawline()
        dest = input("# ")

        if dest == "0":
            game = False
            main_menu = True
        else:
            clear()
            drawline()
            print("False input please enter 0")
            drawline()
            input("> ")
