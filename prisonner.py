#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import game_functions as gf


def prisonnier(active_player, current_dice, players_score, list_players, current_role):
    """A villager enter the prison by rolling a 32"""
    
    if int(current_dice[0]) == 3 and int(current_dice[1]) == 2 or \
    int(current_dice[0]) == 2 and int(current_dice[1]) == 3:
        
        if gf.check_role('Prisoner', current_role):
            current_prisonner = gf.get_playerFromRole('Prisoner', current_role)
            if active_player != current_prisonner:
                print(current_prisonner + " est déjà en prison !!!")
        
        else:
            print(active_player + ", tu es le prisonnier du village.")
            gf.p_win_r(active_player, 'Prisoner', current_role)
            print("Prends " + str(current_dice[2]) 
                  + " pour fêter ton entrée en prison !")
            gf.player_recive(active_player, current_dice[2], list_players, current_role, players_score)
