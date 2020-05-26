#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from random import randint
import game_functions as gf


def catin(active_player, current_dice, players_score,
          list_players, current_role):
    """A villager enter the prison by rolling a 32"""
    if int(current_dice[0]) == 4 and int(current_dice[1]) == 1 or \
    int(current_dice[0]) == 1 and int(current_dice[1]) == 4:
        current_catin = gf.get_playerFromRole('Catin', current_role)
        
        if gf.check_role('God', current_role) and \
            gf.player_role(active_player, 'God', current_role):
            print("Tu es le Dieu, tu ne peux être la Catin.")
        
        elif gf.check_role('Catin', current_role) :
            if gf.player_role(active_player, 'Catin', current_role):
                print(active_player + ', tu es déjà la Catin.')
       
            elif active_player != current_catin:
                print(active_player + " prend le rôle de " + current_catin
                      + " en devenant la nouvelle Catin du village.")
                gf.switch_role(current_catin, active_player, 'Catin',
                               current_role, list_players)
        
        else:
            print(active_player + " devient la Catin du village.")
            gf.p_win_r(active_player, 'Catin', current_role)


def protect(value_attack, current_god, protection, list_players,
            current_role, players_score):
    """The catin try to protect the village before the Hero"""
    current_catin = gf.get_playerFromRole("Catin", current_role)
    catin_roll = randint(1, 6) 
    print(current_catin + ", la Catin s'interpose et fait : "
          + str(catin_roll))
    
    if int(catin_roll) == 1:
        print("La Catin réussit à sauver le village !")
        print(current_god + ' ne donne rien au village et se prend ' 
              + str(value_attack))
        gf.player_recive(current_god, value_attack, list_players,
                         current_role, players_score)
        protection = True
        return protection

    else:
        print(current_catin + " prend la valeur de son dé : "
              + str(catin_roll))
        gf.player_recive(current_catin, int(catin_roll), list_players,
                         current_role, players_score)
        protection = False
        return protection
