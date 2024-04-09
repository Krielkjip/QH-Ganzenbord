from draw_functions import *
from tiles_logic import well_logic, thorn_bush_logic
import random


def draw_settings_menu(players_amount, tiles_amount, double_trouble):
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


def draw_board(tiles_amount, players_data, put_loc, thorn_bush_loc):
    y = len(str(tiles_amount))
    for x in range(1, tiles_amount + 1):
        print(f"{x:{y}}", end=": ")
        if x == put_loc:
            print("(Well)", end=" ")
        if x == thorn_bush_loc:
            print("(Thorn Bush)", end=" ")

        for player in players_data:
            if player[0] == x:
                print(player[1], end=" ")

        print("")


def roll_dice(players_data, current_player, tiles_amount, well_loc, thorn_bush_loc, double_trouble):
    dice_roll1 = random.randint(1, 6)
    dice_roll2 = random.randint(1, 6)
    if double_trouble:
        dice_total = dice_roll1 + dice_roll2
    else:
        dice_total = dice_roll1

    next_loc = players_data[current_player][0] + dice_total
    current_player_lucky_number = players_data[current_player][2]

    if players_data[current_player][3]:
        clear()
        drawline()
        print(players_data[current_player][1], "is stuck in the well and can't move")
        drawline()
        input("> ")
    else:
        if double_trouble:
            if dice_roll1 == dice_roll2:
                clear()
                draw2_dice()
                drawline()
                print(players_data[current_player][1], "rolled 2 dices")
                print("Both Dices rolled", dice_roll1)
                print(players_data[current_player][1], "has been disqualified")
                drawline()
                input("> ")
                return 2

        if next_loc > tiles_amount:
            clear()
            draw_dice() if not double_trouble else draw2_dice()
            drawline()
            print(players_data[current_player][1], "rolled 2 dices" if double_trouble else "rolled a dice")
            print(players_data[current_player][1], "rolled", dice_roll1, "and",
                  dice_roll2) if double_trouble else print(players_data[current_player][1], "rolled", dice_roll1)
            print(players_data[current_player][1], "moved too far and got thrown back")
            print(players_data[current_player][1], "moved from", players_data[current_player][0], "to",
                  tiles_amount - next_loc % tiles_amount)
            drawline()
            input("> ")
            players_data[current_player][0] = tiles_amount - next_loc % tiles_amount
        else:
            clear()
            draw_dice() if not double_trouble else draw2_dice()
            drawline()
            print(players_data[current_player][1], "rolled 2 dices" if double_trouble else "rolled a dice")
            print(players_data[current_player][1], "rolled", dice_roll1, "and",
                  dice_roll2) if double_trouble else print(players_data[current_player][1], "rolled", dice_roll1)
            print(players_data[current_player][1], "moved from", players_data[current_player][0], "to", next_loc)
            drawline()
            input("> ")
            players_data[current_player][0] += dice_total

        if players_data[current_player][0] == current_player_lucky_number:
            next_loc = players_data[current_player][0] + dice_total
            if next_loc > tiles_amount:
                clear()
                drawline()
                print(players_data[current_player][1], "landed on", players_data[current_player][0])
                print("That is", players_data[current_player][1], "lucky number")
                print(players_data[current_player][1], "moved another", dice_total)
                print(players_data[current_player][1], "moved too far and got thrown back")
                print(players_data[current_player][1], "moved to", tiles_amount - next_loc % tiles_amount)
                drawline()
                input("> ")
                players_data[current_player][0] = tiles_amount - next_loc % tiles_amount
            else:
                clear()
                drawline()
                print(players_data[current_player][1], "landed on", players_data[current_player][0])
                print("That is", players_data[current_player][1], "lucky number")
                print(players_data[current_player][1], "moved another", dice_total)
                print(players_data[current_player][1], "moved to", next_loc)
                drawline()
                input("> ")
                players_data[current_player][0] += dice_total

        if players_data[current_player][0] == thorn_bush_loc:
            thorn_bush_logic(players_data, current_player)

        if next_loc == tiles_amount:
            clear()
            drawline()
            print(players_data[current_player][1], "HAS WON!")
            drawline()
            input("> ")
            return 1
        else:
            if players_data[current_player][0] == well_loc:
                well_logic(players_data, current_player)
            return 0


def main_menu_run():
    while True:
        clear()
        draw_title()
        print("0 - Quit Game")
        print("1 - Start Game")
        drawline()
        user_input_fun = input("# ")
        if user_input_fun == "0":
            quit()
        elif user_input_fun == "1":
            return True
        else:
            invalid_input_message("Please enter 0 or 1")


def new_game_menu_run():
    while True:
        clear()
        draw_title()
        print("0 - Quit Game")
        print("1 - Start New Game")
        drawline()
        user_input_fun = input("# ")
        if user_input_fun == "0":
            quit()
        elif user_input_fun == "1":
            return True
        else:
            invalid_input_message("Please enter 0 or 1")


def update_players_amount():
    while True:
        clear()
        drawline()
        print("Minimum amount of players is 2")
        drawline()
        user_input_fun = input("# ")
        try:
            number = int(user_input_fun)
            if number < 2:
                invalid_input_message("Minimum amount of players is 2")
            else:
                return number
        except ValueError:
            invalid_input_message("Please enter a number")


def update_tiles_amount():
    while True:
        clear()
        drawline()
        print("Minimum amount of tiles is 10")
        drawline()
        user_input_fun = input("# ")
        try:
            number = int(user_input_fun)
            if number < 10:
                invalid_input_message("Minimum amount of tiles is 10")
            else:
                return number
        except ValueError:
            invalid_input_message("Please enter a number")


def invalid_input_message(message):
    clear()
    drawline()
    print("False input please enter a valid option")
    print(message)
    drawline()
    input("> ")


def create_player_list_data(amount, tiles_amount):
    player_data = []
    for i in range(amount):
        correct_name = True
        while True:
            clear()
            drawline()
            print("Enter player", i + 1, "name")
            print("Max amount of characters is 8")
            drawline()
            name = input("# ")
            if name == "":
                invalid_input_message("Please enter something")
            elif len(name) > 8:
                invalid_input_message("Name must be less than 8 characters")
            else:
                if any(item[1] == name for item in player_data):
                    invalid_input_message("That name is already in use")
                    correct_name = False
                if correct_name:
                    while True:
                        clear()
                        drawline()
                        print(name, "enter your lucky number")
                        print("Lucky number must be higher than 1 and less than", tiles_amount)
                        drawline()
                        user_input_fun = input("# ")
                        try:
                            lucky_number = int(user_input_fun)
                            if lucky_number <= 1 or lucky_number >= tiles_amount:
                                invalid_input_message(
                                    f"Lucky number must be higher than 1 and less than {tiles_amount}")
                            else:
                                player_data.append([1, name, lucky_number, False])
                                break
                        except ValueError:
                            invalid_input_message("Please enter a number")
                break
    return player_data


def game_run(players_data, current_player, current_player_amount, tiles_amount, double_trouble, well_loc,
             thorn_bush_loc):
    print(players_data)
    clear()
    drawline_long()
    draw_board(tiles_amount, players_data, well_loc, thorn_bush_loc)
    drawline_long()
    print("Current player:", players_data[current_player][1])
    drawline()
    print("0 - Quit Game")
    print("1 - Roll dice")
    print("2 - Give up")

    drawline()
    user_input_fun = input("# ")

    if user_input_fun == "0":
        return True, current_player, current_player_amount
    elif user_input_fun == "1":
        if double_trouble:
            game_over = roll_dice(players_data, current_player, tiles_amount, well_loc, thorn_bush_loc, True)
        else:
            game_over = roll_dice(players_data, current_player, tiles_amount, well_loc, thorn_bush_loc, False)
        print(game_over)

        if current_player > current_player_amount - 1:
            current_player = 0
        if len(players_data) == 1:
            if players_data[current_player][3]:
                clear()
                drawline()
                print("All players have been disqualified except", players_data[current_player][1])
                print("But", players_data[current_player][1], "is stuck in a well")
                print("Game Over")
                drawline()
                input("> ")
                return True, current_player, current_player_amount

        if game_over == 1:
            return True, current_player, current_player_amount
        elif game_over == 2:
            del players_data[current_player]
            current_player -= 1
            current_player_amount -= 1
            if not players_data:
                clear()
                drawline()
                print("Game Over")
                print("All players have been disqualified")
                drawline()
                input("> ")
                return True, current_player, current_player_amount
        if current_player >= current_player_amount - 1:
            current_player = 0
        else:
            current_player += 1
    elif user_input_fun == "2":
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
            return True, current_player, current_player_amount

        if not len(players_data):
            clear()
            drawline()
            print("The last player was done with the game and gave up")
            print("Game over")
            drawline()
            input("> ")
            return True, current_player, current_player_amount
    else:
        invalid_input_message("Please enter 0, 1 or 2")

    return False, current_player, current_player_amount
