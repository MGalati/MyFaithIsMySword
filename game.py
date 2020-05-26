#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import features as ft
from die import Die


# Initialize 3 dice
die_1 = Die()
die_2 = Die()
die_red = Die()

# Initialize every essential object for the game
current_dice = [0, 0, 0]
current_role = {}
last_roll_player = {}
players_score = {}
list_players = ["Mat", "Mina", "Victor", "Pierre"]

# Allow the user to insert the number of player for the game
"""
n_players = int(input("Nombre de joueurs : ")) # Réfléchir except input en str"""

# Allow the user to write the name of players
"""
for person in range(n_players):
    name = input("Ecris ton nom : ")
    list_players.append(name)"""

# Initialize the first role of villager to everyone
for name in list_players:
    current_role[name] = ['Villageois']

# Initialize everyone score to 0
for name in list_players:
    players_score[name] = 0

# Initialize empty last roll for everyone    
for name in list_players:
    last_roll_player[name] = [0, 0, 0]

# Main loop for a lobby
game_active = True
while game_active:
    for active_player in list_players:
        print("It's " + active_player + " turn.")
        current_dice = [die_1.roll_die(), die_2.roll_die(),
                            die_red.roll_die()]
        last_roll_player[active_player] = [current_dice[0], current_dice[1],
                                  current_dice[2]]
        
        print(current_dice)
        
        ft.events(active_player, current_dice, players_score, list_players, current_role)

        print(' ')
        print('Fin du tour.')
        print(current_role)
        print(players_score)
        print('_____________________________________________________________')
        
    print("Nouveau tour ?")
    n_tour = input("Appuie Entree pour continuer.\nEcris n pour arreter la partie: ")
    print('_____________________________________________________________')
    if n_tour == "n":
        ft.save('score', 'save', players_score)
        print("Fin du jeu !")
        game_active = False
        
    else:
        continue
