import os


# Function that draws the games title
def draw_title():
    print(r"Xx--------------------------------------------------------xX")
    print(r"x   _____                           _                   _  x")
    print(r"|  / ____|                         | |                 | | |")
    print(r"| | |  __  __ _ _ __  _______ _ __ | |__   ___  _ __ __| | |")
    print(r"| | | |_ |/ _` | '_ \|_  / _ \ '_ \| '_ \ / _ \| '__/ _` | |")
    print(r"| | |__| | (_| | | | |/ /  __/ | | | |_) | (_) | | | (_| | |")
    print(r"x  \_____|\__,_|_| |_/___\___|_| |_|_.__/ \___/|_|  \__,_| x")
    print(r"Xx--------------------------------------------------------xX")


# Function that draws 1 dice
def draw_dice():
    print(r"   ________    ")
    print(r"  /\       \   ")
    print(r" /()\   ()  \  ")
    print(r"/    \_______\ ")
    print(r"\    /()     / ")
    print(r" \()/   ()  /  ")
    print(r"  \/_____()/   ")


# Function that draws 2 dices
def draw2_dice():
    print(r"   ________        ________    ")
    print(r"  /\       \      /\       \   ")
    print(r" /()\   ()  \    /()\   ()  \  ")
    print(r"/    \_______\  /    \_______\ ")
    print(r"\    /()     /  \    /()     / ")
    print(r" \()/   ()  /    \()/   ()  /  ")
    print(r"  \/_____()/      \/_____()/   ")


# Function that draws a short line
def drawline():
    print("Xx----------------------------------------xX")


# Function that draws a long line
def drawline_long():
    print(
        "Xx---------------------------------------------------------------------------------------------------------xX")


# Function that clears the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
