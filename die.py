#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint

class Die():
    """Representation of a die"""
    
    def __init__(self, num_sides=6):
        """Initialize a basic 6 sides die"""
        self.num_sides = num_sides

    def roll_die(self):
        """Return a random value between 1 and num_sides"""
        return randint(1, self.num_sides)
    