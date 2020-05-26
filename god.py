#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import game_functions as gf


def god(active_player, current_dice, players_score, list_players, current_role):
    """Ascension : Become God by rolling double 4/5/6 then give the value"""
    list_roles = ['Hero', 'Catin', 'Ecuyer']  # Roles that God can't be
    role = 'God'
    
    if int(current_dice[0]) == 4 and int(current_dice[1]) == 4 or \
    int(current_dice[0]) == 5 and int(current_dice[1]) == 5:
        gf.give_to(current_dice[0], list_players, current_role, players_score)
        current_god = gf.get_playerFromRole(role, current_role)
        
        if gf.check_role(role, current_role) and current_god != active_player:
            print("Bataille de Dieux ! ")
            duel_result = gf.duel(active_player, current_god, list_players, current_role, players_score, turn = 2)
            winner = duel_result['winner']
            loser = duel_result['loser']
            
            if winner == current_god:
                print(loser + ' you lost !')
                
            else:
                new_god = duel_result['winner']
                lost_god = duel_result['loser']
                gf.switch_role(lost_god, new_god, role, current_role, list_players)
                gf.lose_roles(new_god, list_roles, current_role, list_players)
                print('Accueillez le nouveau Dieu : ' + new_god)
        
        if gf.player_role(active_player, 'God', current_role):
            print(active_player + ", tu es déjà Dieu.")
        
        else:
            print("Tu es le Dieu.")
            gf.p_win_r(active_player, role, current_role)
            gf.lose_roles(active_player, list_roles, current_role, list_players)
            
    elif int(current_dice[0]) == 6 and int(current_dice[1]) == 6:
        print(active_player + ', tu es le Dieu incontesté !')
        
        if gf.check_role(role, current_role):
            current_god = gf.get_playerFromRole(role, current_role)
            if current_god != active_player:
                lost_god = gf.get_playerFromRole(role, current_role)
                print(lost_god + " n'est plus Dieu ...")
                gf.switch_role(lost_god, active_player, role, current_role, list_players)
                gf.lose_roles(active_player, list_roles, current_role, list_players)
                gf.give_to(current_dice[0], list_players, current_role, players_score)
        
        if gf.player_role(active_player, 'God', current_role):
            print(active_player + ", tu es déjà Dieu.")
        
        else:
            gf.p_win_r(active_player, role, current_role)
