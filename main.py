import os

run = True
main_menu = True
settings_menu = False
game = False

tiles_amount = 63
players_amount = 2


def drawline():
    print("Xx------------------------------xX")


def clear():
    os.system("cls")


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
