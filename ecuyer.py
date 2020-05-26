#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import game_functions as gf


def ecuyer(active_player, current_dice, players_score,
           list_players, current_role):
    """If a Hero is in the game, you will follow him in his travel """
    
    if int(current_dice[0]) == 3 and int(current_dice[1]) == 1\
    or int(current_dice[0]) == 1 and int(current_dice[1]) == 3: 
        
        if gf.check_role('Hero', current_role):
            current_hero = gf.get_playerFromRole('Hero', current_role)
            current_god = gf.get_playerFromRole('God', current_role)
            
            if active_player != current_hero and active_player != current_god:
                if gf.check_role('Ecuyer', current_role):
                    current_ecuyer = gf.get_playerFromRole('Ecuyer',
                                                           current_role)
                    
                    if active_player != current_ecuyer:
                        gf.switch_role(current_ecuyer, active_player,
                                       'Ecuyer', current_role, list_players)
                        print(active_player + " remplace " + current_ecuyer
                              + " auprès de " + current_hero)
                    
                    else:
                        print(active_player + " est déjà l'Ecuyer de " 
                              + current_hero)
                    
                else:
                   gf.p_win_r(active_player, 'Ecuyer', current_role)
