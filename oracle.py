#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import game_functions as gf


def oracle(active_player, current_dice, players_score,
           list_players, current_role):
    """Try to predict Hero's roll before his trial"""
    role = 'Oracle'
    
    if int(current_dice[0]) == 2 and int(current_dice[1]) == 1 or \
        int(current_dice[0]) == 1 and int(current_dice[1]) == 2:
        
        if gf.check_role(role, current_role):
            old_oracle = gf.get_playerFromRole(role, current_role)
            if old_oracle != active_player:            
                print(old_oracle + " n'est plus l'Oracle. ")
                gf.switch_role(old_oracle, active_player, role,
                           current_role, list_players)
                
            if gf.player_role(active_player, 'Oracle', current_role):
                print(active_player + ", tu es déjà l'Oracle.")
            
        else:
            gf.p_win_r(active_player, role, current_role)


def predict(current_role):
    oracle = gf.get_playerFromRole('Oracle', current_role)
    prediction = input(oracle + " prédit le lancer du Héros : ")
    return prediction
    

def change_h_die(hero_roll, current_role):
    oracle = gf.get_playerFromRole('Oracle', current_role)
    
    if hero_roll == 1:
        print(oracle + ", tu peux modifier le dé du Héros.")
        print("Pour faire + 1, écrit : + ")
        print("Si tu ne veux rien faire, appuie sur Entrée ")
        choice = input("Fais ton choix : ")
        
        if choice == '+':
            hero_roll += 1

        elif choice == '0':
            print("Entendu.")

    elif hero_roll == 6:
        print(oracle + ", tu peux modifier le résultat du Héros.")
        print("Pour faire - 1, écrit : - ")
        print("Si tu ne veux rien faire, appuie sur Entrée ")
        choice = input("Fais ton choix : ")
        
        if choice == '-':
            hero_roll -= 1

        elif choice == '0':
            print("Okay.")
    
    else:
        print(oracle + ", tu peux modifier le résultat du Heros.")
        print("Pour faire + 1, écrit : + ")
        print("Pour faire - 1, écrit : - ")
        print("Si tu ne veux rien faire, appuie sur Entrée ")
        choice = input("Fais ton choix : ")
        if choice == '+':
            hero_roll += 1
    
        elif choice == '-':
            hero_roll -= 1
    
        elif choice == '0':
            print("Bien.")

    print("Le dé affiche : " + str(hero_roll))
    return hero_roll


def check_prediction(prediction, hero_roll, list_players,
                     current_role, players_score):
    oracle = gf.get_playerFromRole('Oracle', current_role)
    
    if prediction == hero_roll:
        print("\n" + oracle + ", Bravo pour ta prédiction")
        gf.give_to(prediction, list_players, current_role, players_score)
