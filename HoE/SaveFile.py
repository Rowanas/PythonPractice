import BioMaker
from os.path import exists

def save_file():
	    if character_subrace=="None":
            if exists(`character_name`.txt):
                f = open(r".txt", mode = "w")
		        f.write("""
Name: """+character_name+"""
Species: """+character_race+"""
Gender: """+character_gender+"""
Age: """+character_age+"""
Class: """+character_class+"""
Occupation: """+character_role+"""
Level: """+character_level+"""
XP: """+character_xp+"""

-------
Stats
-------
Strength: """+str(character_strength)+"""
Speed: """+str(character_speed)+"""
Stamina: """+str(character_stamina)+"""/"""+str(character_stamina)+"""
Agility: """+str(character_agility)+"""
Dexterity: """+str(character_dexterity)+"""
Constitution: """+str(character_constitution)+"""/"""+str(character_constitution)+"""
Perception: """+str(character_perception)+"""
Intelligence: """+str(character_intelligence)+"""
Mana: """+str(character_mana)+"""/"""+str(character_mana)+"""
Mana Power: """+str(character_manapower)+"""
Charisma: """+str(character_charisma)+"""
Stealth: """+str(character_stealth)+"""
Luck: """+str(character_luck)+"""
Armour Rating: """+str(character_armour)+"""
		
-------
Skills
-------
Species Skills:
	"""+str(character_skills)+"""
Occupation Skills:
	
Class Skills:
	"""+str(class_skills)+"""
Languages:
	
Racial Attacks:
	"""+str(race_attacks)+"""
Spells:
	"""+str(character_spells)+"""

-------
Equipment
-------
Armour: 	
Weaponry: 	

-------
Inventory
-------


-------
Quests
-------
Informal: 
Independant: 
Prompt: 
Guild: 
Companion: 
Personal: 

-------
Personality
-------
Personality Traits:
	Positive: 
	Negative: 

Beliefs:
	"""+str(race_worship)+"""
	"""+str(mage_worship)+"""
	"""+str(character_worship)+"""

Ideals: 

Personal Goal: 

Alignment: """+str(character_alignment)+"""

-------
Story
-------
Background:
	Hometown: 
	Starting Point: 

Family:


History:

""")
		f.close
	else:
		f = open(r"./characters.txt", mode = "w")
		f.write("""
Name: """+character_name+"""
Species: """+character_race+"""
Subspecies: """+character_subrace+"""
Gender: """+character_gender+"""
Age: """+character_age+"""
Class: """+character_class+"""
Occupation: """+character_role+"""
Level: """+character_level+"""
XP: """+str(character_xp)+"""

-------
Stats
-------
Strength: """+str(character_strength)+"""
Speed: """+str(character_speed)+"""
Stamina: """+str(character_stamina)+"""/"""+str(character_stamina)+"""
Agility: """+str(character_agility)+"""
Dexterity: """+str(character_dexterity)+"""
Constitution: """+str(character_constitution)+"""/"""+str(character_constitution)+"""
Perception: """+str(character_perception)+"""
Intelligence: """+str(character_intelligence)+"""
Mana: """+str(character_mana)+"""/"""+str(character_mana)+"""
Mana Power: """+str(character_manapower)+"""
Charisma: """+str(character_charisma)+"""
Stealth: """+str(character_stealth)+"""
Luck: """+str(character_luck)+"""
Armour Rating: """+str(character_armour)+"""

-------
Skills
-------
Species Skills:
	"""+str(character_skills)+"""
Occupation Skills:
	
Class Skills:
	"""+str(class_skills)+"""
Languages:
	
Racial Attacks:
	"""+str(race_attacks)+"""
Spells:
	"""+str(character_spells)+"""

-------
Equipment
-------
Armour: 	
Weaponry: 	

-------
Inventory
-------


-------
Quests
-------
Informal: 
Independant: 
Prompt: 
Guild: 
Companion: 
Personal: 

-------
Personality
-------
Personality Traits:
	Positive: 
	Negative: 

Beliefs:
	"""+str(race_worship)+"""
	"""+str(mage_worship)+"""
	"""+str(character_worship)+"""

Ideals: 

Personal Goal: 

Alignment: """+str(character_alignment)+"""

-------
Story
-------
Background:
	Hometown: 
	Starting Point: 

Family:


History:

""")
		f.close

save_file()