# -*- coding: utf-8 -*-
"""
Created on Sun May  3 11:44:21 2020

@author: Rowanas
"""

from random import choice
from Classes.places import Place
with open("./Modifiables/humanlocationnames.txt") as human_location_names:
    human_location_list = human_location_names.read().splitlines()