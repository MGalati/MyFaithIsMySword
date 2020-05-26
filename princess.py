#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import game_functions as gf


def princesse(active_player, current_dice, players_score, list_players, current_role):
    """If she take something, she can give the half to the Hero"""
    if int(current_dice[0]) == 5 and int(current_dice[1]) == 4 or \
    int(current_dice[0]) == 4 and int(current_dice[1]) == 5:
        if gf.check_role('Princesse', current_role) :
            current_princesse = gf.get_playerFromRole('Princesse', current_role)
            if gf.player_role(active_player, 'Princesse', current_role):
                print(active_player + ", tu es déjà la Princesse.")
            
            elif active_player != current_princesse:
                print(active_player + " prend le rôle de " + current_princesse 
                      + " en devenant le nouvel Princesse du village.")
                gf.switch_role(current_princesse, active_player, 'Princesse', current_role, list_players) 
       
        else :
            print(active_player + ' , tu deviens la Princesse.')
            gf.p_win_r(active_player, 'Princesse', current_role)  
