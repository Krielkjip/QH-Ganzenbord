from draw_functions import *
import random


# Function that trows a player back if they landed on a thorn bush
def thorn_bush_logic(players_data, current_player):
    number = random.randint(5, 7)
    clear()
    drawline()
    print(players_data[current_player][1], "landed on the thorn bush")
    print(players_data[current_player][1], "got thrown back", number, "tiles")
    print(players_data[current_player][1], "moved from", players_data[current_player][0], "to",
          players_data[current_player][0] - number)
    drawline()
    input("> ")
    players_data[current_player][0] -= number


# Function that changes player state if they landed on the well
def well_logic(players_data, current_player):
    x = 0
    # Loop through all player
    for item in players_data:
        # If player is in well push the player out and lock the other player in the well
        if item[3]:
            clear()
            drawline()
            print(players_data[current_player][1], "landed in the well")
            print(players_data[x][1], "was already in the well")
            print(players_data[x][1], "got pushed out of the well by", players_data[current_player][1])
            print(players_data[current_player][1], "got stuck in the well")
            drawline()
            input("> ")
            players_data[x][3] = False
            players_data[current_player][3] = True
            players_data[current_player][0] += 1
            return
        x += 1

    # If no one was in the well lock player in the well
    clear()
    drawline()
    print(players_data[current_player][1], "landed in the well")
    print(players_data[current_player][1], "got stuck in the well")
    drawline()
    input("> ")
    players_data[current_player][3] = True
