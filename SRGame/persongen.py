# -*- coding: utf-8 -*-
"""
Created on Sun May  3 11:44:21 2020

@author: Rowanas
"""

from random import choice
from Classes.actors import Human
with open("./Modifiables/humanpeopleforenames.txt") as human_people_forenames:
    human_forenames_list = human_people_forenames.read().splitlines()
with open("./Modifiables/humanpeoplesurnames.txt") as human_people_surnames:
    human_surnames_list = human_people_surnames.read().splitlines()

human_list = []

def human_name_gen():
    sethumans = int(input("Please enter the number of unique human actors you would like in the game "))
    for i in (range(0,sethumans)):  # this obviously takes the player input as how many people we're going to generate
        human_list.append(Human(choice(human_forenames_list), choice(human_surnames_list), choice(human_location_list),"More nought","Yet more nought", "Britain"))
    for obj in human_list:
        print(obj.forename, obj.surname, obj.location, obj.kingdom) #prints each person out

human_name_gen()


