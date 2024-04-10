from draw_functions import *
from tiles_logic import well_logic, thorn_bush_logic
import random


# Function that draws Settings Menu
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


# Function that draws the game board
def draw_board(tiles_amount, players_data, put_loc, thorn_bush_loc):
    # Calculate how long the longest number in the board is so they all get printed with the same length
    y = len(str(tiles_amount))
    # Loop for all tiles
    for x in range(1, tiles_amount + 1):
        # Print the Tile with the correct amount of space before it
        print(f"{x:{y}}", end=": ")
        # Check in there is a special tile on current printed tile and print it
        if x == put_loc:
            print("(Well)", end=" ")
        if x == thorn_bush_loc:
            print("(Thorn Bush)", end=" ")

        # Check if there is a player in the current printed tile and print their name
        for player in players_data:
            if player[0] == x:
                print(player[1], end=" ")

        # Move to the next line
        print("")


# Function to roll the dice/dices and change the location of the player and status of player
def roll_dice(players_data, current_player, tiles_amount, well_loc, thorn_bush_loc, double_trouble):
    # Roll dices
    dice_roll1 = random.randint(1, 6)
    dice_roll2 = random.randint(1, 6)
    # Check if it is a double trouble roll
    if double_trouble:
        dice_total = dice_roll1 + dice_roll2
    else:
        dice_total = dice_roll1

    # Calculate the next location based on the dice roll
    next_loc = players_data[current_player][0] + dice_total
    # Get player lucky number
    current_player_lucky_number = players_data[current_player][2]

    # If player is stuck in well print message and end move
    if players_data[current_player][3]:
        clear()
        drawline()
        print(players_data[current_player][1], "is stuck in the well and can't move")
        drawline()
        input("> ")
    else:
        # Check for double trouble
        if double_trouble:
            # If both dices rolled the same disqualify player
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

        # Check if player moved out of map and move player back in the board
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

        # Check if player landed on their lucky number and move them the same number of tiles again
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

        # Check if player landed on the thorn bush
        if players_data[current_player][0] == thorn_bush_loc:
            thorn_bush_logic(players_data, current_player)

        # Check if player reached the end of the board and print player won
        if next_loc == tiles_amount:
            clear()
            drawline()
            print(players_data[current_player][1], "HAS WON!")
            drawline()
            input("> ")
            return 1
        else:
            # Check if player landed on the well
            if players_data[current_player][0] == well_loc:
                well_logic(players_data, current_player)
            return 0


# Function that displays main menu and asks for a user input
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


# Function that displays the new game menu and asks for a user input
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


# Update the number of players and check if the number of players is at least 2
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


# Update the number of tiles and check if the number of tiles is at least 10
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


# Function that prints the invalid input message
def invalid_input_message(message):
    clear()
    drawline()
    print("False input please enter a valid option")
    print(message)
    drawline()
    input("> ")


# Function that creates the player list with curren tile, name, lucky number, in well true/false
def create_player_list_data(amount, tiles_amount):
    # Create empty list
    player_data = []
    # Loop trough each player
    for i in range(amount):
        correct_name = True
        # Input name
        while True:
            clear()
            drawline()
            print("Enter player", i + 1, "name")
            print("Max amount of characters is 8")
            drawline()
            name = input("# ")
            # Check if name is something and is less than 8 characters and isn't already used
            if name == "":
                invalid_input_message("Please enter something")
            elif len(name) > 8:
                invalid_input_message("Name must be less than 8 characters")
            else:
                if any(item[1] == name for item in player_data):
                    invalid_input_message("That name is already in use")
                    correct_name = False
                if correct_name:
                    # Input lucky number
                    while True:
                        clear()
                        drawline()
                        print(name, "enter your lucky number")
                        print("Lucky number must be higher than 1 and less than", tiles_amount)
                        drawline()
                        user_input_fun = input("# ")
                        # Check if Lucky number is more that 1 and less than amount of tiles - 1
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


# Main game function
def game_run(players_data, current_player, current_player_amount, tiles_amount, double_trouble, well_loc,
             thorn_bush_loc):
    print(players_data)
    # Print curren player name and possible inputs
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

    # If user wants to quit the game
    if user_input_fun == "0":
        return True, current_player, current_player_amount
    # If user wants to roll the dice
    elif user_input_fun == "1":
        # Check if double trouble is turned so that 2 dices are rolled when turned on
        if double_trouble:
            game_over = roll_dice(players_data, current_player, tiles_amount, well_loc, thorn_bush_loc, True)
        else:
            game_over = roll_dice(players_data, current_player, tiles_amount, well_loc, thorn_bush_loc, False)
        print(game_over)

        # If last player in list has just rolled dice change current player to first in list
        if current_player > current_player_amount - 1:
            current_player = 0
        # If there is one player left and that player is stuck in a well
        if len(players_data) == 1:
            if players_data[current_player][3]:
                # Print game over
                clear()
                drawline()
                print("All players have been disqualified except", players_data[current_player][1])
                print("But", players_data[current_player][1], "is stuck in a well")
                print("Game Over")
                drawline()
                input("> ")
                return True, current_player, current_player_amount

        # If game over is True
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

        # Change current player to next player
        if current_player >= current_player_amount - 1:
            current_player = 0
        else:
            current_player += 1
    # If user gives up
    elif user_input_fun == "2":
        # Print message player has given up
        clear()
        drawline()
        print(players_data[current_player][1], "has given up")
        print(players_data[current_player][1], "is out of the game")
        drawline()
        input("> ")
        # Remove player that gave up from players_data list
        del players_data[current_player]
        current_player_amount -= 1
        if current_player > current_player_amount - 1:
            current_player -= 1

        # If there is 1 player left
        if len(players_data) == 1:
            # Print win message
            clear()
            drawline()
            print(players_data[current_player][1], "is the only one left")
            print(players_data[current_player][1], "HAS WON!")
            drawline()
            input("> ")
            return True, current_player, current_player_amount

        # If the last player gave up
        if not len(players_data):
            # Print game over message
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
