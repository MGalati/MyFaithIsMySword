#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import game_functions as gf


def dragon(active_player, current_dice, players_score,
           list_players, current_role):
    """When the dragon take, he can spread the total/2 in chain in left and right"""
    
    if int(current_dice[0]) == 5 and int(current_dice[1]) == 6 or \
    int(current_dice[0]) == 6 and int(current_dice[1]) == 5:
        if gf.check_role('Dragon', current_role) :
            current_dragon = gf.get_playerFromRole('Dragon', current_role)
            
            if gf.player_role(active_player, 'Dragon', current_role):
                print(active_player + ", tu es déjà le Dragon.")
            
            elif active_player != current_dragon:
                print(active_player + " prend le rôle de " + current_dragon 
                      + " en devenant le nouveau Dragon.")
                gf.switch_role(current_dragon, active_player, 'Dragon',
                               current_role, list_players) 
       
        else :
            gf.p_win_r(active_player, 'Dragon', current_role)
