# -*- coding: utf-8 -*-

import json

import basic_events as be
import god as god
import oracle as ora
import hero as he
import ecuyer as ecu
import prisonner as priso
import catin as cat
import aubergiste as aub
import princess as princ
import dragon as drag
import god_attack_village as gav

def events(active_player, current_dice, players_score, list_players, current_role):
    be.basic_events(active_player, current_dice, players_score, list_players, current_role)
    god.god(active_player, current_dice, players_score, list_players, current_role)
    he.hero(active_player, current_dice, players_score, list_players, current_role)
    ora.oracle(active_player, current_dice, players_score, list_players, current_role)
    ecu.ecuyer(active_player, current_dice, players_score, list_players, current_role)
    priso.prisonnier(active_player, current_dice, players_score, list_players, current_role)
    cat.catin(active_player, current_dice, players_score, list_players, current_role)
    aub.aubergiste(active_player, current_dice, players_score, list_players, current_role)
    princ.princesse(active_player, current_dice, players_score, list_players, current_role)
    drag.dragon(active_player, current_dice, players_score, list_players, current_role)
    gav.god_attack_village(current_dice, list_players, current_role, players_score)
    
def save(name_file, directory , obj):
    '''Save to a jsonfile with specified name and directory'''
    with open(name_file + '.json', 'w') as f_obj:
        json.dump(obj, f_obj)