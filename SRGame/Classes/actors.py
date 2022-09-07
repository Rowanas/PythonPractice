# -*- coding: utf-8 -*-
"""
Created on Sat May  2 09:20:19 2020

@author: Rowanas
"""

# creates a new class, Person, which will be the blueprint for all people.
class Person:

    def __init__(self, person_forename, person_surname, person_location, person_title, person_race, person_kingdom):
        self.forename = person_forename
        self.surname = person_surname
        self.location = person_location
        self.title = person_title
        self.race = person_race
        self.kingdom = person_kingdom


class Human(Person):

    def __init__(self, person_forename, person_surname, person_location, person_title, person_race, person_kingdom):
        super().__init__(person_forename, person_surname, person_location, person_title, person_race, person_kingdom)
        self.forename = person_forename
        self.surname = person_surname
        self.location = person_location
        self.title = person_title
        self.race = person_race
        self.kingdom = person_kingdom