#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import game_functions as gf


def aubergiste(active_player, current_dice, players_score,
               list_players, current_role):
    """When someone take something, he can apply +1 ou +1"""
    
    if int(current_dice[0]) == 5 and int(current_dice[1]) == 3 or \
    int(current_dice[0]) == 3 and int(current_dice[1]) == 5:
        
        if gf.check_role('Aubergiste', current_role) :
            current_aubergiste = gf.get_playerFromRole('Aubergiste',
                                                       current_role)
            
            if gf.player_role(active_player, 'Aubergiste', current_role):
                print(active_player + ", tu es déjà l'Aubergiste'.")
            
            elif active_player != current_aubergiste:
                print(active_player + " prend le rôle de " + current_aubergiste 
                      + " en devenant le nouvel Aubergiste du village.")
                gf.switch_role(current_aubergiste, active_player,
                               'Aubergiste', current_role, list_players) 
       
        else :
            gf.p_win_r(active_player, 'Aubergiste', current_role)
