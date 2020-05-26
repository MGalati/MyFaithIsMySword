#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from random import randint
import game_functions as gf
import oracle


def hero(active_player, current_dice, players_score,
         list_players, current_role):
    """The Hero always try to protect the village from God's attack"""
    list_roles = ['Ecuyer', 'Princesse']  # Roles that Hero can't be
    
    if int(current_dice[0]) == 1 and int(current_dice[1]) == 1 or \
    int(current_dice[0]) == 2 and int(current_dice[1]) == 2 or \
    int(current_dice[0]) == 3 and int(current_dice[1]) == 3:
        
        if gf.check_role('God', current_role) and \
        gf.player_role(active_player, 'God', current_role):
            print("Tu es le Dieu et non le Héros !")
            target = input("Donne le role de Héros a : ")
            target = target.title()
            
            if gf.check_player(target, list_players):
                if gf.check_role('Hero', current_role):
                    current_hero = gf.get_playerFromRole('Hero', current_role)
                    gf.switch_role(current_hero, target, 'Hero',
                                   current_role, list_players)
                    gf.lose_roles(target, list_roles, current_role,
                                  list_players)
                    
                    if gf.check_role('Ecuyer', current_role):
                        current_ecuyer = gf.get_playerFromRole('Ecuyer',
                                                               current_role)
                        print(current_ecuyer + " l'ecuyer perd son rôle.")
                        gf.p_lose_r(current_ecuyer, 'Ecuyer', current_role,
                                    list_players)
                else:
                    gf.p_win_r(target, 'Hero', current_role)
        
        elif gf.check_role('Hero', current_role) :
            current_hero = gf.get_playerFromRole('Hero', current_role)
            
            if gf.player_role(active_player, 'Hero', current_role):
                print(active_player + ', tu es déjà le Hero.')
       
            elif active_player != current_hero:
                print(active_player + " prend le rôle de " + current_hero
                      + " en devenant le nouveau Hero du village.")
                gf.switch_role(current_hero, active_player, 'Hero',
                               current_role, list_players)
                if gf.check_role('Ecuyer', current_role):
                    current_ecuyer = gf.get_playerFromRole('Ecuyer',
                                                           current_role)
                    print(current_ecuyer + " l'ecuyer perd son rôle.")
                    gf.p_lose_r(current_ecuyer, 'Ecuyer', current_role,
                                    list_players)
        
        else :
            print("Tu es maintenant le Hero !")
            gf.p_win_r(active_player, 'Hero', current_role)
            gf.lose_roles(active_player, list_roles,
                          current_role, list_players)


def protect(value_attack, village, current_god, list_players,
            current_role, players_score):
    """The Hero roll a die in case of saving potentially the village"""
    if gf.check_role('Oracle', current_role):
        prediction = int(oracle.predict(current_role))
        
    current_hero = gf.get_playerFromRole("Hero", current_role)
    hero_roll = randint(1, 6)
    print(current_hero + " le Héros s'interpose et fait : " + str(hero_roll))
    
    if gf.check_role('Oracle', current_role):
        hero_roll = oracle.change_h_die(hero_roll, current_role)    
    
    if int(hero_roll) == 1:
        print("Le Héros est foudroyé !! Prends 6 et n'est plus Héros")
        gf.player_recive(current_hero, 6, list_players,
                         current_role, players_score)
        gf.p_lose_r(current_hero, 'Hero', current_role, list_players)
        
        if gf.check_role('Ecuyer', current_role):
            current_ecuyer = gf.get_playerFromRole('Ecuyer', current_role)
            print('Son fidèle écuyer ' + current_ecuyer 
                  + ' partage son sort ...')
            gf.p_lose_r(current_ecuyer, 'Ecuyer', current_role, list_players)
        
    elif int(hero_roll) == 2 or int(hero_roll) == 3:
        print("Tous les habitants du village prennent : " + str(value_attack))
        for villageois in village:
            gf.player_recive(villageois, value_attack, list_players,
                             current_role, players_score)
        
    elif int(hero_roll) == 4 or int(hero_roll) == 5:
        print("Le Héros devient la cible de Dieu et prend : "
              + str(value_attack))
        gf.player_recive(current_hero, value_attack, list_players,
                         current_role, players_score)
        
    elif int(hero_roll) == 6:
        print(current_god + " le Dieu ne distribue rien et prend : "
              + str(value_attack))
        gf.player_recive('Mat', value_attack, list_players,
                         current_role, players_score)
    
    if gf.check_role('Oracle', current_role):
        oracle.check_prediction(prediction, hero_roll, list_players,
                                current_role, players_score)
