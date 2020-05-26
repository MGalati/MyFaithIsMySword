#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import game_functions as gf


def basic_events(active_player, current_dice, players_score,
                 list_players, current_role):
    """Some few basic rules for non-role score"""


    # A 6 is rolled so the other die is given to someone
    if (int(current_dice[0]) == 6 and int(current_dice[1]) != 6):
        gf.give_to(current_dice[1], list_players, current_role, players_score)
        
    elif (int(current_dice[1]) == 6 and int(current_dice[0]) != 6):
        gf.give_to(current_dice[0], list_players, current_role, players_score)


    # 42 is rolled so everyone have the special die
    if int(current_dice[0]) == 4 and int(current_dice[1]) == 2:
        print("Tout le monde prend " + str(current_dice[2]) + " !")
        gf.everyone_take(int(current_dice[2]), players_score)

    elif int(current_dice[1]) == 4 and int(current_dice[0]) == 2:
        print("Tout le monde prend " + str(current_dice[2]) + " !")
        gf.everyone_take(int(current_dice[2]), players_score)


    # 51 is rolled so everyone have the special die
    if int(current_dice[0]) == 5 and int(current_dice[1]) == 1:
        print("Tout le monde prend " + str(current_dice[2]) + " !")
        gf.everyone_take(int(current_dice[2]), players_score)

    elif int(current_dice[1]) == 5 and int(current_dice[0]) == 1:
        print("Tout le monde prend " + str(current_dice[2]) + " !")
        gf.everyone_take(int(current_dice[2]), players_score)


    # When a 3 is rolled the prisoner take 1
    if (int(current_dice[0]) == 3 and int(current_dice[1]) != 2 \
    and int(current_dice[1]) != 3) or (int(current_dice[1]) == 3 \
    and int(current_dice[0]) != 2 and int(current_dice[0]) != 3):
        if gf.check_role('Prisoner', current_role):
            current_prisoner = gf.get_playerFromRole('Prisoner', current_role)
            if active_player != current_prisoner:
                print('Un 3 est sorti, le prisonnier ' + current_prisoner 
                      + ' prends 1.')
                gf.player_recive(current_prisoner, 1, list_players,
                                 current_role, players_score)
            
            else:
                print('Félicitation ! ' + active_player 
                      + ' Tu sors de prison. Et fête ça en prenant : '
                      + str(current_dice[2]))
                gf.p_lose_r(active_player, 'Prisoner', current_role,
                            list_players)
                gf.player_recive(current_prisoner, current_dice[2],
                                 list_players, current_role, players_score)
    
    elif (int(current_dice[0]) == 3 and int(current_dice[1]) == 2) or\
        (int(current_dice[1]) == 3 and int(current_dice[0]) == 2):
        if gf.check_role('Prisoner', current_role):
            current_prisoner = gf.get_playerFromRole('Prisoner', current_role)
            if active_player == current_prisoner:
                print('Félicitation avec le 3, '
                      + current_prisoner 
                      + ' sort de prison. Mais, prends '
                      + str(current_dice[2]) 
                      + " pour fêter qu'il y rerentre !")
                gf.player_recive(current_prisoner, current_dice[2],
                                 list_players, current_role, players_score)
            
            else:
                print('Un 3 est sorti, le prisonnier ' + current_prisoner 
                      + ' prends 1.')
                gf.player_recive(current_prisoner, 1, list_players,
                                 current_role, players_score)
    
    elif int(current_dice[0]) == 3 and int(current_dice[1]) == 3:
        if gf.check_role('Prisoner', current_role):
            current_prisoner = gf.get_playerFromRole('Prisoner', current_role)
            if active_player != current_prisoner:
                print('Deux 3 ! Le prisonnier ' + current_prisoner 
                      + ' prends 2.')
                gf.player_recive(current_prisoner, 2, list_players,
                                 current_role, players_score)
