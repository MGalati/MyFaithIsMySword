#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from random import randint


def check_player(player_name, list_players):
    """Check if the name is in the list of players"""
    if player_name in list_players:
        return True
    
    else:
        return False


def check_role(role, current_role):
    """Check if the role is in the dict. of current role"""
    presence = False
    
    for players, list_roles in current_role.items():
        for roles in list_roles:
            if roles == role:
                presence = True
                
    return presence


def check_empty_roles(current_role):
    """Look through the list of roles and if it's empty, fill it with the basic role"""
    for players, list_roles in current_role.items():
        if list_roles:
            continue
        
        else:
            list_roles.append('Villageois')

   
def get_playerFromRole(role, current_role):
    """Having the player behind the role"""
    for players, list_roles in current_role.items():
        for roles in list_roles:
            if role == roles:
                return players


def player_role(player, role, current_role):
    """Check if the player have the role"""
    presence = False
    
    for players, list_roles in current_role.items():
        if players == player:
            for roles in list_roles:
                if roles == role:
                    presence = True
    
    return presence


def ricochet(player_name, total, current_role, list_players, players_score):
    """Check if there is some ricochet according to somes roles dependencies"""
    if check_role('Princesse', current_role) and \
    check_role('Hero', current_role) and total >= 2:
        if player_role(player_name, 'Princesse', current_role):
            
            current_princesse = get_playerFromRole('Princesse', current_role)
            current_hero = get_playerFromRole('Hero', current_role)
            print(current_princesse 
                  + ' en son rôle de Princesse peut partager avec son Héros ' 
                  + current_hero) 
            gift = input("la somme de " + str(int(total)) 
                         + " ... 'o' pour partager : ")
            
            if gift == 'o':
                x = total / 2
                player_recive(current_hero, x, list_players, current_role, players_score)


    if check_role('Ecuyer', current_role):
        if player_role(player_name, 'Hero', current_role):
            
            current_ecuyer = get_playerFromRole('Ecuyer', current_role)
            current_hero = get_playerFromRole('Hero', current_role)
            players_score[current_ecuyer] += int(total)
            print(current_ecuyer + ' apporte son soutien à ' + current_hero
                  + ' son Héros et prend aussi : ' + str(int(total)))


    if check_role('Dragon', current_role) and total > 1:
        if player_role(player_name, 'Dragon', current_role):
            
            score = total
            print(player_name + ' le Dragon prend : ' + str(int(score)))
            decision = input('Ecris "o" pour répandre ton soufle autour de toi : ')
            
            if decision == 'o':
                index = list_players.index(player_name)
                dist = 1
                index_left = index - dist
                index_right = index + dist
                
                
                if index_left < 0:
                    index_left = len(list_players) - 1
                
                if index_right > len(list_players) - 1:
                    index_right = 0
                
                
                while score > 1:
                    score = int(score / 2)
                    left = list_players[index_left]
                    right = list_players[index_right]
                    
                    if left == right:
                        print (left + ' prend : ' + str(score) + ' et ' + str(score))
                        players_score[left] += int(2 * score)
                    else:
                        print(left + ' et ' + right + ' prennent : ' + str(score))
                        players_score[left] += int(score)
                        players_score[right] += int(score)
                    dist += 1
                    index_left -= 1
                    index_right += 1
                    if index_left < 0:
                        index_left = len(list_players) - 1
                    if index_right > len(list_players) - 1:
                        index_right = 0


def player_recive(player_name, total, list_players, current_role, players_score):
    """Add the total to a player in the players score dict."""
    if check_player(player_name, list_players):
        if check_role('Aubergiste', current_role):
            current_aubergiste = get_playerFromRole('Aubergiste', current_role)
            print(current_aubergiste + " en ton rôle d'Aubergiste")
            n_total = input("Tu peux faire + 1 ou - 1 ou rien : ")
            
            if n_total == '+':
                total += 1
            
            elif n_total == '-':
                total -= 1
            
            print("Le total est maintenant de " + str(int(total)))
        
        players_score[player_name] += int(total)
        ricochet(player_name, total, current_role, list_players, players_score)


def give_to(total, list_players, current_role, players_score):
    """Ask for an input's name to give the total to a player's score"""
    player_name = input("Distribue " + str(total) + " a : ")
    player_recive(player_name.title(), total, list_players,
                  current_role, players_score)


def duel(player_1, player_2, list_players, current_role, players_score, turn = 1):
    """Two players roll a die to find a winner"""
    die_1 = randint(1, 6)
    die_2 = randint(1, 6)
    print('Jet de ' + player_1 + ' : ' + str(die_1))
    print('Jet de ' + player_2 + ' : ' + str(die_2))
    
    if die_1 > die_2:
        winner = player_1
        loser = player_2
        duel_result = {'winner': winner, 'loser': loser}
        
        score = (die_1 - die_2) * turn
        player_recive(loser, score, list_players, current_role, players_score)
        return duel_result
    
    elif die_2 > die_1:
        winner = player_2
        loser = player_1
        duel_result = {'winner': winner, 'loser': loser}
        
        score = (die_2 - die_1) * turn
        player_recive(loser, score, list_players, current_role, players_score)
        return duel_result
    
    elif die_1 == die_2:
        turn += 1
        print('Le multiplicateur est de : ' + str(turn))
        return duel(player_1, player_2, list_players,
                    current_role, players_score, turn)


def p_lose_r(player, role, current_role, list_players):
    """The player lose the role from his pool"""
    if check_player(player, list_players) and check_role(role, current_role) \
    and player == get_playerFromRole(role, current_role):
        for players, list_roles in current_role.items():
            if players == player:
                try:
                    list_roles.remove(role)
                
                except:
                    print(role + " n'est pas un (des) role(s) de " + player)
                
    else:
        print(role + " n'est pas un (des) role(s) de " + player)
    


def p_win_r(player, role, current_role):
    """The player have now the role in his pool"""
    if player_role(player, role, current_role):
        print(player + " a déjà le rôle de " + role + ". Donc, le reste.")
    
    else:
        # print("Le joueur " + player + " devient " + role)
        for players, list_roles in current_role.items():
            if players == player:
                list_roles.append(role)
                
   
def switch_role(player_1, player_2, role, current_role, list_players):
    """The 2nd player win the role of the 1st player (btw he lost it)"""
    p_lose_r(player_1, role, current_role, list_players)
    p_win_r(player_2, role, current_role)
    check_empty_roles(current_role)
    

def everyone_take(total, players_score):
    """Everyone in the game take the total in their respective score"""
    for players in players_score:
        players_score[players] += total
        
        
def lose_roles(player, list_roles, current_role, list_players):
    """Check if the player have roles in the list and lose them"""
    for roles in list_roles:
        if player == get_playerFromRole(roles, current_role):
            p_lose_r(player, roles, current_role, list_players)
            print(player + ", tu perds ton rôle de " + roles)
    
    check_empty_roles(current_role)