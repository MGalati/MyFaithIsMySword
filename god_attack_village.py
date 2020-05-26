#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import game_functions as gf
import catin
import hero


def god_attack_village(current_dice, list_players, current_role, players_score):
    
    """When a total of 7 is draw, God give the smallest die to someone"""
    
    if int(current_dice[0]) + int(current_dice[1]) == 7:
        
        if gf.check_role('God', current_role):
            
            current_god = gf.get_playerFromRole('God', current_role)
            print(current_god + " en son nom de Dieu attaque le village !")
            value_attack = 0
            
            if current_dice[0] > current_dice[1]:
                value_attack = int(current_dice[1])
                
            elif int(current_dice[1]) > int(current_dice[0]):
                value_attack = int(current_dice[0])
            
            village = list_players[:]
            village.remove(current_god)
            print("Tout le village prend " + str(value_attack))
            protection = False
            
            if gf.check_role('Catin', current_role):
                print("A moins que ...")
                catin.protect(value_attack, current_god, protection,
                              list_players, current_role, players_score)
            
            if protection == False:
                
                if gf.check_role('Hero', current_role):
                    print("Mais ...")
                    hero.protect(value_attack, village, current_god,
                                 list_players, current_role, players_score)
