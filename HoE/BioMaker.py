from os import system
from random import randint

gametitle="The Heralds of Eloria: Character Biography Creator"
system("mode 170,80")
system("title "+gametitle)

def cls():
	system('cls')

character_era = None
character_name = None
character_race = None
character_subrace = None
h_subrace = None
character_gender = None
character_age = None
character_class = None
character_role = None
character_level = None
character_xp = None
character_strength = None
character_speed = None
character_stamina = None
character_agility = None
character_dexterity = None
character_constitution = None
character_perception = None
character_intelligence = None
character_mana = None
character_manapower = None
character_manalevel = None
character_charisma = None
character_stealth = None
character_luck = None
character_armour = None
character_skills = None
class_skills = None
character_spells = None
magic_type = None
character_worship = None
race_worship = None
mage_worship = None
race_attacks = None
character_world = None
character_alignment = None

cls()
print("The Heralds of Eloria: Character Biography Creator")

def Intro():
	input("Press Enter to start...")

Intro()

def create_character():
	cls()
	global character_era
	while character_era is None:
		era_choice=input("""
		Let's begin!

		First, in which era does your character live? Make your choice by entering one of the numbers below: (Ask DM for clarification)
		1 - Dawn of the Heralds
		2 - Eastern Invasion
		3 - The Curse of Count Bellosi
		4 - The Hunted Sisters
		5 - The Renegades of Kasik
		6 - The Valley of Unrest
		7 - War of Rock and Bone
		8 - Troubled Water
		9 - Birth of the Umbralord
		10 - The Fall of Olic Highborn
		11 - Kove's Conquest
		12 - The Dark Tide
		13 - Mortal Gods
		14 - The Great Cataclysm
		15 - Relics in the Deep
		16 - Age of Rediscovery
		17 - The Great Awakening
		
		> """)
		if era_choice=="1":
			character_era="Dawn of the Heralds"
		elif era_choice=="2":
			character_era="Eastern Invasion"
		elif era_choice=="3":
			character_era="The Curse of Count Bellosi"
		elif era_choice=="4":
			character_era="The Hunted Sisters"
		elif era_choice=="5":
			character_era="The Renegades of Kasik"
		elif era_choice=="6":
			character_era="The Valley of Unrest"
		elif era_choice=="7":
			character_era="War of Rock and Bone"
		elif era_choice=="8":
			character_era="Troubled Water"
		elif era_choice=="9":
			character_era="Birth of the Umbralord"
		elif era_choice=="10":
			character_era="The Fall of Olic Highborn"
		elif era_choice=="11":
			character_era="Kove's Conquest"
		elif era_choice=="12":
			character_era="The Dark Tide"
		elif era_choice=="13":
			character_era="Mortal Gods"
		elif era_choice=="14":
			character_era="The Great Cataclysm"
		elif era_choice=="15":
			character_era="Relics in the Deep"
		elif era_choice=="16":
			character_era="Age of Rediscovery"
		elif era_choice=="17":
			character_era="The Great Awakening"
		else:
			print("Not a valid choice, please try again")
	
	cls()
	global character_world
	while character_world is None:
		if character_era=="Dawn of the Heralds":
			world_choice=input("""
			During the time of the first Heralds, there were fewer races in both the bright world of Eloria, and the storm-covered realm of Ta'bros. Which world does your character come from?
			1 - Eloria
			2 - Ta'bros
		
			> """)
			if world_choice=="1":
				character_world="Primal Eloria"
			elif world_choice=="2":
				character_world="Primal Ta'bros"
			else:
				print("Not a valid choice, try again")
		elif character_era=="Eastern Invasion":
			character_world="Eloria - 175,000 BDT"
		elif character_era=="The Curse of Count Bellosi":
			character_world="Ta'bros"
		elif character_era=="The Hunted Sisters":
			character_world="Eloria - 156,900 BDT"
		elif character_era=="The Renegades of Kasik":
			character_world="Eloria - 100,000 BDT"
		elif character_era=="The Valley of Unrest":
			character_world="Eloria - 100,000 BDT"
		elif character_era=="War of Rock and Bone":
			character_world="Eloria - 15,000 BDT"
		elif character_era=="Troubled Water":
			character_world="Eloria - 6,250 BDT"
		elif character_era=="Birth of the Umbralord":
			character_world="Eloria - 5,000 BDT"
		elif character_era=="The Fall of Olic Highborn":
			character_world="Eloria - 2,085 BDT"
		elif character_era=="Kove's Conquest":
			character_world="Ta'bros"
		elif character_era=="The Dark Tide":
			world_choice=input("""
			Durig the era of the Dark Tide, races from both the bright world of Eloria and the storm-covered realm of Ta'bros were drawn towards a war that would change the fates of both worlds. Which realm does your character come from?
			1 - Eloria
			2 - Ta'bros
			
			> """)
			if world_choice=="1":
				character_world="Eloria"
			elif world_choice=="2":
				character_world="Ta'bros"
			else:
				print("Not a valid choice, try again")
		elif character_era=="Mortal Gods":
			character_world="Unified"
		elif character_era=="The Great Cataclysm":
			character_world="Post-Unification"
		elif character_era=="Relics in the Deep":
			character_world="Restricted"
		elif character_era=="Age of Rediscovery":
			character_world="Restricted"
		elif character_era=="The Great Awakening":
			character_world="Restricted"

	cls()
	global character_race
	while character_race is None:
		if character_world=="Primal Eloria":
			race_choice=input("""
				Now comes the time to choose your character's race based on those available in Eloria during your chosen era.
					* = Not available as a player character

				1 - Bokabu - Mobile, Plant Being
				2 - Centaur - Daoine Sith/Horse Being
				3 - Daoine Sith - Fair-Skinned, Long-Eared Being
				4 - Dragon* - Giant, Six-Limbed Reptile
				5 - Dwarf - Short, Stocky Being
				6 - Faerie* - Miniature, Winged, Daoine Sith-Like Being
				7 - Garikon - Muscular, Four-Armed, Rock Being
				8 - Ibrigat - Squat, Bipedal Reptilian Being
				9 - Kitsune - Fox/Daoine Sith Shapeshifter
				10 - Merrow - Daoine Sith/Fish Being
				11 - Minotaur - Bull/Human Being
				12 - Quetzal* - Winged, Dragon/Daoine Sith Offspring
				13 - Satyr - Daoine Sith/Goat Being
				14 - Talis* - Elemental Being
				15 - Thrael - Daoine Sith/Newt Being

				> """)
			if race_choice=="1":
				character_race="Bokabu"
			elif race_choice=="2":
				character_race="Centaur"
			elif race_choice=="3":
				character_race="Daoine Sith"
			elif race_choice=="4":
				character_race="Dragon"
			elif race_choice=="5":
				character_race="Dwarf"
			elif race_choice=="6":
				character_race="Faerie"
			elif race_choice=="7":
				character_race="Garikon"
			elif race_choice=="8":
				character_race="Ibrigat"
			elif race_choice=="9":
				character_race="Kitsune"
			elif race_choice=="10":
				character_race="Merrow"
			elif race_choice=="11":
				character_race="Minotaur"
			elif race_choice=="12":
				character_race="Quetzal"
			elif race_choice=="13":
				character_race="Satyr"
			elif race_choice=="14":
				character_race="Talis"
			elif race_choice=="15":
				character_race="Thrael"
			else:
				print("Not a valid choice, try again")
		elif character_world=="Primal Ta'bros":
			race_choice=input("""
				Now comes the time to choose your character's race based on those available in Ta'bros during your chosen era.
					* = Not available as a player character
				
				1 - Cecaelia - Dökkálfar/Octopus Being
				2 - Delphyne - Dökkálfar/Snake Being
				3 - Dökkálfar - Dark-Skinned, Daoine Sith-Like Being
				4 - Greftaga - Mobile, Tree Being
				5 - Imp* - Dark, Faerie-Like Shapeshifter
				6 - Jorogumo - Dökkálfar/Spider Being
				7 - Khepri - Hive-Minded, Six-Limbed, Insectoid Being
				8 - Nagual - Dog/Dökkálfar Shapeshifter
				9 - Ogre - Dark, Troll-Like Being
				10 - Ponaturi - Amphibious, Goblin-Like Being
				11 - Redcap - Goblin-Like Being
				12 - Shurgan - Muscular, Armoured Lava Being
				13 - Strigoi* - Fanged, Pale-Skinned, Blood-Drinking, Light-Fearing Being
				14 - Varah - Boar/Dökkálfar Being
				15 - Waheela* - Giant Wolf with Ice Magic
			
				> """)
			if race_choice=="1":
				character_race="Cecaelia"
			elif race_choice=="2":
				character_race="Delphyne"
			elif race_choice=="3":
				character_race="Dökkálfar"
			elif race_choice=="4":
				character_race="Greftaga"
			elif race_choice=="5":
				character_race="Imp"
			elif race_choice=="6":
				character_race="Jorogumo"
			elif race_choice=="7":
				character_race="Khepri"
			elif race_choice=="8":
				character_race="Nagual"
			elif race_choice=="9":
				character_race="Ogre"
			elif race_choice=="10":
				character_race="Ponaturi"
			elif race_choice=="11":
				character_race="Redcap"
			elif race_choice=="12":
				character_race="Shurgan"
			elif race_choice=="13":
				character_race="Strigoi"
			elif race_choice=="14":
				character_race="Varah"
			elif race_choice=="15":
				character_race="Waheela"
			else:
				print("Not a valid choice, try again")
		elif character_world=="Eloria - 175,000 BDT":
			race_choice=input("""
				Now comes the time to choose your character's race based on those available in Eloria during your chosen era.
					* = Not available as a player character
				
				1 - Aamon - Owl-Headed, Winged Being
				2 - Ackirian - Grey-Skinned, Fanged, Human-Like Being
				3 - Bokabu - Mobile, Plant Being
				4 - Centaur - Daoine Sith/Horse Being
				5 - Daoine Sith - Fair-Skinned, Long-Eared Being
				6 - Dragon* - Giant, Six-Limbed Reptile
				7 - Dwarf - Short, Stocky Being
				8 - Faerie* - Miniature, Winged, Daoine Sith-Like Being
				9 - Garikon - Muscular, Four-Armed, Rock Being
				10 - Giant* - Exceptionally Large, Human-Like Being
				11 - Goblin - Short, Gruesome Being
				12 - Harpy - Human/Bird Being
				13 - Human - Human Being
				14 - Ibrigat - Squat, Bipedal Reptilian Being
				15 - Imp* - Dark, Faerie-Like Shapeshifter
				16 - Kitsune - Fox/Daoine Sith Shapeshifter
				17 - Merrow - Daoine Sith/Fish Being
				18 - Minotaur - Bull/Human Being
				19 - Quetzal* - Winged, Dragon/Daoine Sith Offspring
				20 - Satyr - Daoine Sith /Goat Being
				21 - Talis* - Elemental Being
				22 - Thrael - Daoine Sith/Newt Being
				23 - Troll - Huge, Goblin-Like Being
				24 - Wulver - Wolf/Human Being
			
				> """)
			if race_choice=="1":
				character_race="Aamon"
			elif race_choice=="2":
				character_race="Ackirian"
			elif race_choice=="3":
				character_race="Bokabu"
			elif race_choice=="4":
				character_race="Centaur"
			elif race_choice=="5":
				character_race="Daoine Sith"
			elif race_choice=="6":
				character_race="Dragon"
			elif race_choice=="7":
				character_race="Dwarf"
			elif race_choice=="8":
				character_race="Faerie"
			elif race_choice=="9":
				character_race="Garikon"
			elif race_choice=="10":
				character_race="Giant"
			elif race_choice=="11":
				character_race="Goblin"
			elif race_choice=="12":
				character_race="Harpy"
			elif race_choice=="13":
				character_race="Human"
			elif race_choice=="14":
				character_race="Ibrigat"
			elif race_choice=="15":
				character_race="Imp"
			elif race_choice=="16":
				character_race="Kitsune"
			elif race_choice=="17":
				character_race="Merrow"
			elif race_choice=="18":
				character_race="Minotaur"
			elif race_choice=="19":
				character_race="Quetzal"
			elif race_choice=="20":
				character_race="Satyr"
			elif race_choice=="21":
				character_race="Talis"
			elif race_choice=="22":
				character_race="Thrael"
			elif race_choice=="23":
				character_race="Troll"
			elif race_choice=="24":
				character_race="Wulver"
			else:
				print("Not a valid choice, try again")
		elif character_world=="Eloria - 156,900 BDT":
			race_choice=input("""
				Now comes the time to choose your character's race based on those available in Eloria during your chosen era.
					* = Not available as a player character
				
				1 - Aamon - Owl-Headed, Winged Being
				2 - Ackirian - Grey-Skinned, Fanged, Human-Like Being
				3 - Bokabu - Mobile, Plant Being
				4 - Centaur - Daoine Sith/Horse Being
				5 - Daoine Sith - Fair-Skinned, Long-Eared Being
				6 - Dragon* - Giant, Six-Limbed Reptile
				7 - Dwarf - Short, Stocky Being
				8 - Elfling - Daoine Sith/Human Offspring
				9 - Faerie* - Miniature, Winged, Daoine Sith-Like Being
				10 - Garikon - Muscular, Four-Armed, Rock Being
				11 - Giant* - Exceptionally Large, Human-Like Being
				12 - Goblin - Short, Gruesome Being
				13 - Harpy - Human/Bird Being
				14 - Human - Human Being
				15 - Ibrigat - Squat, Bipedal Reptilian Being
				16 - Imp* - Dark, Faerie-Like Shapeshifter
				17 - Kitsune - Fox/Daoine Sith Shapeshifter
				18 - Merrow - Daoine Sith/Fish Being
				19 - Minotaur - Bull/Human Being
				20 - Quetzal* - Winged, Dragon/Daoine Sith Offspring
				21 - Satyr - Daoine Sith /Goat Being
				22 - Talis* - Elemental Being
				23 - Thrael - Daoine Sith/Newt Being
				24 - Troll - Huge, Goblin-Like Being
				25 - Wulver - Wolf/Human Being
			
				> """)
			if race_choice=="1":
				character_race="Aamon"
			elif race_choice=="2":
				character_race="Ackirian"
			elif race_choice=="3":
				character_race="Bokabu"
			elif race_choice=="4":
				character_race="Centaur"
			elif race_choice=="5":
				character_race="Daoine Sith"
			elif race_choice=="6":
				character_race="Dragon"
			elif race_choice=="7":
				character_race="Dwarf"
			elif race_choice=="8":
				character_race="Elfling"
			elif race_choice=="9":
				character_race="Faerie"
			elif race_choice=="10":
				character_race="Garikon"
			elif race_choice=="11":
				character_race="Giant"
			elif race_choice=="12":
				character_race="Goblin"
			elif race_choice=="13":
				character_race="Harpy"
			elif race_choice=="14":
				character_race="Human"
			elif race_choice=="15":
				character_race="Ibrigat"
			elif race_choice=="16":
				character_race="Imp"
			elif race_choice=="17":
				character_race="Kitsune"
			elif race_choice=="18":
				character_race="Merrow"
			elif race_choice=="19":
				character_race="Minotaur"
			elif race_choice=="20":
				character_race="Quetzal"
			elif race_choice=="21":
				character_race="Satyr"
			elif race_choice=="22":
				character_race="Talis"
			elif race_choice=="23":
				character_race="Thrael"
			elif race_choice=="24":
				character_race="Troll"
			elif race_choice=="25":
				character_race="Wulver"
			else:
				print("Not a valid choice, try again")
		elif character_world=="Eloria - 100,000 BDT":
			race_choice=input("""
				Now comes the time to choose your character's race based on those available in Eloria during your chosen era.
					* = Not available as a player character
				
				1 - Aamon - Owl-Headed, Winged Being
				2 - Ackirian - Grey-Skinned, Fanged, Human-Like Being
				3 - Bokabu - Mobile, Plant Being
				4 - Centaur - Daoine Sith/Horse Being
				5 - Daoine Sith - Fair-Skinned, Long-Eared Being
				6 - Dragon* - Giant, Six-Limbed Reptile
				7 - Dwarf - Short, Stocky Being
				8 - Elfling - Daoine Sith/Human Offspring
				9 - Faerie* - Miniature, Winged, Daoine Sith-Like Being
				10 - Garikon - Muscular, Four-Armed, Rock Being
				11 - Giant* - Exceptionally Large, Human-Like Being
				12 - Goblin - Short, Gruesome Being
				13 - Golem* - Artificial Being
				14 - Harpy - Human/Bird Being
				15 - Human - Human Being
				16 - Ibrigat - Squat, Bipedal Reptilian Being
				17 - Imp* - Dark, Faerie-Like Shapeshifter
				18 - Kitsune - Fox/Daoine Sith Shapeshifter
				19 - Merrow - Daoine Sith/Fish Being
				20 - Minotaur - Bull/Human Being
				21 - Quetzal* - Winged, Dragon/Daoine Sith Offspring
				22 - Satyr - Daoine Sith /Goat Being
				23 - Talis* - Elemental Being
				24 - Thrael - Daoine Sith/Newt Being
				25 - Troll - Huge, Goblin-Like Being
				26 - Wulver - Wolf/Human Being
				27 - Yuki-Ona - Daoine Sith-Like Being with Ice Magic
			
				> """)
			if race_choice=="1":
				character_race="Aamon"
			elif race_choice=="2":
				character_race="Ackirian"
			elif race_choice=="3":
				character_race="Bokabu"
			elif race_choice=="4":
				character_race="Centaur"
			elif race_choice=="5":
				character_race="Daoine Sith"
			elif race_choice=="6":
				character_race="Dragon"
			elif race_choice=="7":
				character_race="Dwarf"
			elif race_choice=="8":
				character_race="Elfling"
			elif race_choice=="9":
				character_race="Faerie"
			elif race_choice=="10":
				character_race="Garikon"
			elif race_choice=="11":
				character_race="Giant"
			elif race_choice=="12":
				character_race="Goblin"
			elif race_choice=="13":
				character_race="Golem"
			elif race_choice=="14":
				character_race="Harpy"
			elif race_choice=="15":
				character_race="Human"
			elif race_choice=="16":
				character_race="Ibrigat"
			elif race_choice=="17":
				character_race="Imp"
			elif race_choice=="18":
				character_race="Kitsune"
			elif race_choice=="19":
				character_race="Merrow"
			elif race_choice=="20":
				character_race="Minotaur"
			elif race_choice=="21":
				character_race="Quetzal"
			elif race_choice=="22":
				character_race="Satyr"
			elif race_choice=="23":
				character_race="Talis"
			elif race_choice=="24":
				character_race="Thrael"
			elif race_choice=="25":
				character_race="Troll"
			elif race_choice=="26":
				character_race="Wulver"
			elif race_choice=="27":
				character_race="Yuki-Ona"
			else:
				print("Not a valid choice, try again")
		elif character_world=="Eloria - 15,000 BDT":
			race_choice=input("""
				Now comes the time to choose your character's race based on those available in Eloria during your chosen era.
					* = Not available as a player character
				
				1 - Aamon - Owl-Headed, Winged Being
				2 - Ackirian - Grey-Skinned, Fanged, Human-Like Being
				3 - Bokabu - Mobile, Plant Being
				4 - Centaur - Daoine Sith/Horse Being
				5 - Daoine Sith - Fair-Skinned, Long-Eared Being
				6 - Dragon* - Giant, Six-Limbed Reptile
				7 - Dwarf - Short, Stocky Being
				8 - Elfling - Daoine Sith/Human Offspring
				9 - Faerie* - Miniature, Winged, Daoine Sith-Like Being
				10 - Garikon - Muscular, Four-Armed, Rock Being
				11 - Giant* - Exceptionally Large, Human-Like Being
				12 - Goblin - Short, Gruesome Being
				13 - Golem* - Artificial Being
				14 - Harpy - Human/Bird Being
				15 - Human - Human Being
				16 - Ibrigat - Squat, Bipedal Reptilian Being
				17 - Imp* - Dark, Faerie-Like Shapeshifter
				18 - Kitsune - Fox/Daoine Sith Shapeshifter
				19 - Merrow - Daoine Sith/Fish Being
				20 - Minotaur - Bull/Human Being
				21 - Quetzal* - Winged, Dragon/Daoine Sith Offspring
				22 - Satyr - Daoine Sith /Goat Being
				23 - Talis* - Elemental Being
				24 - Thrael - Daoine Sith/Newt Being
				25 - Troll - Huge, Goblin-Like Being
				26 - Wulver - Wolf/Human Being
				27 - Yuki-Ona - Daoine Sith-Like Being with Ice Magic
			
				> """)
			if race_choice=="1":
				character_race="Aamon"
			elif race_choice=="2":
				character_race="Ackirian"
			elif race_choice=="3":
				character_race="Bokabu"
			elif race_choice=="4":
				character_race="Centaur"
			elif race_choice=="5":
				character_race="Daoine Sith"
			elif race_choice=="6":
				character_race="Dragon"
			elif race_choice=="7":
				character_race="Dwarf"
			elif race_choice=="8":
				character_race="Elfling"
			elif race_choice=="9":
				character_race="Faerie"
			elif race_choice=="10":
				character_race="Garikon"
			elif race_choice=="11":
				character_race="Giant"
			elif race_choice=="12":
				character_race="Goblin"
			elif race_choice=="13":
				character_race="Golem"
			elif race_choice=="14":
				character_race="Harpy"
			elif race_choice=="15":
				character_race="Human"
			elif race_choice=="16":
				character_race="Ibrigat"
			elif race_choice=="17":
				character_race="Imp"
			elif race_choice=="18":
				character_race="Kitsune"
			elif race_choice=="19":
				character_race="Merrow"
			elif race_choice=="20":
				character_race="Minotaur"
			elif race_choice=="21":
				character_race="Quetzal"
			elif race_choice=="22":
				character_race="Satyr"
			elif race_choice=="23":
				character_race="Talis"
			elif race_choice=="24":
				character_race="Thrael"
			elif race_choice=="25":
				character_race="Troll"
			elif race_choice=="26":
				character_race="Wulver"
			elif race_choice=="27":
				character_race="Yuki-Ona"
			else:
				print("Not a valid choice, try again")
		elif character_world=="Eloria - 6,250 BDT":
			race_choice=input("""
				Now comes the time to choose your character's race based on those available in Eloria during your chosen era.
					* = Not available as a player character
				
				1 - Aamon - Owl-Headed, Winged Being
				2 - Ackirian - Grey-Skinned, Fanged, Human-Like Being
				3 - Bokabu - Mobile, Plant Being
				4 - Centaur - Daoine Sith/Horse Being
				5 - Daoine Sith - Fair-Skinned, Long-Eared Being
				6 - Dragon* - Giant, Six-Limbed Reptile
				7 - Dwarf - Short, Stocky Being
				8 - Elfling - Daoine Sith/Human Offspring
				9 - Faerie* - Miniature, Winged, Daoine Sith-Like Being
				10 - Garikon - Muscular, Four-Armed, Rock Being
				11 - Giant* - Exceptionally Large, Human-Like Being
				12 - Goblin - Short, Gruesome Being
				13 - Golem* - Artificial Being
				14 - Harpy - Human/Bird Being
				15 - Human - Human Being
				16 - Ibrigat - Squat, Bipedal Reptilian Being
				17 - Imp* - Dark, Faerie-Like Shapeshifter
				18 - Kitsune - Fox/Daoine Sith Shapeshifter
				19 - Merrow - Daoine Sith/Fish Being
				20 - Minotaur - Bull/Human Being
				21 - Quetzal* - Winged, Dragon/Daoine Sith Offspring
				22 - Satyr - Daoine Sith /Goat Being
				23 - Talis* - Elemental Being
				24 - Thrael - Daoine Sith/Newt Being
				25 - Troll - Huge, Goblin-Like Being
				26 - Wulver - Wolf/Human Being
				27 - Yuki-Ona - Daoine Sith-Like Being with Ice Magic
			
				> """)
			if race_choice=="1":
				character_race="Aamon"
			elif race_choice=="2":
				character_race="Ackirian"
			elif race_choice=="3":
				character_race="Bokabu"
			elif race_choice=="4":
				character_race="Centaur"
			elif race_choice=="5":
				character_race="Daoine Sith"
			elif race_choice=="6":
				character_race="Dragon"
			elif race_choice=="7":
				character_race="Dwarf"
			elif race_choice=="8":
				character_race="Elfling"
			elif race_choice=="9":
				character_race="Faerie"
			elif race_choice=="10":
				character_race="Garikon"
			elif race_choice=="11":
				character_race="Giant"
			elif race_choice=="12":
				character_race="Goblin"
			elif race_choice=="13":
				character_race="Golem"
			elif race_choice=="14":
				character_race="Harpy"
			elif race_choice=="15":
				character_race="Human"
			elif race_choice=="16":
				character_race="Ibrigat"
			elif race_choice=="17":
				character_race="Imp"
			elif race_choice=="18":
				character_race="Kitsune"
			elif race_choice=="19":
				character_race="Merrow"
			elif race_choice=="20":
				character_race="Minotaur"
			elif race_choice=="21":
				character_race="Quetzal"
			elif race_choice=="22":
				character_race="Satyr"
			elif race_choice=="23":
				character_race="Talis"
			elif race_choice=="24":
				character_race="Thrael"
			elif race_choice=="25":
				character_race="Troll"
			elif race_choice=="26":
				character_race="Wulver"
			elif race_choice=="27":
				character_race="Yuki-Ona"
			else:
				print("Not a valid choice, try again")
		elif character_world=="Eloria - 5,000 BDT":
			race_choice=input("""
				Now comes the time to choose your character's race based on those available in Eloria during your chosen era.
					* = Not available as a player character
				
				1 - Aamon - Owl-Headed, Winged Being
				2 - Ackirian - Grey-Skinned, Fanged, Human-Like Being
				3 - Bokabu - Mobile, Plant Being
				4 - Centaur - Daoine Sith/Horse Being
				5 - Daoine Sith - Fair-Skinned, Long-Eared Being
				6 - Dragon* - Giant, Six-Limbed Reptile
				7 - Dwarf - Short, Stocky Being
				8 - Elfling - Daoine Sith/Human Offspring
				9 - Faerie* - Miniature, Winged, Daoine Sith-Like Being
				10 - Garikon - Muscular, Four-Armed, Rock Being
				11 - Giant* - Exceptionally Large, Human-Like Being
				12 - Goblin - Short, Gruesome Being
				13 - Golem* - Artificial Being
				14 - Harpy - Human/Bird Being
				15 - Human - Human Being
				16 - Ibrigat - Squat, Bipedal Reptilian Being
				17 - Imp* - Dark, Faerie-Like Shapeshifter
				18 - Kitsune - Fox/Daoine Sith Shapeshifter
				19 - Merrow - Daoine Sith/Fish Being
				20 - Minotaur - Bull/Human Being
				21 - Quetzal* - Winged, Dragon/Daoine Sith Offspring
				22 - Satyr - Daoine Sith /Goat Being
				23 - Talis* - Elemental Being
				24 - Thrael - Daoine Sith/Newt Being
				25 - Troll - Huge, Goblin-Like Being
				26 - Wulver - Wolf/Human Being
				27 - Yuki-Ona - Daoine Sith-Like Being with Ice Magic
			
				> """)
			if race_choice=="1":
				character_race="Aamon"
			elif race_choice=="2":
				character_race="Ackirian"
			elif race_choice=="3":
				character_race="Bokabu"
			elif race_choice=="4":
				character_race="Centaur"
			elif race_choice=="5":
				character_race="Daoine Sith"
			elif race_choice=="6":
				character_race="Dragon"
			elif race_choice=="7":
				character_race="Dwarf"
			elif race_choice=="8":
				character_race="Elfling"
			elif race_choice=="9":
				character_race="Faerie"
			elif race_choice=="10":
				character_race="Garikon"
			elif race_choice=="11":
				character_race="Giant"
			elif race_choice=="12":
				character_race="Goblin"
			elif race_choice=="13":
				character_race="Golem"
			elif race_choice=="14":
				character_race="Harpy"
			elif race_choice=="15":
				character_race="Human"
			elif race_choice=="16":
				character_race="Ibrigat"
			elif race_choice=="17":
				character_race="Imp"
			elif race_choice=="18":
				character_race="Kitsune"
			elif race_choice=="19":
				character_race="Merrow"
			elif race_choice=="20":
				character_race="Minotaur"
			elif race_choice=="21":
				character_race="Quetzal"
			elif race_choice=="22":
				character_race="Satyr"
			elif race_choice=="23":
				character_race="Talis"
			elif race_choice=="24":
				character_race="Thrael"
			elif race_choice=="25":
				character_race="Troll"
			elif race_choice=="26":
				character_race="Wulver"
			elif race_choice=="27":
				character_race="Yuki-Ona"
			else:
				print("Not a valid choice, try again")
		elif character_world=="Eloria - 2,085 BDT":
			race_choice=input("""
				Now comes the time to choose your character's race based on those available in Eloria during your chosen era.
					* = Not available as a player character
				
				1 - Aamon - Owl-Headed, Winged Being
				2 - Ackirian - Grey-Skinned, Fanged, Human-Like Being
				3 - Bokabu - Mobile, Plant Being
				4 - Centaur - Daoine Sith/Horse Being
				5 - Daoine Sith - Fair-Skinned, Long-Eared Being
				6 - Dragon* - Giant, Six-Limbed Reptile
				7 - Dwarf - Short, Stocky Being
				8 - Elfling - Daoine Sith/Human Offspring
				9 - Faerie* - Miniature, Winged, Daoine Sith-Like Being
				10 - Garikon - Muscular, Four-Armed, Rock Being
				11 - Giant* - Exceptionally Large, Human-Like Being
				12 - Goblin - Short, Gruesome Being
				13 - Golem* - Artificial Being
				14 - Harpy - Human/Bird Being
				15 - Human - Human Being
				16 - Ibrigat - Squat, Bipedal Reptilian Being
				17 - Imp* - Dark, Faerie-Like Shapeshifter
				18 - Kitsune - Fox/Daoine Sith Shapeshifter
				19 - Merrow - Daoine Sith/Fish Being
				20 - Minotaur - Bull/Human Being
				21 - Quetzal* - Winged, Dragon/Daoine Sith Offspring
				22 - Satyr - Daoine Sith /Goat Being
				23 - Talis* - Elemental Being
				24 - Thrael - Daoine Sith/Newt Being
				25 - Troll - Huge, Goblin-Like Being
				26 - Wulver - Wolf/Human Being
				27 - Yuki-Ona - Daoine Sith-Like Being with Ice Magic
			
				> """)
			if race_choice=="1":
				character_race="Aamon"
			elif race_choice=="2":
				character_race="Ackirian"
			elif race_choice=="3":
				character_race="Bokabu"
			elif race_choice=="4":
				character_race="Centaur"
			elif race_choice=="5":
				character_race="Daoine Sith"
			elif race_choice=="6":
				character_race="Dragon"
			elif race_choice=="7":
				character_race="Dwarf"
			elif race_choice=="8":
				character_race="Elfling"
			elif race_choice=="9":
				character_race="Faerie"
			elif race_choice=="10":
				character_race="Garikon"
			elif race_choice=="11":
				character_race="Giant"
			elif race_choice=="12":
				character_race="Goblin"
			elif race_choice=="13":
				character_race="Golem"
			elif race_choice=="14":
				character_race="Harpy"
			elif race_choice=="15":
				character_race="Human"
			elif race_choice=="16":
				character_race="Ibrigat"
			elif race_choice=="17":
				character_race="Imp"
			elif race_choice=="18":
				character_race="Kitsune"
			elif race_choice=="19":
				character_race="Merrow"
			elif race_choice=="20":
				character_race="Minotaur"
			elif race_choice=="21":
				character_race="Quetzal"
			elif race_choice=="22":
				character_race="Satyr"
			elif race_choice=="23":
				character_race="Talis"
			elif race_choice=="24":
				character_race="Thrael"
			elif race_choice=="25":
				character_race="Troll"
			elif race_choice=="26":
				character_race="Wulver"
			elif race_choice=="27":
				character_race="Yuki-Ona"
			else:
				print("Not a valid choice, try again")
		elif character_world=="Eloria":
			race_choice=input("""
				Now comes the time to choose your character's race based on those available in Eloria during your chosen era.
					* = Not available as a player character
				
				1 - Aamon - Owl-Headed, Winged Being
				2 - Ackirian - Grey-Skinned, Fanged, Human-Like Being
				3 - Bokabu - Mobile, Plant Being
				4 - Centaur - Daoine Sith/Horse Being
				5 - Daoine Sith - Fair-Skinned, Long-Eared Being
				6 - Dragon* - Giant, Six-Limbed Reptile
				7 - Dwarf - Short, Stocky Being
				8 - Elfling - Daoine Sith/Human Offspring
				9 - Faerie* - Miniature, Winged, Daoine Sith-Like Being
				10 - Garikon - Muscular, Four-Armed, Rock Being
				11 - Giant* - Exceptionally Large, Human-Like Being
				12 - Goblin - Short, Gruesome Being
				13 - Golem* - Artificial Being
				14 - Harpy - Human/Bird Being
				15 - Human - Human Being
				16 - Ibrigat - Squat, Bipedal Reptilian Being
				17 - Imp* - Dark, Faerie-Like Shapeshifter
				18 - Kitsune - Fox/Daoine Sith Shapeshifter
				19 - Merrow - Daoine Sith/Fish Being
				20 - Minotaur - Bull/Human Being
				21 - Quetzal* - Winged, Dragon/Daoine Sith Offspring
				22 - Satyr - Daoine Sith /Goat Being
				23 - Talis* - Elemental Being
				24 - Thrael - Daoine Sith/Newt Being
				25 - Troll - Huge, Goblin-Like Being
				26 - Wulver - Wolf/Human Being
				27 - Yuki-Ona - Daoine Sith-Like Being with Ice Magic
			
				> """)
			if race_choice=="1":
				character_race="Aamon"
			elif race_choice=="2":
				character_race="Ackirian"
			elif race_choice=="3":
				character_race="Bokabu"
			elif race_choice=="4":
				character_race="Centaur"
			elif race_choice=="5":
				character_race="Daoine Sith"
			elif race_choice=="6":
				character_race="Dragon"
			elif race_choice=="7":
				character_race="Dwarf"
			elif race_choice=="8":
				character_race="Elfling"
			elif race_choice=="9":
				character_race="Faerie"
			elif race_choice=="10":
				character_race="Garikon"
			elif race_choice=="11":
				character_race="Giant"
			elif race_choice=="12":
				character_race="Goblin"
			elif race_choice=="13":
				character_race="Golem"
			elif race_choice=="14":
				character_race="Harpy"
			elif race_choice=="15":
				character_race="Human"
			elif race_choice=="16":
				character_race="Ibrigat"
			elif race_choice=="17":
				character_race="Imp"
			elif race_choice=="18":
				character_race="Kitsune"
			elif race_choice=="19":
				character_race="Merrow"
			elif race_choice=="20":
				character_race="Minotaur"
			elif race_choice=="21":
				character_race="Quetzal"
			elif race_choice=="22":
				character_race="Satyr"
			elif race_choice=="23":
				character_race="Talis"
			elif race_choice=="24":
				character_race="Thrael"
			elif race_choice=="25":
				character_race="Troll"
			elif race_choice=="26":
				character_race="Wulver"
			elif race_choice=="27":
				character_race="Yuki-Ona"
			else:
				print("Not a valid choice, try again")
		elif character_world=="Ta'bros":
			race_choice=input("""
				Now comes the time to choose your character's race based on those available in Ta'bros during your chosen era.
					* = Not available as a player character
				
				1 - Adlet - Dog/Dökkálfar Being
				2 - Cecaelia - Dökkálfar/Octopus Being
				3 - Delphyne - Dökkálfar/Snake Being
				4 - Dökkálfar - Dark-Skinned, Daoine Sith-Like Being
				5 - Garuda - Eagle-Headed, Winged Being
				6 - Giant* - Exceptionally Large, Human-Like Being
				7 - Greftaga - Mobile, Tree Being
				8 - Human - Human Being
				9 - Imp* - Dark, Faerie-Like Shapeshifter
				10 - Jorogumo - Dökkálfar/Spider Being
				11 - Khepri - Hive-Minded, Six-Limbed, Insectoid Being
				12 - Nagual - Dog/Dökkálfar Shapeshifter
				13 - Ogre - Dark, Troll-Like Being
				14 - Ponaturi - Amphibious, Goblin-Like Being
				15 - Redcap - Goblin-Like Being
				16 - Shurgan - Muscular, Armoured Lava Being
				17 - Siren - Dark, Harpy-Like Being
				18 - Strigoi* - Fanged, Pale-Skinned, Blood-Drinking, Light-Fearing Being
				19 - Varah - Boar/Dökkálfar Being
				20 - Waheela* - Giant Wolf with Ice Magic
			
				> """)
			if race_choice=="1":
				character_race="Adlet"
			elif race_choice=="2":
				character_race="Cecaelia"
			elif race_choice=="3":
				character_race="Delphyne"
			elif race_choice=="4":
				character_race="Dökkálfar"
			elif race_choice=="5":
				character_race="Garuda"
			elif race_choice=="6":
				character_race="Giant"
			elif race_choice=="7":
				character_race="Greftaga"
			elif race_choice=="8":
				character_race="Human"
			elif race_choice=="9":
				character_race="Imp"
			elif race_choice=="10":
				character_race="Jorogumo"
			elif race_choice=="11":
				character_race="Khepri"
			elif race_choice=="12":
				character_race="Nagual"
			elif race_choice=="13":
				character_race="Ogre"
			elif race_choice=="14":
				character_race="Ponaturi"
			elif race_choice=="15":
				character_race="Redcap"
			elif race_choice=="16":
				character_race="Shurgan"
			elif race_choice=="17":
				character_race="Siren"
			elif race_choice=="18":
				character_race="Strigoi"
			elif race_choice=="19":
				character_race="Varah"
			elif race_choice=="20":
				character_race="Waheela"
			else:
				print("Not a valid choice, try again")
		elif character_world=="Unified":
			race_choice=input("""
				Now comes the time to choose your character's race based on those available during your chosen era.
					* = Not available as a player character
				
				1 - Aamon - Owl-Headed, Winged Being
				2 - Ackirian - Grey-Skinned, Fanged, Human-Like Being
				3 - Adlet - Dog/Dökkálfar Being
				4 - Bokabu - Mobile, Plant Being
				5 - Cecaelia - Dökkálfar/Octopus Being
				6 - Centaur - Daoine Sith/Horse Being
				7 - Daoine Sith - Fair-Skinned, Long-Eared Being
				8 - Delphyne - Dökkálfar/Snake Being
				9 - Dökkálfar - Dark-Skinned, Daoine Sith-Like Being
				10 - Dragon* - Giant, Six-Limbed Reptile
				11 - Dwarf - Short, Stocky Being
				12 - Elfling - Daoine Sith/Human Offspring
				13 - Faerie* - Miniature, Winged, Daoine Sith-Like Being
				14 - Garikon - Muscular, Four-Armed, Rock Being
				15 - Garuda - Eagle-Headed, Winged Being
				16 - Giant* - Exceptionally Large, Human-Like Being
				17 - Goblin - Short, Gruesome Being
				18 - Golem* - Artificial Being
				19 - Greftaga - Mobile, Tree Being
				20 - Harpy - Human/Bird Being
				21 - Human - Human Being
				22 - Ibrigat - Squat, Bipedal Reptilian Being
				23 - Imp* - Dark, Faerie-Like Shapeshifter
				24 - Jorogumo - Dökkálfar/Spider Being
				25 - Khepri - Hive-Minded, Six-Limbed, Insectoid Being
				26 - Kitsune - Fox/Daoine Sith Shapeshifter
				27 - Merrow - Daoine Sith/Fish Being
				28 - Minotaur - Bull/Human Being
				29 - Nagual - Dog/Dökkálfar Shapeshifter
				30 - Ogre - Dark, Troll-Like Being
				31 - Ponaturi - Amphibious, Goblin-Like Being
				32 - Quetzal* - Winged, Dragon/Daoine Sith Offspring
				33 - Redcap - Goblin-Like Being
				34 - Rionnath - Human-Like Beings with Flower-Based Characteristics
				35 - Satyr - Daoine Sith/Goat Being
				36 - Shurgan - Muscular, Armoured Lava Being
				37 - Siren - Dark, Harpy-Like Being
				38 - Strigoi* - Fanged, Pale-Skinned, Blood-Drinking, Light-Fearing Being
				39 - Talis* - Elemental Being
				40 - Thrael - Daoine Sith/Newt Being
				41 - Troll - Huge, Goblin-Like Being
				42 - Varah - Boar/Dökkálfar Being
				43 - Vinori* - Muscular, Bestial, Human-Like Being
				44 - Waheela* - Giant Wolf with Ice Magic
				45 - Wulver - Wolf/Human Being
				46 - Yuki-Ona - Daoine Sith-Like Being with Ice Magic

				> """)
			if race_choice=="1":
				character_race="Aamon"
			elif race_choice=="2":
				character_race="Ackirian"
			elif race_choice=="3":
				character_race="Adlet"
			elif race_choice=="4":
				character_race="Bokabu"
			elif race_choice=="5":
				character_race="Cecaelia"
			elif race_choice=="6":
				character_race="Centaur"
			elif race_choice=="7":
				character_race="Daoine Sith"
			elif race_choice=="8":
				character_race="Delphyne"
			elif race_choice=="9":
				character_race="Dökkálfar"
			elif race_choice=="10":
				character_race="Dragon"
			elif race_choice=="11":
				character_race="Dwarf"
			elif race_choice=="12":
				character_race="Elfling"
			elif race_choice=="13":
				character_race="Faerie"
			elif race_choice=="14":
				character_race="Garikon"
			elif race_choice=="15":
				character_race="Garuda"
			elif race_choice=="16":
				character_race="Giant"
			elif race_choice=="17":
				character_race="Goblin"
			elif race_choice=="18":
				character_race="Golem"
			elif race_choice=="19":
				character_race="Greftaga"
			elif race_choice=="20":
				character_race="Harpy"
			elif race_choice=="21":
				character_race="Human"
			elif race_choice=="22":
				character_race="Ibrigat"
			elif race_choice=="23":
				character_race="Imp"
			elif race_choice=="24":
				character_race="Jorogumo"
			elif race_choice=="25":
				character_race="Khepri"
			elif race_choice=="26":
				character_race="Kitsune"
			elif race_choice=="27":
				character_race="Merrow"
			elif race_choice=="28":
				character_race="Minotaur"
			elif race_choice=="29":
				character_race="Nagual"
			elif race_choice=="30":
				character_race="Ogre"
			elif race_choice=="31":
				character_race="Ponaturi"
			elif race_choice=="32":
				character_race="Quetzal"
			elif race_choice=="33":
				character_race="Redcap"
			elif race_choice=="34":
				character_race="Rionnath"
			elif race_choice=="35":
				character_race="Satyr"
			elif race_choice=="36":
				character_race="Shurgan"
			elif race_choice=="37":
				character_race="Siren"
			elif race_choice=="38":
				character_race="Strigoi"
			elif race_choice=="39":
				character_race="Talis"
			elif race_choice=="40":
				character_race="Thrael"
			elif race_choice=="41":
				character_race="Troll"
			elif race_choice=="42":
				character_race="Varah"
			elif race_choice=="43":
				character_race="Vinori"
			elif race_choice=="44":
				character_race="Waheela"
			elif race_choice=="45":
				character_race="Wulver"
			elif race_choice=="46":
				character_race="Yuki-Ona"
			else:
				print("Not a valid choice, try again")
		elif character_world=="Post-Unification":
			race_choice=input("""
				Now comes the time to choose your character's race based on those available during your chosen era.
					* = Not available as a player character
				
				1 - Aamon - Owl-Headed, Winged Being
				2 - Ackirian - Grey-Skinned, Fanged, Human-Like Being
				3 - Adlet - Dog/Dökkálfar Being
				4 - Bokabu - Mobile, Plant Being
				5 - Cecaelia - Dökkálfar/Octopus Being
				6 - Centaur - Daoine Sith/Horse Being
				7 - Daoine Sith - Fair-Skinned, Long-Eared Being
				8 - Delphyne - Dökkálfar/Snake Being
				9 - Dökkálfar - Dark-Skinned, Daoine Sith-Like Being
				10 - Dragon* - Giant, Six-Limbed Reptile
				11 - Dwarf - Short, Stocky Being
				12 - Elfling - Daoine Sith/Human Offspring
				13 - Faerie* - Miniature, Winged, Daoine Sith-Like Being
				14 - Garikon - Muscular, Four-Armed, Rock Being
				15 - Garuda - Eagle-Headed, Winged Being
				16 - Giant* - Exceptionally Large, Human-Like Being
				17 - Goblin - Short, Gruesome Being
				18 - Golem* - Artificial Being
				19 - Greftaga - Mobile, Tree Being
				20 - Harpy - Human/Bird Being
				21 - Human - Human Being
				22 - Ibrigat - Squat, Bipedal Reptilian Being
				23 - Imp* - Dark, Faerie-Like Shapeshifter
				24 - Jorogumo - Dökkálfar/Spider Being
				25 - Khepri - Hive-Minded, Six-Limbed, Insectoid Being
				26 - Kitsune - Fox/Daoine Sith Shapeshifter
				27 - Merrow - Daoine Sith/Fish Being
				28 - Minotaur - Bull/Human Being
				29 - Nagual - Dog/Dökkálfar Shapeshifter
				30 - Ogre - Dark, Troll-Like Being
				31 - Ponaturi - Amphibious, Goblin-Like Being
				32 - Quetzal* - Winged, Dragon/Daoine Sith Offspring
				33 - Redcap - Goblin-Like Being
				34 - Rionnath - Human-Like Beings with Flower-Based Characteristics
				35 - Satyr - Daoine Sith/Goat Being
				36 - Shurgan - Muscular, Armoured Lava Being
				37 - Siren - Dark, Harpy-Like Being
				38 - Strigoi* - Fanged, Pale-Skinned, Blood-Drinking, Light-Fearing Being
				39 - Talis* - Elemental Being
				40 - Thrael - Daoine Sith/Newt Being
				41 - Troll - Huge, Goblin-Like Being
				42 - Varah - Boar/Dökkálfar Being
				43 - Waheela* - Giant Wolf with Ice Magic
				44 - Wulver - Wolf/Human Being
				45 - Yuki-Ona - Daoine Sith-Like Being with Ice Magic

				> """)
			if race_choice=="1":
				character_race="Aamon"
			elif race_choice=="2":
				character_race="Ackirian"
			elif race_choice=="3":
				character_race="Adlet"
			elif race_choice=="4":
				character_race="Bokabu"
			elif race_choice=="5":
				character_race="Cecaelia"
			elif race_choice=="6":
				character_race="Centaur"
			elif race_choice=="7":
				character_race="Daoine Sith"
			elif race_choice=="8":
				character_race="Delphyne"
			elif race_choice=="9":
				character_race="Dökkálfar"
			elif race_choice=="10":
				character_race="Dragon"
			elif race_choice=="11":
				character_race="Dwarf"
			elif race_choice=="12":
				character_race="Elfling"
			elif race_choice=="13":
				character_race="Faerie"
			elif race_choice=="14":
				character_race="Garikon"
			elif race_choice=="15":
				character_race="Garuda"
			elif race_choice=="16":
				character_race="Giant"
			elif race_choice=="17":
				character_race="Goblin"
			elif race_choice=="18":
				character_race="Golem"
			elif race_choice=="19":
				character_race="Greftaga"
			elif race_choice=="20":
				character_race="Harpy"
			elif race_choice=="21":
				character_race="Human"
			elif race_choice=="22":
				character_race="Ibrigat"
			elif race_choice=="23":
				character_race="Imp"
			elif race_choice=="24":
				character_race="Jorogumo"
			elif race_choice=="25":
				character_race="Khepri"
			elif race_choice=="26":
				character_race="Kitsune"
			elif race_choice=="27":
				character_race="Merrow"
			elif race_choice=="28":
				character_race="Minotaur"
			elif race_choice=="29":
				character_race="Nagual"
			elif race_choice=="30":
				character_race="Ogre"
			elif race_choice=="31":
				character_race="Ponaturi"
			elif race_choice=="32":
				character_race="Quetzal"
			elif race_choice=="33":
				character_race="Redcap"
			elif race_choice=="34":
				character_race="Rionnath"
			elif race_choice=="35":
				character_race="Satyr"
			elif race_choice=="36":
				character_race="Shurgan"
			elif race_choice=="37":
				character_race="Siren"
			elif race_choice=="38":
				character_race="Strigoi"
			elif race_choice=="39":
				character_race="Talis"
			elif race_choice=="40":
				character_race="Thrael"
			elif race_choice=="41":
				character_race="Troll"
			elif race_choice=="42":
				character_race="Varah"
			elif race_choice=="43":
				character_race="Waheela"
			elif race_choice=="44":
				character_race="Wulver"
			elif race_choice=="45":
				character_race="Yuki-Ona"
			else:
				print("Not a valid choice, try again")
		elif character_world=="Restricted":
			race_choice=input("""
				Now comes the time to choose your character's race based on those available during your chosen era.
					* = Not available as a player character
				
				1 - Aamon - Owl-Headed, Winged Being
				2 - Ackirian - Grey-Skinned, Fanged, Human-Like Being
				3 - Adlet - Dog/Dökkálfar Being
				4 - Bokabu - Mobile, Plant Being
				5 - Cecaelia - Dökkálfar/Octopus Being
				6 - Centaur - Daoine Sith/Horse Being
				7 - Daoine Sith - Fair-Skinned, Long-Eared Being
				8 - Delphyne - Dökkálfar/Snake Being
				9 - Dökkálfar - Dark-Skinned, Daoine Sith-Like Being
				10 - Dragon* - Giant, Six-Limbed Reptile
				11 - Dwarf - Short, Stocky Being
				12 - Elfling - Daoine Sith/Human Offspring
				13 - Garikon - Muscular, Four-Armed, Rock Being
				14 - Garuda - Eagle-Headed, Winged Being
				15 - Goblin - Short, Gruesome Being
				16 - Greftaga - Mobile, Tree Being
				17 - Harpy - Human/Bird Being
				18 - Human - Human Being
				19 - Ibrigat - Squat, Bipedal Reptilian Being
				20 - Jorogumo - Dökkálfar/Spider Being
				21 - Khepri - Hive-Minded, Six-Limbed, Insectoid Being
				22 - Merrow - Daoine Sith/Fish Being
				23 - Minotaur - Bull/Human Being
				24 - Ponaturi - Amphibious, Goblin-Like Being
				25 - Quetzal* - Winged, Dragon/Daoine Sith Offspring
				26 - Rionnath - Human-Like Beings with Flower-Based Characteristics
				27 - Satyr - Daoine Sith/Goat Being
				28 - Shurgan - Muscular, Armoured Lava Being
				29 - Siren - Dark, Harpy-Like Being
				30 - Thrael - Daoine Sith/Newt Being
				31 - Troll - Huge, Goblin-Like Being
				32 - Varah - Boar/Dökkálfar Being
				33 - Wulver - Wolf/Human Being

				> """)
			if race_choice=="1":
				character_race="Aamon"
			elif race_choice=="2":
				character_race="Ackirian"
			elif race_choice=="3":
				character_race="Adlet"
			elif race_choice=="4":
				character_race="Bokabu"
			elif race_choice=="5":
				character_race="Cecaelia"
			elif race_choice=="6":
				character_race="Centaur"
			elif race_choice=="7":
				character_race="Daoine Sith"
			elif race_choice=="8":
				character_race="Delphyne"
			elif race_choice=="9":
				character_race="Dökkálfar"
			elif race_choice=="10":
				character_race="Dragon"
			elif race_choice=="11":
				character_race="Dwarf"
			elif race_choice=="12":
				character_race="Elfling"
			elif race_choice=="13":
				character_race="Garikon"
			elif race_choice=="14":
				character_race="Garuda"
			elif race_choice=="15":
				character_race="Goblin"
			elif race_choice=="16":
				character_race="Greftaga"
			elif race_choice=="17":
				character_race="Harpy"
			elif race_choice=="18":
				character_race="Human"
			elif race_choice=="19":
				character_race="Ibrigat"
			elif race_choice=="20":
				character_race="Jorogumo"
			elif race_choice=="21":
				character_race="Khepri"
			elif race_choice=="22":
				character_race="Merrow"
			elif race_choice=="23":
				character_race="Minotaur"
			elif race_choice=="24":
				character_race="Ponaturi"
			elif race_choice=="25":
				character_race="Quetzal"
			elif race_choice=="26":
				character_race="Rionnath"
			elif race_choice=="27":
				character_race="Satyr"
			elif race_choice=="28":
				character_race="Shurgan"
			elif race_choice=="29":
				character_race="Siren"
			elif race_choice=="30":
				character_race="Thrael"
			elif race_choice=="31":
				character_race="Troll"
			elif race_choice=="32":
				character_race="Varah"
			elif race_choice=="33":
				character_race="Wulver"
			else:
				print("Not a valid choice, try again")

	global character_subrace, h_subrace
	while character_subrace is None:
		if character_race=="Aamon":
			subrace_choice=input("""
			Which subrace of Aamon is your character?
			1 - Diurna - Yellow-Eyes (Awake during daylight)
			2 - Crepusca - Orange-Eyes (Awake during dawn and dusk)
			3 - Nocturna - Black-Eyes (Awake at night)
			
			> """)
			if subrace_choice=="1":
				character_subrace="Diurna"
			elif subrace_choice=="2":
				character_subrace="Crepusca"
			elif subrace_choice=="3":
				character_subrace="Nocturna"
			else:
				print("Not a valid choice, try again")

		elif character_race=="Daoine Sith":
			roll=randint(1,12)
			if roll==12:
				randchoice=input("""
				You have the option of becoming a Hürdin;
				a Daoine Sith with the ability to transform into an animal.

				Do you wish to apply this trait to your character?
				y - Yes
				n - No
				> """)
				if randchoice=="y":
					h_subrace=input("""
					Which animal do you wish the character to be able to transform into?

					>""")
					character_subrace="Hürdin"
				else:
					character_subrace="None"
			else:
				character_subrace="None"

		elif character_race=="Dragon":
			subrace_choice=input("""
			Which subrace of Dragon is your character?
			1 - Northern
			2 - Southern
			3 - Sea

			> """)
			if subrace_choice=="1":
				character_subrace="Northern Dragon"
			elif subrace_choice=="2":
				character_subrace="Southern Dragon"
			elif subrace_choice=="3":
				character_subrace="Sea Dragon"
			else:
				print("Not a valid choice, try again")

		elif character_race=="Dwarf":
			roll=randint(1,12)
			if roll==12:
				randchoice=input("""
				You have the option of becoming a Hürdin;
				a Dwarf with the ability to transform into an animal.

				Do you wish to apply this trait to your character?
				y - Yes
				n - No
				> """)
				if randchoice=="y":
					h_subrace=input("""
					Which animal do you wish the character to be able to transform into?

					>""")
					character_subrace="Hürdin"
				else:
					character_subrace="None"
			else:
				character_subrace="None"

		elif character_race=="Faerie":
			subrace_choice=input("""
			Which subrace of Faerie is your character?
			1 - Alven
			2 - Ariel
			3 - Domovik
			4 - Drachen
			5 - Ghille Dhu
			6 - Kobold
			7 - Lunantishee
			8 - Pixie
			9 - Sprite
			10 - Tuatha De Danaan
			11 - Vardogl
			12 - Venusleutes

			> """)
			if subrace_choice=="1":
				character_subrace="Alven"
			elif subrace_choice=="2":
				character_subrace="Ariel"
			elif subrace_choice=="3":
				character_subrace="Domovik"
			elif subrace_choice=="4":
				character_subrace="Drachen"
			elif subrace_choice=="5":
				character_subrace="Ghille Dhu"
			elif subrace_choice=="6":
				character_subrace="Kobold"
			elif subrace_choice=="7":
				character_subrace="Lunantishee"
			elif subrace_choice=="8":
				character_subrace="Pixie"
			elif subrace_choice=="9":
				character_subrace="Sprite"
			elif subrace_choice=="10":
				character_subrace="Tuatha De Danaan"
			elif subrace_choice=="11":
				character_subrace="Vardogl"
			elif subrace_choice=="12":
				character_subrace="Venusleutes"
			else:
				print("Not a valid choice, try again")

		elif character_race=="Golem":
			subrace_choice=input("""
			Which material is your Golem made from?
			1 - Clay
			2 - Stone
			3 - Wood
			4 - Gold
			5 - Crystal
			6 - Iron

			> """)
			if subrace_choice=="1":
				character_subrace="Clay Golem"
			elif subrace_choice=="2":
				character_subrace="Stone Golem"
			elif subrace_choice=="3":
				character_subrace="Wood Golem"
			elif subrace_choice=="4":
				character_subrace="Gold Golem"
			elif subrace_choice=="5":
				character_subrace="Crystal Golem"
			elif subrace_choice=="6":
				character_subrace="Iron Golem"
			else:
				print("Not a valid choice, try again")

		elif character_race=="Human":
			roll=randint(1,12)
			if roll==12:
				randchoice=input("""
				You have the option of becoming a Hürdin;
				a Human with the ability to transform into an animal.

				Do you wish to apply this trait to your character?
				y - Yes
				n - No
				> """)
				if randchoice=="y":
					h_subrace=input("""
					Which animal do you wish the character to be able to transform into?

					>""")
					character_subrace="Hürdin"
				else:
					character_subrace="None"
			else:
				character_subrace="None"

		elif character_race=="Khepri":
			subrace_choice=input("""
			Which caste is your Khepri part of?
			1 - Brown Carapace
			2 - Green Carapace
			3 - Blue Carapace
			4 - White Carapace
			5 - Yellow Carapace
			6 - Black Carapace
			7 - Red Carapace
			8 - Purple Carapace

			> """)
			if subrace_choice=="1":
				character_subrace="Brown Carapace"
			elif subrace_choice=="2":
				character_subrace="Green Carapace"
			elif subrace_choice=="3":
				character_subrace="Blue Carapace"
			elif subrace_choice=="4":
				character_subrace="White Carapace"
			elif subrace_choice=="5":
				character_subrace="Yellow Carapace"
			elif subrace_choice=="6":
				character_subrace="Black Carapace"
			elif subrace_choice=="7":
				character_subrace="Red Carapace"
			elif subrace_choice=="8":
				character_subrace="Purple Carapace"
			else:
				print("Not a valid choice, try again")

		elif character_race=="Talis":
			subrace_choice=input("""
			Which element is your Talis?
			1 - Air
			2 - Dark
			3 - Earth
			4 - Fire
			5 - Light
			6 - Water

			> """)
			if subrace_choice=="1":
				character_subrace="Air Talis"
			elif subrace_choice=="2":
				character_subrace="Dark Talis"
			elif subrace_choice=="3":
				character_subrace="Earth Talis"
			elif subrace_choice=="4":
				character_subrace="Fire Talis"
			elif subrace_choice=="5":
				character_subrace="Light Talis"
			elif subrace_choice=="6":
				character_subrace="Water Talis"
			else:
				print("Not a valid choice, try again")

		elif character_race=="Troll":
			subrace_choice=input("""
			What type of Troll is your character?
			1 - Mountain
			2 - Cave
			3 - Jungle
			4 - Snow

			> """)
			if subrace_choice=="1":
				character_subrace="Mountain Troll"
			elif subrace_choice=="2":
				character_subrace="Cave Troll"
			elif subrace_choice=="3":
				character_subrace="Jungle Troll"
			elif subrace_choice=="4":
				character_subrace="Snow Troll"
			else:
				print("Not a valid choice, try again")

		else:
			character_subrace="None"

	cls()
	global character_name
	while character_name is None:
		if character_race=="Aamon":
			print("""
			Aamon Naming Conventions:
				Aamons have a given name and a family name.
			Given Name Examples:
				Arcadys - Brashal - Horis - Larisi - Lavento - Ovazi - Varisia
			Family Name Examples:
				Arcan - Carvo - Krayse - Minasi - Passel

			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Ackirian":
			print("""
			Ackirian Naming Conventions:
				Ackirians have a given name and a family name.
			Given Name Examples:
				Bandon - Grayph - Mendal - Sedge - Vace
			Family Name Examples:
				Bavaro - Capari - Dirego - Oremi - Sintali
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Adlet":
			print("""
			Adlet Naming Conventions:
				Adlets have a single given name with an instance of double letters in it.
			Given Name Examples:
				Dakkin - Gelln - Sharrik - Vurri
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Bokabu":
			print("""
			Bokabu Naming Conventions:
				Bokabu have a single given name.
			Given Name Examples:
				Alisenia - Corontix - Hawthan - Levitus - Lilithia - Maleav - Rhondan - Sondron - Tanendon

			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Cecaelia":
			print("""
			Cecaelia Naming Conventions:
				Cecaelia have two given names and a family name.
			Given Name Examples:
				Barumi - Falinia - Gurosi - Marova - Raluti - Toluna - Zarilin
			Family Name Examples:
				Binura - Eshinda - Kurusin - Maelan - Seruli - Vaelint
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Centaur":
			print("""
			Centaur Naming Conventions:
				Centaurs have one given name and two family names, in the style of Legionnaires.
			Given Name Examples:
				Agita - Ecurio - Erisia - Heilo - Herilas - Iosati - Petrovus - Sagasi - Tarinis - Tavi
			Family Name Examples:
				Arogus - Bilinus - Korinus - Limasi - Malirus - Sagus - Torovus - Travisi - Uatarus
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Daoine Sith":
			print("""
			Daoine Sith Naming Conventions:
				Daoine Sith have a family name and a given name. Daoine honour family before self, so the family name comes first.
				Family names are only two or three letters long and are separated by an apostrophe.
			Full Name Examples:
				An'Kona - Bo'Uvar - Ey'Lyris - Ji'Komi - Ke'Juva - Ki'Lania - Ki'Miro - Ko'Lisha - Li'Fiora - Olo'Daram - Qi'Bellori - Qi'Tarrom - Ri'Kalova - Xo'Baros
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Delphyne":
			print("""
			Delphyne Naming Conventions:
				Delphyne have a given name and a family name.
			Given Name Examples:
				Addrena - Boandar - Correno - Covran - Hilisent - Kai - Luiel - Pylith - Pythev - Raysse - Shahede
			Family Name Examples:
				Baoni - Grenesh - Korozma - Ogorose - Seridep - Typhir - Vilisian
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Dökkálfar":
			print("""
			Dökkálfar Naming Convetions:
				Dökkálfar have a given name and a family name.
			Given Name Examples:
				Corik - Firendan - Firrim - Govaro - Gran - Inerva - Jerendar - Kraen - Ordi
			Family Name Examples:
				Kavo - Kove - Ovaxi - Silh - Travin - Viedal

			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_subrace=="Northern Dragon":
			print("""
			Northern Dragon Naming Conventions:
				Northern Dragons have a given name, a clutch name (family generation name), and a clan name. Dragons honour their clans, 
				then their cluthes, before themselves. Northern Dragon given names always contain only four letters.
			Clan Names:
				Beliar - Fyliol - Lunedar - Mashindo - Prodeshi - Solinar - Twiriad
			Clutch Name Examples:
				Bresco - Daelin - Karnow - Revene - Rostin - Shendi - Trimand - Varandi
			Given Name Examples:
				Koli - Liro - Norv - Pika - Rono - Savi - Tano - Varo
			
			The example names above have already been used, so try to avoid those exact names, except for the Clan Names, which are the only ones available.
			> """)
		
		elif character_subrace=="Southern Dragon":
			print("""
			Southern Dragon Naming Conventions:
				Southern Dragons have a given name and a family name. Southern Dragon given and family names always consist of three letters each.
			Given Name Examples:
				Ari - Chi - Khi - Joi - Nei - Sia - Umi - Ven
			Family Name Examples:
				Boi - Cio - Ges - Lin - Mun - Shi - Tai - Zin
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_subrace=="Sea Dragon":
			print("""
			Sea Dragon Naming Conventions:
				Sea Dragons have only a given name, which is always three syllables long.
			Given Name Examples:
				Avina - Colino - Honodi - Jamali - Minoka - Tenoba - Wazaki - Yariko
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Dwarf":
			print("""
			Dwarf Naming Conventions:
				Dwarves have a given name and a family name. Dwarven family names consist of a combined two words based on a 
				great deed or act performed by their family in the past.
			Given Name Examples:
				Aseli - Ashis - Borii - Fovan - Irin - Loukar - Mako - Morgo
			Family Name Examples:
				Blackheart - Blackpalm - Gemfinder - Halfaxe - Highborn - Ironwill - Moonsong - Sickleside - Stoneheart - Trollsbane
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Elfling":
			print("""
			Elfling Naming Conventions:
				Elflings take their names from either their Daoine Sith or Human parent, depending on which they are closer to 
				or where they were born.
			Full Name Examples:
				Kina Baltur - Fo'Denu - Tarris Motta - Va'Noren
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Faerie":
			print("""
			Faerie Naming Conventions:
				Faeries have only a given name.
			Given Name Examples:
				Alinam - Carolia - Linsei - Numa - Riahan - Sula - Tyress - Viana
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Garikon":
			print("""
			Garikon Naming Conventions:
				Garikons have a given name, which is created from half of each parents' name. Males take the first half of their 
				father's name and the second half of their mother's. Females takes the first half of their mother's name and 
				the second half of their father's. In the case of a second son or daughter, Garikon males are given the first half 
				of their father's name and the second half of their maternal grandmother's name, while Garikon females are given the first 
				half of their mother's name and the second half of their paternal grandfather's name. Since Garikons have no lips and only 
				their crushing jaws, they use no sounds that humans would make with their lips, such as 'B', 'F', 'M', 'P' or 'V'.
			Given Name Examples:
				Asharde - Ashira - Dacachar - Denira - Eristas - Hireteth - Listas - Relarde - Soruteth - Thahred - Trenis
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Garuda":
			print("""
			Garuda Naming Conventions:
				Garudas have only a given name.
			Given Name Examples:
				Aventis - Draca - Egilia - Erkrit - Miliun - Oranith - Storin - Wode
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Giant":
			print("""
			Giant Naming Conventions:
				Giants have only a given name.
			Given Name Examples:
				Borf - Damba - Gonn - Noff - Ropp - Turrm
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Goblin":
			print("""
			Goblin Naming Conventions:
				Goblins have a given name and a tribe name, although they only use their tribe name with other Goblins.
			Given Name Examples:
				Bravantin - Franarida - Gramadrist - Huridig - Krophtin - Mekridin - Oniris
			Tribe Name Examples:
				Bugrod - Funrol - Ishtik - Mussha - Simeal - Troguon
			
			The example names above have already been used, so try to avoid those exact names, although use of the Tribe names is fine.
			> """)
		
		elif character_race=="Golem":
			print("""
			Golem Naming Conventions:
				Golems have only a given name which consists of only two syllables.
			Given Name Examples:
				Aman - Binur - Doriph - Hepro - Milon - Shavin
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Greftaga":
			print("""
			Greftaga Naming Conventions:
				Greftagas have a single given name which consists of either three or four syllables.
			Given Name Examples:
				Ahshanati - Ghorolon - Niharov - Rilahoma - Shivanoth - Urhaventon
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Harpy":
			print("""
			Harpy Naming Conventions:
				Harpies are given an Egg Name on their hatching day, and an Honour Name on the day they become an adult, at age 16. Honour names always end with a 'day'.
			Given/Egg Name Examples:
				Fernim - Harvic - Iola - Kali - Mazin - Melira - Orno - Raphe - Shava - Terrow - Verca - Worval
			Honour Name Examples:
				Bishiday - Foloday - Imeday - Kaliday - Mishiday - Shavaday - Toroday - Valuday
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Human":
			print("""
			Human Naming Conventions:
				Humans have at least one given name and a family name.
			Given Name Examples:
				Aytria - Danco - Fittu - Gammaro - Gatus - Gollsha - Ilia - Jolus - Kob - Koltte - Maller -  Merrik - Nuem - Phindar - Sovi
			Family Name Examples:
				Baler - Cabarn - Canov - Carma - Derise - Gannatry - Haxton - Illan - Karven - Pache - Pago - Penine - Valisci - Wirrel
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Ibrigat":
			print("""
			Ibrigat Naming Conventions:
				Ibrigats have a given name and a tribe name. Ibrigat given names consist of three syllables.
			Given Name Examples:
				Agiron - Cobantir - Fitaran - Terashin
			Tribe Names:
				Bilwa - Dondo - Felden - Mortil - Tundas - Vilesh
			
			The example names above have already been used, so try to avoid those exact names, although use of the Tribe names is fine.
			> """)
		
		elif character_race=="Imp":
			print("""
			Imp Naming Conventions:
				Imps have only a given name that consists of three syllables.
			Given Name Examples:
				Felizan - Indalak - Kopheshu - Lushidu - Miganash - Troshibu - Vikuna

			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Jorogumo":
			print("""
			Jorogumo Naming Conventions:
				Jorogumos have a given name and two family names. Jorogumo given names consist of four letters, as does the first part of the family name.
			Given Name Examples:
				Dinu - Frin - Koal - Newa - Unti - Vank
			First Family Name Examples:
				Alis - Besh - Crov - Faln - Neth - Shal - Tros
			Second Famil Name Examples:
				Enith - Eodey - Galani - Klishan - Molonish - Rokandi - Tromila

			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Khepri":
			print("""
			Khepri Naming Conventions:
				Khepri, being a hive-minded race, don't use names. However, when an individual Khepri develops free will and decides to escape 
				the hive, they usually, but not always, end up naming themselves with a single name, based around something they see on 
				their journey, or an ideal they wish to pursue.
			Chosen Name Examples:
				Firebird - Freeheart - Horizonhunter - Livefull - Moonrise - Yellowhorn
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Kitsune":
			print("""
			Kitsune Naming Conventions:
				Most Kitsune spend the majority of their time living and looking like Daoine Sith. As such, their naming conventions are similar, 
				with their family name coming before their given name and conjoined with an apostrophe. However, Kitsune family names consist 
				of two syllables, rather than two letters. They will also shorten their family name to the first two letters when interacting 
				with Daoine Sith.
			Full Name Examples:
				Aval'Vinam - Dores'Troshil - Mivay'Ara - Sarov'Rinol - Taren'Enu
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Merrow":
			print("""
			Merrow Naming Conventions:
				Merrow have a single given name.
			Given Name Examples:
				Arcka - Bysindo - Krinis - Kuruq - Qualan - Riluqar - Tarquis
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Minotaur":
			print("""
			Minotaur Naming Conventions:
				Minotaurs have a given name and a family name. When they come of age (15), they are also given an Honour Name.
			Given Name Examples:
				Gorom - Gromisha - Iresto - Krascel - Trask - Vaike
			Honour Name Examples:
				Doronus - Haricas - Paraclius - Rictor - Troshus
			Family Name Examples:
				Bodar - Ferlin - Mascu - Shonin - Tarrik
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Nagual":
			print("""
			Nagual Naming Conventions:
				Naguals have a given name and a family name.
			Given Name Examples:
				Dovana - Kisuni - Pilosi - Salisco - Ushinar - Wenaro
			Family Name:
				Calsen - Gaphalsi - Ikansi - Noruva - Ratha - Yoden
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Ogre":
			print("""
			Ogre Naming Conventions:
				Ogres have a single given name.
			Given Name Examples:
				Krest - Noush - Partha - Orush - Roonga - Terix
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Ponaturi":
			print("""
			Ponaturi Naming Conventions:
				Ponaturi have a single given name.
			Given Name Examples:
				Buldara - Erondal - Hinisa - Kulishu - Nocatar - Shurin - Trauin
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Quetzal":
			print("""
			Quetzal Naming Conventions:
				Quetzal naming follows those of their parents, the Northern Dragons.
			Clan Names:
				Beliar - Fyliol - Lunedar - Mashindo - Prodeshi - Solinar - Twiriad
			Clutch Name Examples:
				Bresco - Daelin - Karnow - Revene - Rostin - Shendi - Trimand - Varandi
			Given Name Examples:
				Koli - Liro - Norv - Pika - Razi - Rono - Savi - Tano - Varo
			
			The example names above have already been used, so try to avoid those exact names, except for the Clan Names, which are the only ones available.
			> """)
		
		elif character_race=="Redcap":
			print("""
			Redcap Naming Conventions:
				Redcaps have a single given name.
			Given Name Examples:
				Baan - Crell - Darru - Gellad - Noosi - Vak - Wrostin
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Rionnath":
			print("""
			Rionnath Naming Conventions:
				Rionnaths descend from a Human ancestor, and follow Human naming styles.
			Given Name Examples:
				Aytria - Danco - Fittu - Gammaro - Gatus - Gollsha - Ilia - Jolus - Kob - Koltte - Maller -  Merrik - Nuem - Phindar - Sovi
			Family Name Examples:
				Baler - Cabarn - Canov - Carma - Derise - Gannatry - Haxton - Illan - Karven - Pache - Pago - Penine - Valisci - Wirrel
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Satyr":
			print("""
			Satyr Naming Conventions:
				Satyrs have a given name and a family name.
			Given Name Examples:
				Cavir - Jok - Kiwo - Kresto - Lika - Miri - Orman - Wexil
			Family Name Examples:
				Astar - Caival - Filius - Gharus - Morias - Shea - Umurant
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Shurgan":
			print("""
			Shurgan Naming Conventions:
				Shurgans have only a given name, although they are often named after heroes and famous Shurgans of the past.
			Given Name Examples:
				Calerada - Larion - Livalus - Malangus - Molonda - Promerius - Pryse - Scaladrel - Surt
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Siren":
			print("""
			Siren Naming Conventions:
				Sirens have only a given name.
			Given Name Examples:
				Gialisi - Lulina - Nizalu - Poliani - Segrea - Trian
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Strigoi":
			print("""
			Strigoi Naming Conventions:
				Strigoi have a given name and a family name.
			Given Name Examples:
				Diraca - Nosantu - Validar
			Family Name Examples:
				Imalapi - Nonisca - Stilani
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Talis":
			print("""
			Talis Naming Conventions:
				Talis have only a given name.
			Given Name Examples:
				Cosatan - Elothin - Estannad - Ilminia - Orobis - Shael - Teieda -  Tumina
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Thrael":
			print("""
			Thrael Naming Conventions:
				Thraels have a given name, a family name and a home name. The home name is only used when travelling or talking to other races, and is the name of the Hahnunah in which they live. If the Thrael has left the safety of the giant turtles in which they make their home, they take the home name 'Noshell'.
			Given Name Exmaples:
				Bilian - Elyn - Isiso - Levish - Nist - Rishuli - Tersi
			Family Name Examples:
				Dullan - Feltis - Jusine - Mokino - Sulanta - Ubilin
			Home Names:
				Appigentius - Noshell - Torinatagus
			
			The example names above have already been used, so try to avoid those exact names, except for the Home Names, which are the only ones available.
			> """)
		
		elif character_race=="Troll":
			print("""
			Troll Naming Conventions:
				Trolls have a given name and a tribe name. A common feature of Troll names is the use of double letters in the name, 
				although this isn't always the case.
			Given Name Examples:
				Brarsh - Bromun - Curgha - Frrod - Gorrsh - Hurhag - Mrogga - Reskul - Trosk - Vargha
			Tribe Name Examples:
				Ghursh - Mugluhn - Pursun - Shugida
			
			The example names above have already been used, so try to avoid those exact names, although use of the Tribe names is fine.
			> """)
		
		elif character_race=="Varah":
			print("""
			Varah Naming Conventions:
				Varahs have a given name which is separated into two parts with an apostrophe and a family name. The second part of the given name denotes which tribe the Varah belongs to.
			Given Name Examples:
				Biahl'hgrosh - Ehnga'gahlan - Teish'egrehn - Yho'hgrosh
			Family Name Examples:
				Ahlgahn - Feinhem - Oinheld - Neiheimh - Sehndiem
			Tribe Names (To form the second part of the Given Name):
				Egrehn - Gahlan - Hgrosh - Khalein - Neihind - Teinhad
			
			The example names above have already been used, so try to avoid those exact names, although use of the Tribe names is fine.
			> """)
		
		elif character_race=="Vinori":
			print("""
			Vinori Naming Conventions:
				Vinori have a single given name.
			Given Name Examples:
				Eshc - Girahn - Ienas - Lethk
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Waheela":
			print("""
			Waheela Naming Conventions:
				Waheelas have a given name and, once they become recognised by their pack, they are given an Honour name by the pack alphas.
				Honour names are traditionally based upon some feat or achievment.
			Given Name Examples:
				Asena - Fenris - Hati - Holo - Horevir - Managarm - Skoll - Urik
			Honour Name Examples:
				Icefang - Windrider
			
			The example names above have already been used, so try to avoid those exact names.

			> """)
		
		elif character_race=="Wulver":
			print("""
			Wulver Naming Conventions:
				Wulvers have a given name and a family name.
			Given Name Examples:
				Alran - Diovi - Candar - Kulon - Nouli - Relis - Torm - Zepha
			Family Name Examples:
				Lurap - Mendan - Romus - Shezin - Traesh
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
		
		elif character_race=="Yuki-Ona":
			print("""
			Yuki-Ona Naming Conventions:
				Yuki-Onas have a family name and a given name. Like Daoine Sith and Kitsune, they honour family before self and 
				use the family name first.
			Family Name Examples:
				Dariko - Folana - Hakira - Senvol - Tivea
			Given Name Examples:
				Eria - Gaani - Inso - Kalian - Nianka
			
			The example names above have already been used, so try to avoid those exact names.
			> """)
#Put logic here to split up clans, tribes and everything else for more lines saved.
		character_name = input("""

		What is your character's name?
		
		""")

	global character_gender
	while character_gender is None:
		if character_subrace=="Purple Carapace":
			character_gender="Female"
		elif character_race=="Golem":
			character_gender="None"
		elif character_race=="Greftaga":
			character_gender="None"
		else:
			gender_choice=input("""
			Is """+character_name+""" male or female?
			1 - Male
			2 - Female
			3 - Other
			4 - Unknown

			""")
			if gender_choice=="1":
				character_gender="Male"
			elif gender_choice=="2":
				character_gender="Female"
			elif gender_choice=="3":
				character_gender="Other"
			elif gender_choice=="4":
				character_gender="Unknown"
			else:
				print("Not a valid choice, try again")
	
	global character_age
	while character_age is None:
		if character_race=="Aamon":
			character_age=input("""
			Average Aamon Lifespan:
				100 Years
			Aamon are considered adults at:
				20 Years Old

			What is """+character_name+"""'s age?
	
			>""")

		elif character_race=="Ackirian":
			character_age=input("""
			Average Ackirian Lifespan:
				80 Years
			Ackirians are considered adults at:
				17 Years Old

			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Adlet":
			character_age=input("""
			Average Adlet Lifespan:
				50 Years
			Adlets are considered adults at:
				15 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)
		
		elif character_race=="Bokabu":
			character_age=input("""
			Average Bokabu Lifespan:
				500 Years
			Bokabu Lifecycle Details:
				Seedling (Seed-Like) 				- 0 - ~2 Years
				Budling (Bud with searching tongue)		- ~2 - ~5 Years
				Sprout (Bud with exposed head) 			- ~5 - ~10 Years
				Sapling (Budling-Like with uprooted roots) 	- ~10 - ~22 Years
				Adult					- ~22 - ~150 Years
				Elder (Tree-like, planted roots)		- ~150+
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Cecaelia":
			character_age=input("""
			Average Cecaelia Lifespan:
				65 Years
			Cecaelias are considered adults at:
				16 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Centaur":
			character_age=input("""
			Average Centaur Lifespan:
				60 Years
			Centaurs are considered adults at:
				17 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Daoine Sith":
			character_age=input("""
			Average Daoine Sith Lifespan:
				100 Years
			Daoine Sith are considered adults at:
				18 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)
		
		elif character_race=="Delphyne":
			character_age=input("""
			Average Delphyne Lifespan:
				60 Years
			Delphynes are considered adults at:
				17 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Dökkálfar":
			character_age=input("""
			Average Dökkálfar Lifespan:
				100 Years
			Dökkálfar are considered adults at:
				16 Years Old

			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Dragon":
			character_age=input("""
			Average Dragon Lifespan:
				1000 Years
			Dragons are considered adults at:
				50 Years Old
			
			What is """+character_name+"""'s age?

			> """)
		
		elif character_race=="Dwarf":
			character_age=input("""
			Average Dwarf Lifespan:
				70 Years
			Dwarves are considered adults at:
				18 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)
		
		elif character_race=="Elfling":
			character_age=input("""
			Average Elfling Lifespan:
				90 Years
			Elflings are considered adults at:
				17 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Faerie":
			character_age=input("""
			Average Faerie Lifespan:
				200 Years
			Faeries are considered adults at:
				25 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Garikon":
			character_age=input("""
			Average Garikon Lifespan:
				250 Years
			Garikons are considered adults at:
				20 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Garuda":
			character_age=input("""
			Average Garuda Lifespan:
				100 Years
			Garudas are considered adults at:
				18 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Giant":
			character_age=input("""
			Average Giant Lifespan:
				200 Years
			Giants are considered adults at:
				25 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)
		
		elif character_race=="Goblin":
			character_age=input("""
			Average Goblin Lifespan:
				50 Years
			Goblins are considered adults at:
				15 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)
		
		elif character_race=="Golem":
			character_age=input("""
			Average Golem Lifespan:
				Unlimited (Unless Destroyed)
			Golems are considered adults at time of creation.

			What is """+character_name+"""'s age?
			
			> """)
		
		elif character_race=="Greftaga":
			character_age=input("""
			Average Greftaga Lifespan:
				500 Years
			Greftagas are considered adults at:
				13 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Harpy":
			character_age=input("""
			Average Harpy Lifespan:
				50 Years
			Harpies are considered adults at:
				16 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Human":
			character_age=input("""
			Average Human Lifespan:
				60 Years
			Humans are considered adults at:
				16 Years Old

			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Ibrigat":
			character_age=input("""
			Average Ibrigat Lifespan:
				60 Years
			Ibrigats are considered adults at:

			What is """+character_name+"""'s age?
			
			> """)
		
		elif character_race=="Imp":
			character_age=input("""
			Average Imp Lifespan:
				180 Years
			Imps are considered adults at:
				15 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Jorogumo":
			character_age=input("""
			Average Jorogumo Lifespan:
				80 Years
			Jorogumos are considered adults at:
				15 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Khepri":
			character_age=input("""
			Average Khepri Lifespan:
				120 Years
			Khepri Lifecycle Details:
				Egg -	0 - ~2 Years
				Grub -	~2 - ~5 Years
				Pupa -	~5 - ~15 Years
				Adult -	~15+ Years
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Kitsune":
			character_age=input("""
			Average Kitsune Lifespan:
				100 Years
			Kitsunes are considered adults at:
				17 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Merrow":
			character_age=input("""
			Average Merrow Lifespan:
				60 Years
			Merrow are considered adults at:
				16 Years Old

			What is """+character_name+"""'s age?
			
			> """)
		
		elif character_race=="Minotaur":
			character_age=input("""
			Average Minotaur Lifespan:
				80 Years
			Minotaurs are considered adults at:
				19 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)
		
		elif character_race=="Nagual":
			character_age=input("""
			Average Nagual Lifespan:
				60 Years
			Naguals are considered adults at:
				18 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Ogre":
			character_age=input("""
			Average Ogre Lifespan:
				50 Years
			Ogres are considered adults at:
				16 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Ponaturi":
			character_age=input("""
			Average Ponaturi Lifespan:
				70 Years
			Ponaturis are considered adults at:
				16 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Quetzal":
			character_age=input("""
			Average Quetzal Lifespan:
				800 Years
			Quetzals are considered adults at:
				20 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Redcap":
			character_age=input("""
			Average Redcap Lifespan:
				40 Years
			Redcaps are considered adults at:
				15 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Rionnath":
			character_age=input("""
			Average Rionnath Lifespan:
				80 Years
			Rionnaths are considered adults at:
				17 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Satyr":
			character_age=input("""
			Average Satyr Lifespan:
				50 Years
			Satyrs are considered adults at:
				16 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Shurgan":
			character_age=input("""
			Average Shurgan Lifespan:
				250 Years
			Shurgans are considered adults at:
				20 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Siren":
			character_age=input("""
			Average Siren Lifespan:
				50 Years
			Sirens are considered adults at:
				16 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)
		
		elif character_race=="Strigoi":
			character_age=input("""
			Average Strigoi Lifespan:
				700 Years
			Strigoi are considered adults at:
				18 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)
		
		elif character_race=="Talis":
			character_age=input("""
			Average Talis Lifespan:
				900 Years
			Talis are considered adults at:
				25 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)
		
		elif character_race=="Thrael":
			character_age=input("""
			Average Thrael Lifespan:
				70 Years
			Thraels are considered adults at:
				18 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Troll":
			character_age=input("""
			Average Troll Lifespan
				80 Years
			Trolls are considered adults at:
				15 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Varah":
			character_age=input("""
			Average Varah Lifespan:
				50 Years
			Varahs are considered adults at:
				16 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)
		
		elif character_race=="Vinori":
			character_age=input("""
			Average Vinori Lifespan:
				90 Years
			Vinori are considered adults at:
				15 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Waheela":
			character_age=input("""
			Average Waheela Lifespan:
				1000 Years
			Waheela are considered adults at:
				50 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

		elif character_race=="Wulver":
			character_age=input("""
			Average Wulver Lifespan:
				120 Years
			Wulvers are considered adults at:
				18 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)
		
		elif character_race=="Yuki-Ona":
			character_age=input("""
			Average Yuki-Ona Lifespan:
				100 Years
			Yuki-Ona are considered adults at:
				17 Years Old
			
			What is """+character_name+"""'s age?
			
			> """)

	

	global character_level
	character_level=int(input("""
	What is """+character_name+"""'s level?
	
	>"""))
		
	global character_xp
	character_xp=input("""
	How much XP does """+character_name+""" start with (or, how much XP does a character gain for killing """+character_name+""")?

	>""")

	cls()
	global character_worship
	while character_worship is None:
		if character_world=="Primal Eloria":
			character_deity=input("""
			If """+character_name+""" is pious, which deity do they prey to for guidance?
			If """+character_name+""" isn't pious, type 0.

			1 - Belim: God of Darkness, Death and Patron of Secrets
			2 - Faren: God of Earth, Nature and Patron of Crafts
			3 - Kivena: Goddess of Water, Oceans and Patron of Sailing
			4 - Movan: God of Fire, Spirit and Patron of Home
			5 - Novia: Goddess of Light, Life and Patron of Healing
			6 - Valira: Goddess of Air, Weather and Patron of Travel
			7 - Chronia: Goddess of Time and the Patron of History

			8 - Aurien: God of Dreams and Dawn
			9 - Everia: Goddess of Nightmares and Dusk
			10 - Ilisium: God of Ice and Winter
			11 - Palitar: Goddess of Plants and Spring
			12 - Sharam: Goddess of Volcanoes and Summer
			13 - Veelae: God of Storms and Autumn
			
			> """)
			if character_deity=="0":
				character_worship="None"
			elif character_deity=="1":
				character_worship="Belim"
			elif character_deity=="2":
				character_worship="Faren"
			elif character_deity=="3":
				character_worship="Kivena"
			elif character_deity=="4":
				character_worship="Movan"
			elif character_deity=="5":
				character_worship="Novia"
			elif character_deity=="6":
				character_worship="Valira"
			elif character_deity=="7":
				character_worship="Chronia"
			elif character_deity=="8":
				character_worship="Aurien"
			elif character_deity=="9":
				character_worship="Everia"
			elif character_deity=="10":
				character_worship="Ilisium"
			elif character_deity=="11":
				character_worship="Palitar"
			elif character_deity=="12":
				character_worship="Sharam"
			elif character_deity=="13":
				character_worship="Veelae"
			else:
				print("Not a valid choice, try again")
		elif character_world=="Primal Ta'bros":
			character_deity=input("""
			If """+character_name+""" is pious, which deity do they prey to for guidance?
			If """+character_name+""" isn't pious, type 0.

			1 - Emolat: Goddess of Darkness, Destruction and the Patron of Hunting
			2 - Rigath: God of Earth, The Forge and the Patron of Trade
			3 - Hurüsh: God of Air, Storms and the Patron of Vengeance
			4 - Magarab: Goddess of Fire, Chaos and the Patron of War
			5 - Inauri: Goddess of Water, Oceans and Patron of The Unknown
			
			> """)
			if character_deity=="0":
				character_worship="None"
			elif character_deity=="1":
				character_worship="Emolat"
			elif character_deity=="2":
				character_worship="Rigath"
			elif character_deity=="3":
				character_worship="Hurüsh"
			elif character_deity=="4":
				character_worship="Magarab"
			elif character_deity=="5":
				character_worship="Inauri"
			else:
				print("Not a valid choice, try again")
		elif character_world=="Eloria - 175,000 BDT" or "Eloria - 156,900 BDT":
			character_deity=input("""
			If """+character_name+""" is pious, which deity do they prey to for guidance?
			If """+character_name+""" isn't pious, type 0.

			1 - Belim: God of Darkness, Death and Patron of Secrets
			2 - Faren: God of Earth, Nature and Patron of Crafts
			3 - Kivena: Goddess of Water, Oceans and Patron of Sailing
			4 - Movan: God of Fire, Spirit and Patron of Home
			5 - Novia: Goddess of Light, Life and Patron of Healing
			6 - Valira: Goddess of Air, Weather and Patron of Travel
			7 - Chronia: Goddess of Time and the Patron of History

			8 - Aurien: God of Dreams and Dawn
			9 - Everia: Goddess of Nightmares and Dusk
			10 - Ilisium: God of Ice and Winter
			11 - Palitar: Goddess of Plants and Spring
			12 - Sharam: Goddess of Volcanoes and Summer
			13 - Veelae: God of Storms and Autumn

			14 - Amiras: Goddess of Love, Family and the Patron of Marriage
			15 - Eretiad: God of Premonition, Belief and the Patron of Oracles
			16 - Hularik: God of War, Loyatly and the Patron of Brotherhood
			17 - Muzio: Goddess of Inspiration, Confidence and the Patron of The Arts
			18 - Oulana: Goddess of Domestication, The Harvest and the Patron of Farming
			19 - Quanir: God of Coasts, Change and the Patron of Navigation
			20 - Ravion: God of Wilderness, The Hunt and the Patron of Hunting
			21 - Reiyat: Goddess of Rivers, Harmony and the Patron of Fishing

			22 - Thanoukos: God of Souls, Ghosts and the Patron of Graveyards
			23 - Suvadag: God of Lust, Seduction and the Patron of Brothels
			
			> """)
			if character_deity=="0":
				character_worship="None"
			elif character_deity=="1":
				character_worship="Belim"
			elif character_deity=="2":
				character_worship="Faren"
			elif character_deity=="3":
				character_worship="Kivena"
			elif character_deity=="4":
				character_worship="Movan"
			elif character_deity=="5":
				character_worship="Novia"
			elif character_deity=="6":
				character_worship="Valira"
			elif character_deity=="7":
				character_worship="Chronia"
			elif character_deity=="8":
				character_worship="Aurien"
			elif character_deity=="9":
				character_worship="Everia"
			elif character_deity=="10":
				character_worship="Ilisium"
			elif character_deity=="11":
				character_worship="Palitar"
			elif character_deity=="12":
				character_worship="Sharam"
			elif character_deity=="13":
				character_worship="Veelae"
			elif character_deity=="14":
				character_worship="Amiras"
			elif character_deity=="15":
				character_worship="Eretiad"
			elif character_deity=="16":
				character_worship="Hularik"
			elif character_deity=="17":
				character_worship="Muzio"
			elif character_deity=="18":
				character_worship="Oulana"
			elif character_deity=="19":
				character_worship="Quanir"
			elif character_deity=="20":
				character_worship="Ravion"
			elif character_deity=="21":
				character_worship="Reiyat"
			elif character_deity=="22":
				character_worship="Thanoukos"
			elif character_deity=="23":
				character_worship="Suvadag"
			else:
				print("Not a valid choice, try again")
		elif character_world=="Eloria - 100,000 BDT":
			character_deity=input("""
			If """+character_name+""" is pious, which deity do they prey to for guidance?
			If """+character_name+""" isn't pious, type 0.

			1 - Belim: God of Darkness, Death and Patron of Secrets
			2 - Faren: God of Earth, Nature and Patron of Crafts
			3 - Kivena: Goddess of Water, Oceans and Patron of Sailing
			4 - Movan: God of Fire, Spirit and Patron of Home
			5 - Novia: Goddess of Light, Life and Patron of Healing
			6 - Valira: Goddess of Air, Weather and Patron of Travel
			7 - Chronia: Goddess of Time and the Patron of History

			8 - Aurien: God of Dreams and Dawn
			9 - Everia: Goddess of Nightmares and Dusk
			10 - Ilisium: God of Ice and Winter
			11 - Palitar: Goddess of Plants and Spring
			12 - Sharam: Goddess of Volcanoes and Summer
			13 - Veelae: God of Storms and Autumn

			14 - Amiras: Goddess of Love, Family and the Patron of Marriage
			15 - Eretiad: God of Premonition, Belief and the Patron of Oracles
			16 - Hularik: God of War, Loyatly and the Patron of Brotherhood
			17 - Muzio: Goddess of Inspiration, Confidence and the Patron of The Arts
			18 - Oulana: Goddess of Domestication, The Harvest and the Patron of Farming
			19 - Quanir: God of Coasts, Change and the Patron of Navigation
			20 - Ravion: God of Wilderness, The Hunt and the Patron of Hunting
			21 - Reiyat: Goddess of Rivers, Harmony and the Patron of Fishing

			22 - Thanoukos: God of Souls, Ghosts and the Patron of Graveyards
			23 - Suvadag: God of Lust, Seduction and the Patron of Brothels
			24 - Gouramet: God of Food, Satisfaction and the Patron of Cooking
			25 - Eaosin: Goddess of The Past, Memories and the Patron of Rememberance
			26 - Momina: Goddess of The Present, Choices and the Patron of Crossroads
			27 - Phaerin: Goddess of The Future, Hope and the Patron of Prayers
			28 - Varkis: God of Ore, Gems and the Patron of Mines
			29 - Endramia: Goddess of Childbirth, Innocence and the Patron of Doulas
			
			> """)
			if character_deity=="0":
				character_worship="None"
			elif character_deity=="1":
				character_worship="Belim"
			elif character_deity=="2":
				character_worship="Faren"
			elif character_deity=="3":
				character_worship="Kivena"
			elif character_deity=="4":
				character_worship="Movan"
			elif character_deity=="5":
				character_worship="Novia"
			elif character_deity=="6":
				character_worship="Valira"
			elif character_deity=="7":
				character_worship="Chronia"
			elif character_deity=="8":
				character_worship="Aurien"
			elif character_deity=="9":
				character_worship="Everia"
			elif character_deity=="10":
				character_worship="Ilisium"
			elif character_deity=="11":
				character_worship="Palitar"
			elif character_deity=="12":
				character_worship="Sharam"
			elif character_deity=="13":
				character_worship="Veelae"
			elif character_deity=="14":
				character_worship="Amiras"
			elif character_deity=="15":
				character_worship="Eretiad"
			elif character_deity=="16":
				character_worship="Hularik"
			elif character_deity=="17":
				character_worship="Muzio"
			elif character_deity=="18":
				character_worship="Oulana"
			elif character_deity=="19":
				character_worship="Quanir"
			elif character_deity=="20":
				character_worship="Ravion"
			elif character_deity=="21":
				character_worship="Reiyat"
			elif character_deity=="22":
				character_worship="Thanoukos"
			elif character_deity=="23":
				character_worship="Suvadag"
			elif character_deity=="24":
				character_worship="Gouramet"
			elif character_deity=="25":
				character_worship="Eaosin"
			elif character_deity=="26":
				character_worship="Momina"
			elif character_deity=="27":
				character_worship="Phaerin"
			elif character_deity=="28":
				character_worship="Varkis"
			elif character_deity=="29":
				character_worship="Endramia"
			else:
				print("Not a valid choice, try again")
		elif character_world=="Eloria - 15,000 BDT":
			character_deity=input("""
			If """+character_name+""" is pious, which deity do they prey to for guidance?
			If """+character_name+""" isn't pious, type 0.

			1 - Belim: God of Darkness, Death and Patron of Secrets
			2 - Faren: God of Earth, Nature and Patron of Crafts
			3 - Kivena: Goddess of Water, Oceans and Patron of Sailing
			4 - Movan: God of Fire, Spirit and Patron of Home
			5 - Novia: Goddess of Light, Life and Patron of Healing
			6 - Valira: Goddess of Air, Weather and Patron of Travel
			7 - Chronia: Goddess of Time and the Patron of History

			8 - Aurien: God of Dreams and Dawn
			9 - Everia: Goddess of Nightmares and Dusk
			10 - Ilisium: God of Ice and Winter
			11 - Palitar: Goddess of Plants and Spring
			12 - Sharam: Goddess of Volcanoes and Summer
			13 - Veelae: God of Storms and Autumn

			14 - Amiras: Goddess of Love, Family and the Patron of Marriage
			15 - Eretiad: God of Premonition, Belief and the Patron of Oracles
			16 - Hularik: God of War, Loyatly and the Patron of Brotherhood
			17 - Muzio: Goddess of Inspiration, Confidence and the Patron of The Arts
			18 - Oulana: Goddess of Domestication, The Harvest and the Patron of Farming
			19 - Quanir: God of Coasts, Change and the Patron of Navigation
			20 - Ravion: God of Wilderness, The Hunt and the Patron of Hunting
			21 - Reiyat: Goddess of Rivers, Harmony and the Patron of Fishing

			22 - Thanoukos: God of Souls, Ghosts and the Patron of Graveyards
			23 - Suvadag: God of Lust, Seduction and the Patron of Brothels
			24 - Gouramet: God of Food, Satisfaction and the Patron of Cooking
			25 - Eaosin: Goddess of The Past, Memories and the Patron of Rememberance
			26 - Momina: Goddess of The Present, Choices and the Patron of Crossroads
			27 - Phaerin: Goddess of The Future, Hope and the Patron of Prayers
			28 - Varkis: God of Ore, Gems and the Patron of Mines
			29 - Endramia: Goddess of Childbirth, Innocence and the Patron of Doulas
			30 - Inybo: God of Celebration, Intoxication and the Patron of Wine
			31 - Lanirida: Goddess of Flowers, Herbs and the Patron of Herbalists
			
			> """)
			if character_deity=="0":
				character_worship="None"
			elif character_deity=="1":
				character_worship="Belim"
			elif character_deity=="2":
				character_worship="Faren"
			elif character_deity=="3":
				character_worship="Kivena"
			elif character_deity=="4":
				character_worship="Movan"
			elif character_deity=="5":
				character_worship="Novia"
			elif character_deity=="6":
				character_worship="Valira"
			elif character_deity=="7":
				character_worship="Chronia"
			elif character_deity=="8":
				character_worship="Aurien"
			elif character_deity=="9":
				character_worship="Everia"
			elif character_deity=="10":
				character_worship="Ilisium"
			elif character_deity=="11":
				character_worship="Palitar"
			elif character_deity=="12":
				character_worship="Sharam"
			elif character_deity=="13":
				character_worship="Veelae"
			elif character_deity=="14":
				character_worship="Amiras"
			elif character_deity=="15":
				character_worship="Eretiad"
			elif character_deity=="16":
				character_worship="Hularik"
			elif character_deity=="17":
				character_worship="Muzio"
			elif character_deity=="18":
				character_worship="Oulana"
			elif character_deity=="19":
				character_worship="Quanir"
			elif character_deity=="20":
				character_worship="Ravion"
			elif character_deity=="21":
				character_worship="Reiyat"
			elif character_deity=="22":
				character_worship="Thanoukos"
			elif character_deity=="23":
				character_worship="Suvadag"
			elif character_deity=="24":
				character_worship="Gouramet"
			elif character_deity=="25":
				character_worship="Eaosin"
			elif character_deity=="26":
				character_worship="Momina"
			elif character_deity=="27":
				character_worship="Phaerin"
			elif character_deity=="28":
				character_worship="Varkis"
			elif character_deity=="29":
				character_worship="Endramia"
			elif character_deity=="30":
				character_worship="Inybo"
			elif character_deity=="31":
				character_worship="Lanirida"
			else:
				print("Not a valid choice, try again")
		elif character_world=="Eloria - 6,250 BDT":
			character_deity=input("""
			If """+character_name+"""is pious, which deity do they prey to for guidance?
			If """+character_name+""" isn't pious, type 0.

			1 - Belim: God of Darkness, Death and Patron of Secrets
			2 - Faren: God of Earth, Nature and Patron of Crafts
			3 - Kivena: Goddess of Water, Oceans and Patron of Sailing
			4 - Movan: God of Fire, Spirit and Patron of Home
			5 - Novia: Goddess of Light, Life and Patron of Healing
			6 - Valira: Goddess of Air, Weather and Patron of Travel
			7 - Chronia: Goddess of Time and the Patron of History

			8 - Aurien: God of Dreams and Dawn
			9 - Everia: Goddess of Nightmares and Dusk
			10 - Ilisium: God of Ice and Winter
			11 - Palitar: Goddess of Plants and Spring
			12 - Sharam: Goddess of Volcanoes and Summer
			13 - Veelae: God of Storms and Autumn

			14 - Amiras: Goddess of Love, Family and the Patron of Marriage
			15 - Eretiad: God of Premonition, Belief and the Patron of Oracles
			16 - Hularik: God of War, Loyatly and the Patron of Brotherhood
			17 - Muzio: Goddess of Inspiration, Confidence and the Patron of The Arts
			18 - Oulana: Goddess of Domestication, The Harvest and the Patron of Farming
			19 - Quanir: God of Coasts, Change and the Patron of Navigation
			20 - Ravion: God of Wilderness, The Hunt and the Patron of Hunting
			21 - Reiyat: Goddess of Rivers, Harmony and the Patron of Fishing

			22 - Thanoukos: God of Souls, Ghosts and the Patron of Graveyards
			23 - Suvadag: God of Lust, Seduction and the Patron of Brothels
			24 - Gouramet: God of Food, Satisfaction and the Patron of Cooking
			25 - Eaosin: Goddess of The Past, Memories and the Patron of Rememberance
			26 - Momina: Goddess of The Present, Choices and the Patron of Crossroads
			27 - Phaerin: Goddess of The Future, Hope and the Patron of Prayers
			28 - Varkis: God of Ore, Gems and the Patron of Mines
			29 - Endramia: Goddess of Childbirth, Innocence and the Patron of Doulas
			30 - Inybo: God of Celebration, Intoxication and the Patron of Wine
			31 - Lanirida: Goddess of Flowers, Herbs and the Patron of Herbalists
			32 - Oruphia: Goddess of Snow, Guidance and the Patron of Exploration
			33 - Moghai: Goddess of Animals, Instinct and the Patron of Beast Tamers
			34 - Triposia: Goddess of Tides, Abundance and the Patron of Reefs
			35 - Merriala: Goddess of Music, Songs and the Patron of Musicians
			
			> """)
			if character_deity=="0":
				character_worship="None"
			elif character_deity=="1":
				character_worship="Belim"
			elif character_deity=="2":
				character_worship="Faren"
			elif character_deity=="3":
				character_worship="Kivena"
			elif character_deity=="4":
				character_worship="Movan"
			elif character_deity=="5":
				character_worship="Novia"
			elif character_deity=="6":
				character_worship="Valira"
			elif character_deity=="7":
				character_worship="Chronia"
			elif character_deity=="8":
				character_worship="Aurien"
			elif character_deity=="9":
				character_worship="Everia"
			elif character_deity=="10":
				character_worship="Ilisium"
			elif character_deity=="11":
				character_worship="Palitar"
			elif character_deity=="12":
				character_worship="Sharam"
			elif character_deity=="13":
				character_worship="Veelae"
			elif character_deity=="14":
				character_worship="Amiras"
			elif character_deity=="15":
				character_worship="Eretiad"
			elif character_deity=="16":
				character_worship="Hularik"
			elif character_deity=="17":
				character_worship="Muzio"
			elif character_deity=="18":
				character_worship="Oulana"
			elif character_deity=="19":
				character_worship="Quanir"
			elif character_deity=="20":
				character_worship="Ravion"
			elif character_deity=="21":
				character_worship="Reiyat"
			elif character_deity=="22":
				character_worship="Thanoukos"
			elif character_deity=="23":
				character_worship="Suvadag"
			elif character_deity=="24":
				character_worship="Gouramet"
			elif character_deity=="25":
				character_worship="Eaosin"
			elif character_deity=="26":
				character_worship="Momina"
			elif character_deity=="27":
				character_worship="Phaerin"
			elif character_deity=="28":
				character_worship="Varkis"
			elif character_deity=="29":
				character_worship="Endramia"
			elif character_deity=="30":
				character_worship="Inybo"
			elif character_deity=="31":
				character_worship="Lanirida"
			elif character_deity=="32":
				character_worship="Oruphia"
			elif character_deity=="33":
				character_worship="Moghai"
			elif character_deity=="34":
				character_worship="Triposia"
			elif character_deity=="35":
				character_worship="Merriala"
			else:
				print("Not a valid choice, try again")
		elif character_world=="Eloria - 5,000 BDT" or "Eloria - 2,085 BDT":
			character_deity=input("""
			If """+character_name+""" is pious, which deity do they prey to for guidance?
			If """+character_name+""" isn't pious, type 0.

			1 - Belim: God of Darkness, Death and Patron of Secrets
			2 - Faren: God of Earth, Nature and Patron of Crafts
			3 - Kivena: Goddess of Water, Oceans and Patron of Sailing
			4 - Movan: God of Fire, Spirit and Patron of Home
			5 - Novia: Goddess of Light, Life and Patron of Healing
			6 - Valira: Goddess of Air, Weather and Patron of Travel
			7 - Chronia: Goddess of Time and the Patron of History

			8 - Aurien: God of Dreams and Dawn
			9 - Everia: Goddess of Nightmares and Dusk
			10 - Ilisium: God of Ice and Winter
			11 - Palitar: Goddess of Plants and Spring
			12 - Sharam: Goddess of Volcanoes and Summer
			13 - Veelae: God of Storms and Autumn

			14 - Amiras: Goddess of Love, Family and the Patron of Marriage
			15 - Eretiad: God of Premonition, Belief and the Patron of Oracles
			16 - Hularik: God of War, Loyatly and the Patron of Brotherhood
			17 - Muzio: Goddess of Inspiration, Confidence and the Patron of The Arts
			18 - Oulana: Goddess of Domestication, The Harvest and the Patron of Farming
			19 - Quanir: God of Coasts, Change and the Patron of Navigation
			20 - Ravion: God of Wilderness, The Hunt and the Patron of Hunting
			21 - Reiyat: Goddess of Rivers, Harmony and the Patron of Fishing

			22 - Thanoukos: God of Souls, Ghosts and the Patron of Graveyards
			23 - Suvadag: God of Lust, Seduction and the Patron of Brothels
			24 - Gouramet: God of Food, Satisfaction and the Patron of Cooking
			25 - Eaosin: Goddess of The Past, Memories and the Patron of Rememberance
			26 - Momina: Goddess of The Present, Choices and the Patron of Crossroads
			27 - Phaerin: Goddess of The Future, Hope and the Patron of Prayers
			28 - Varkis: God of Ore, Gems and the Patron of Mines
			29 - Endramia: Goddess of Childbirth, Innocence and the Patron of Doulas
			30 - Inybo: God of Celebration, Intoxication and the Patron of Wine
			31 - Lanirida: Goddess of Flowers, Herbs and the Patron of Herbalists
			32 - Oruphia: Goddess of Snow, Guidance and the Patron of Exploration
			33 - Moghai: Goddess of Animals, Instinct and the Patron of Beast Tamers
			34 - Triposia: Goddess of Tides, Abundance and the Patron of Reefs
			35 - Merriala: Goddess of Music, Songs and the Patron of Musicians
			36 - Sarek: God of The Deep, The Unknown and Patron of The Abyss
			37 - Ramira: Goddess of Communication, Languages and the Patron of Messengers
			
			> """)
			if character_deity=="0":
				character_worship="None"
			elif character_deity=="1":
				character_worship="Belim"
			elif character_deity=="2":
				character_worship="Faren"
			elif character_deity=="3":
				character_worship="Kivena"
			elif character_deity=="4":
				character_worship="Movan"
			elif character_deity=="5":
				character_worship="Novia"
			elif character_deity=="6":
				character_worship="Valira"
			elif character_deity=="7":
				character_worship="Chronia"
			elif character_deity=="8":
				character_worship="Aurien"
			elif character_deity=="9":
				character_worship="Everia"
			elif character_deity=="10":
				character_worship="Ilisium"
			elif character_deity=="11":
				character_worship="Palitar"
			elif character_deity=="12":
				character_worship="Sharam"
			elif character_deity=="13":
				character_worship="Veelae"
			elif character_deity=="14":
				character_worship="Amiras"
			elif character_deity=="15":
				character_worship="Eretiad"
			elif character_deity=="16":
				character_worship="Hularik"
			elif character_deity=="17":
				character_worship="Muzio"
			elif character_deity=="18":
				character_worship="Oulana"
			elif character_deity=="19":
				character_worship="Quanir"
			elif character_deity=="20":
				character_worship="Ravion"
			elif character_deity=="21":
				character_worship="Reiyat"
			elif character_deity=="22":
				character_worship="Thanoukos"
			elif character_deity=="23":
				character_worship="Suvadag"
			elif character_deity=="24":
				character_worship="Gouramet"
			elif character_deity=="25":
				character_worship="Eaosin"
			elif character_deity=="26":
				character_worship="Momina"
			elif character_deity=="27":
				character_worship="Phaerin"
			elif character_deity=="28":
				character_worship="Varkis"
			elif character_deity=="29":
				character_worship="Endramia"
			elif character_deity=="30":
				character_worship="Inybo"
			elif character_deity=="31":
				character_worship="Lanirida"
			elif character_deity=="32":
				character_worship="Oruphia"
			elif character_deity=="33":
				character_worship="Moghai"
			elif character_deity=="34":
				character_worship="Triposia"
			elif character_deity=="35":
				character_worship="Merriala"
			elif character_deity=="36":
				character_worship="Sarek"
			elif character_deity=="37":
				character_worship="Ramira"
			else:
				print("Not a valid choice, try again")
		elif character_world=="Eloria":
			character_deity=input("""
			If """+character_name+""" is pious, which deity do they prey to for guidance?
			If """+character_name+""" isn't pious, type 0.

			1 - Belim: God of Darkness, Death and Patron of Secrets
			2 - Faren: God of Earth, Nature and Patron of Crafts
			3 - Kivena: Goddess of Water, Oceans and Patron of Sailing
			4 - Movan: God of Fire, Spirit and Patron of Home
			5 - Novia: Goddess of Light, Life and Patron of Healing
			6 - Valira: Goddess of Air, Weather and Patron of Travel
			7 - Chronia: Goddess of Time and the Patron of History

			8 - Aurien: God of Dreams and Dawn
			9 - Everia: Goddess of Nightmares and Dusk
			10 - Ilisium: God of Ice and Winter
			11 - Palitar: Goddess of Plants and Spring
			12 - Sharam: Goddess of Volcanoes and Summer
			13 - Veelae: God of Storms and Autumn

			14 - Amiras: Goddess of Love, Family and the Patron of Marriage
			15 - Eretiad: God of Premonition, Belief and the Patron of Oracles
			16 - Hularik: God of War, Loyatly and the Patron of Brotherhood
			17 - Muzio: Goddess of Inspiration, Confidence and the Patron of The Arts
			18 - Oulana: Goddess of Domestication, The Harvest and the Patron of Farming
			19 - Quanir: God of Coasts, Change and the Patron of Navigation
			20 - Ravion: God of Wilderness, The Hunt and the Patron of Hunting
			21 - Reiyat: Goddess of Rivers, Harmony and the Patron of Fishing

			22 - Thanoukos: God of Souls, Ghosts and the Patron of Graveyards
			23 - Suvadag: God of Lust, Seduction and the Patron of Brothels
			24 - Gouramet: God of Food, Satisfaction and the Patron of Cooking
			25 - Eaosin: Goddess of The Past, Memories and the Patron of Rememberance
			26 - Momina: Goddess of The Present, Choices and the Patron of Crossroads
			27 - Phaerin: Goddess of The Future, Hope and the Patron of Prayers
			28 - Varkis: God of Ore, Gems and the Patron of Mines
			29 - Endramia: Goddess of Childbirth, Innocence and the Patron of Doulas
			30 - Inybo: God of Celebration, Intoxication and the Patron of Wine
			31 - Lanirida: Goddess of Flowers, Herbs and the Patron of Herbalists
			32 - Oruphia: Goddess of Snow, Guidance and the Patron of Exploration
			33 - Moghai: Goddess of Animals, Instinct and the Patron of Beast Tamers
			34 - Triposia: Goddess of Tides, Abundance and the Patron of Reefs
			35 - Merriala: Goddess of Music, Songs and the Patron of Musicians
			36 - Sarek: God of The Deep, The Unknown and Patron of The Abyss
			37 - Ramira: Goddess of Communication, Languages and the Patron of Messengers
			38 - Codronos: God of Age, Fatigue and the Patron of The Elderly
			39 - Zinix: Goddess of Fog, Illusions and the Patron of Thieves
			40 - Narshad: God of Chance, Luck and the Patron of Gambling
			41 - Alirade: Goddess of Rainbows, Auroras and the Patron of Beauty
			
			> """)
			if character_deity=="0":
				character_worship="None"
			elif character_deity=="1":
				character_worship="Belim"
			elif character_deity=="2":
				character_worship="Faren"
			elif character_deity=="3":
				character_worship="Kivena"
			elif character_deity=="4":
				character_worship="Movan"
			elif character_deity=="5":
				character_worship="Novia"
			elif character_deity=="6":
				character_worship="Valira"
			elif character_deity=="7":
				character_worship="Chronia"
			elif character_deity=="8":
				character_worship="Aurien"
			elif character_deity=="9":
				character_worship="Everia"
			elif character_deity=="10":
				character_worship="Ilisium"
			elif character_deity=="11":
				character_worship="Palitar"
			elif character_deity=="12":
				character_worship="Sharam"
			elif character_deity=="13":
				character_worship="Veelae"
			elif character_deity=="14":
				character_worship="Amiras"
			elif character_deity=="15":
				character_worship="Eretiad"
			elif character_deity=="16":
				character_worship="Hularik"
			elif character_deity=="17":
				character_worship="Muzio"
			elif character_deity=="18":
				character_worship="Oulana"
			elif character_deity=="19":
				character_worship="Quanir"
			elif character_deity=="20":
				character_worship="Ravion"
			elif character_deity=="21":
				character_worship="Reiyat"
			elif character_deity=="22":
				character_worship="Thanoukos"
			elif character_deity=="23":
				character_worship="Suvadag"
			elif character_deity=="24":
				character_worship="Gouramet"
			elif character_deity=="25":
				character_worship="Eaosin"
			elif character_deity=="26":
				character_worship="Momina"
			elif character_deity=="27":
				character_worship="Phaerin"
			elif character_deity=="28":
				character_worship="Varkis"
			elif character_deity=="29":
				character_worship="Endramia"
			elif character_deity=="30":
				character_worship="Inybo"
			elif character_deity=="31":
				character_worship="Lanirida"
			elif character_deity=="32":
				character_worship="Oruphia"
			elif character_deity=="33":
				character_worship="Moghai"
			elif character_deity=="34":
				character_worship="Triposia"
			elif character_deity=="35":
				character_worship="Merriala"
			elif character_deity=="36":
				character_worship="Sarek"
			elif character_deity=="37":
				character_worship="Ramira"
			else:
				print("Not a valid choice, try again")
		elif character_world=="Ta'bros":
			character_deity=input("""
			If """+character_name+""" is pious, which deity do they prey to for guidance?
			If """+character_name+""" isn't pious, type 0.

			1 - Emolat: Goddess of Darkness, Destruction and the Patron of Hunting
			2 - Rigath: God of Earth, The Forge and the Patron of Trade
			3 - Hurüsh: God of Air, Storms and the Patron of Vengeance
			4 - Magarab: Goddess of Fire, Chaos and the Patron of War
			5 - Inauri: Goddess of Water, Oceans and Patron of The Unknown
			
			> """)
			if character_deity=="0":
				character_worship="None"
			elif character_deity=="1":
				character_worship="Emolat"
			elif character_deity=="2":
				character_worship="Rigath"
			elif character_deity=="3":
				character_worship="Hurüsh"
			elif character_deity=="4":
				character_worship="Magarab"
			elif character_deity=="5":
				character_worship="Inauri"
			else:
				print("Not a valid choice, try again")
		elif character_world=="Unified":
			if character_race=="Vinori":
				character_deity=input("""
			Which deity does your tribe worship?

			1 - Elushaan: Goddess of Lust, Control and the Patron of Seduction
			2 - Gormis: God of Rage, Power and the Patron of War
			3 - Halis: God of Light, Fire and the Patron of The Sun
			4 - Ogrom: God of Animals, Earth and the Patron of Hunting
			5 - Shumid: God of Water, Tides and the Patron of Life
			6 - Tyamir: Goddess of Storms, Air and the Patron of Weather
			7 - Viran: Goddess of Fear, Night and the Patron of Death
			
			> """)
				if character_deity=="1":
					character_worship="Elushaan"
				elif character_deity=="2":
					character_worship="Gormis"
				elif character_deity=="3":
					character_worship="Halis"
				elif character_deity=="4":
					character_worship="Ogrom"
				elif character_deity=="5":
					character_worship="Shumid"
				elif character_deity=="6":
					character_worship="Tyamir"
				elif character_deity=="7":
					character_worship="Viran"
				else:
					print("Not a valid choice, try again")
			else:
				character_deity=input("""
			If """+character_name+""" is pious, which deity do they prey to for guidance?
			If """+character_name+""" isn't pious, type 0.

			1 - Rigath: God of Earth, The Forge and the Patron of Trade
			2 - Inauri: Goddess of Water, Oceans and the Patron of The Unknown
			
			3 - Belim: God of Darkness, Death and Patron of Secrets
			4 - Faren: God of Earth, Nature and Patron of Crafts
			5 - Kivena: Goddess of Water, Oceans and Patron of Sailing
			6 - Movan: God of Fire, Spirit and Patron of Home
			7 - Novia: Goddess of Light, Life and Patron of Healing
			8 - Valira: Goddess of Air, Weather and Patron of Travel
			9 - Chronia: Goddess of Time and the Patron of History

			10 - Aurien: God of Dreams and Dawn
			11 - Everia: Goddess of Nightmares and Dusk
			12 - Ilisium: God of Ice and Winter
			13 - Palitar: Goddess of Plants and Spring
			14 - Sharam: Goddess of Volcanoes and Summer
			15 - Veelae: God of Storms and Autumn

			16 - Amiras: Goddess of Love, Family and the Patron of Marriage
			17 - Eretiad: God of Premonition, Belief and the Patron of Oracles
			18 - Hularik: God of War, Loyatly and the Patron of Brotherhood
			19 - Muzio: Goddess of Inspiration, Confidence and the Patron of The Arts
			20 - Oulana: Goddess of Domestication, The Harvest and the Patron of Farming
			21 - Quanir: God of Coasts, Change and the Patron of Navigation
			22 - Ravion: God of Wilderness, The Hunt and the Patron of Hunting
			23 - Reiyat: Goddess of Rivers, Harmony and the Patron of Fishing
			
			24 - Thanoukos: God of Souls, Ghosts and the Patron of Graveyards
			25 - Suvadag: God of Lust, Seduction and the Patron of Brothels
			26 - Gouramet: God of Food, Satisfaction and the Patron of Cooking
			27 - Eaosin: Goddess of The Past, Memories and the Patron of Rememberance
			28 - Momina: Goddess of The Present, Choices and the Patron of Crossroads
			29 - Phaerin: Goddess of The Future, Hope and the Patron of Prayers
			30 - Varkis: God of Ore, Gems and the Patron of Mines
			31 - Endramia: Goddess of Childbirth, Innocence and the Patron of Doulas
			32 - Inybo: God of Celebration, Intoxication and the Patron of Wine
			33 - Lanirida: Goddess of Flowers, Herbs and the Patron of Herbalists
			34 - Oruphia: Goddess of Snow, Guidance and the Patron of Exploration
			35 - Moghai: Goddess of Animals, Instinct and the Patron of Beast Tamers
			36 - Triposia: Goddess of Tides, Abundance and the Patron of Reefs
			37 - Ramira: Goddess of Communication, Languages and the Patron of Messengers
			38 - Merriala: Goddess of Music, Songs and the Patron of Musicians
			39 - Sarek: God of The Deep, The Unknown and Patron of The Abyss
			40 - Codronos: God of Age, Fatigue and the Patron of The Elderly
			41 - Zinix: Goddess of Fog, Illusions and the Patron of Thieves
			42 - Narshad: God of Chance, Luck and the Patron of Gambling
			43 - Alirade: Goddess of Rainbows, Auroras and the Patron of Beauty
			44 - Tylia: Goddess of Diplomacy, Cooperation and the Patron of Translation
			45 - Elos: God of Light, Stars and the Patron of Hope
			46 - Ryali: Goddess of Flowers, Herbs and the Patron of Love
			47 - Nytris: Goddess of Justice, Judgement and the Patron of Freedom
			48 - Nemina: Goddess of Revenge, Punishment and the Patron of Imprisonment
			49 - Igran: God of Tactics, Strategy and the PAtron of Cartographers
			50 - Derisha: Goddess of Performance, Entertainment and the Patron of The Theatre
			51 - Kromar: God of Protection, Shelter and the Patron of Home
			
			> """)
				if character_deity=="0":
					character_worship="None"
				elif character_deity=="1":
					character_worship="Rigath"
				elif character_deity=="2":
					character_worship="Inauri"
				elif character_deity=="3":
					character_worship="Belim"
				elif character_deity=="4":
					character_worship="Faren"
				elif character_deity=="5":
					character_worship="Kivena"
				elif character_deity=="6":
					character_worship="Movan"
				elif character_deity=="7":
					character_worship="Novia"
				elif character_deity=="8":
					character_worship="Valira"
				elif character_deity=="9":
					character_worship="Chronia"
				elif character_deity=="10":
					character_worship="Aurien"
				elif character_deity=="11":
					character_worship="Everia"
				elif character_deity=="12":
					character_worship="Ilisium"
				elif character_deity=="13":
					character_worship="Palitar"
				elif character_deity=="14":
					character_worship="Sharam"
				elif character_deity=="15":
					character_worship="Veelae"
				elif character_deity=="16":
					character_worship="Amiras"
				elif character_deity=="17":
					character_worship="Eretiad"
				elif character_deity=="18":
					character_worship="Hularik"
				elif character_deity=="19":
					character_worship="Muzio"
				elif character_deity=="20":
					character_worship="Oulana"
				elif character_deity=="21":
					character_worship="Quanir"
				elif character_deity=="22":
					character_worship="Ravion"
				elif character_deity=="23":
					character_worship="Reiyat"
				elif character_deity=="24":
					character_worship="Thanoukos"
				elif character_deity=="25":
					character_worship="Suvadag"
				elif character_deity=="26":
					character_worship="Gouramet"
				elif character_deity=="27":
					character_worship="Eaosin"
				elif character_deity=="28":
					character_worship="Momina"
				elif character_deity=="29":
					character_worship="Phaerin"
				elif character_deity=="30":
					character_worship="Varkis"
				elif character_deity=="31":
					character_worship="Endramia"
				elif character_deity=="32":
					character_worship="Inybo"
				elif character_deity=="33":
					character_worship="Lanirida"
				elif character_deity=="34":
					character_worship="Oruphia"
				elif character_deity=="35":
					character_worship="Moghai"
				elif character_deity=="36":
					character_worship="Triposia"
				elif character_deity=="37":
					character_worship="Ramira"
				elif character_deity=="38":
					character_worship="Merriala"
				elif character_deity=="39":
					character_worship="Sarek"
				elif character_deity=="40":
					character_worship="Codronos"
				elif character_deity=="41":
					character_worship="Zinix"
				elif character_deity=="42":
					character_worship="Narshad"
				elif character_deity=="43":
					character_worship="Alirade"
				elif character_deity=="44":
					character_worship="Tylia"
				elif character_deity=="45":
					character_worship="Elos"
				elif character_deity=="46":
					character_worship="Ryali"
				elif character_deity=="47":
					character_worship="Nytris"
				elif character_deity=="48":
					character_worship="Nemina"
				elif character_deity=="49":
					character_worship="Igran"
				elif character_deity=="50":
					character_worship="Derisha"
				elif character_deity=="51":
					character_worship="Kromar"
				else:
					print("Not a valid choice, try again")
		elif character_world=="Post-Unification":
			character_deity=input("""
			If """+character_name+""" is pious, which deity do they prey to for guidance?
			If """+character_name+""" isn't pious, type 0.

			1 - Rigath: God of Earth, The Forge and the Patron of Trade
			2 - Inauri: Goddess of Water, Oceans and the Patron of The Unknown
			
			3 - Belim: God of Darkness, Death and Patron of Secrets
			4 - Faren: God of Earth, Nature and Patron of Crafts
			5 - Kivena: Goddess of Water, Oceans and Patron of Sailing
			6 - Movan: God of Fire, Spirit and Patron of Home
			7 - Novia: Goddess of Light, Life and Patron of Healing
			8 - Valira: Goddess of Air, Weather and Patron of Travel
			9 - Chronia: Goddess of Time and the Patron of History

			10 - Aurien: God of Dreams and Dawn
			11 - Everia: Goddess of Nightmares and Dusk
			12 - Ilisium: God of Ice and Winter
			13 - Palitar: Goddess of Plants and Spring
			14 - Sharam: Goddess of Volcanoes and Summer
			15 - Veelae: God of Storms and Autumn

			16 - Amiras: Goddess of Love, Family and the Patron of Marriage
			17 - Eretiad: God of Premonition, Belief and the Patron of Oracles
			18 - Hularik: God of War, Loyatly and the Patron of Brotherhood
			19 - Muzio: Goddess of Inspiration, Confidence and the Patron of The Arts
			20 - Oulana: Goddess of Domestication, The Harvest and the Patron of Farming
			21 - Quanir: God of Coasts, Change and the Patron of Navigation
			22 - Ravion: God of Wilderness, The Hunt and the Patron of Hunting
			23 - Reiyat: Goddess of Rivers, Harmony and the Patron of Fishing
			
			24 - Thanoukos: God of Souls, Ghosts and the Patron of Graveyards
			25 - Kurex: God of Betrayal, Trickery and the Patron of Traitors
			26 - Gouramet: God of Food, Satisfaction and the Patron of Cooking
			27 - Eaosin: Goddess of The Past, Memories and the Patron of Rememberance
			28 - Momina: Goddess of The Present, Choices and the Patron of Crossroads
			29 - Phaerin: Goddess of The Future, Hope and the Patron of Prayers
			30 - Varkis: God of Ore, Gems and the Patron of Mines
			31 - Endramia: Goddess of Childbirth, Innocence and the Patron of Doulas
			32 - Inybo: God of Celebration, Intoxication and the Patron of Wine
			33 - Lanirida: Goddess of Flowers, Herbs and the Patron of Herbalists
			34 - Oruphia: Goddess of Snow, Guidance and the Patron of Exploration
			35 - Moghai: Goddess of Animals, Instinct and the Patron of Beast Tamers
			36 - Triposia: Goddess of Tides, Abundance and the Patron of Reefs
			37 - Merriala: Goddess of Music, Songs and the Patron of Musicians
			38 - Sarek: God of The Deep, The Unknown and Patron of The Abyss
			39 - Codronos: God of Age, Fatigue and the Patron of The Elderly
			40 - Zinix: Goddess of Fog, Illusions and the Patron of Thieves
			41 - Narshad: God of Chance, Luck and the Patron of Gambling
			42 - Alirade: Goddess of Rainbows, Auroras and the Patron of Beauty
			43 - Tylia: Goddess of Diplomacy, Communication and the Patron of Messengers
			44 - Elos: God of Light, Stars and the Patron of Hope
			45 - Ryali: Goddess of Flowers, Herbs and the Patron of Love
			46 - Nytris: Goddess of Justice, Judgement and the Patron of Freedom
			47 - Nemina: Goddess of Revenge, Punishment and the Patron of Imprisonment
			48 - Igran: God of Tactics, Strategy and the Patron of Cartographers
			49 - Derisha: Goddess of Performance, Entertainment and the Patron of The Theatre
			50 - Kromar: God of Protection, Shelter and the Patron of Home
			
			> """)
			if character_deity=="0":
				character_worship="None"
			elif character_deity=="1":
				character_worship="Rigath"
			elif character_deity=="2":
				character_worship="Inauri"
			elif character_deity=="3":
				character_worship="Belim"
			elif character_deity=="4":
				character_worship="Faren"
			elif character_deity=="5":
				character_worship="Kivena"
			elif character_deity=="6":
				character_worship="Movan"
			elif character_deity=="7":
				character_worship="Novia"
			elif character_deity=="8":
				character_worship="Valira"
			elif character_deity=="9":
				character_worship="Chronia"
			elif character_deity=="10":
				character_worship="Aurien"
			elif character_deity=="11":
				character_worship="Everia"
			elif character_deity=="12":
				character_worship="Ilisium"
			elif character_deity=="13":
				character_worship="Palitar"
			elif character_deity=="14":
				character_worship="Sharam"
			elif character_deity=="15":
				character_worship="Veelae"
			elif character_deity=="16":
				character_worship="Amiras"
			elif character_deity=="17":
				character_worship="Eretiad"
			elif character_deity=="18":
				character_worship="Hularik"
			elif character_deity=="19":
				character_worship="Muzio"
			elif character_deity=="20":
				character_worship="Oulana"
			elif character_deity=="21":
				character_worship="Quanir"
			elif character_deity=="22":
				character_worship="Ravion"
			elif character_deity=="23":
				character_worship="Reiyat"
			elif character_deity=="24":
				character_worship="Thanoukos"
			elif character_deity=="25":
				character_worship="Kurex"
			elif character_deity=="26":
				character_worship="Gouramet"
			elif character_deity=="27":
				character_worship="Eaosin"
			elif character_deity=="28":
				character_worship="Momina"
			elif character_deity=="29":
				character_worship="Phaerin"
			elif character_deity=="30":
				character_worship="Varkis"
			elif character_deity=="31":
				character_worship="Endramia"
			elif character_deity=="32":
				character_worship="Inybo"
			elif character_deity=="33":
				character_worship="Lanirida"
			elif character_deity=="34":
				character_worship="Oruphia"
			elif character_deity=="35":
				character_worship="Moghai"
			elif character_deity=="36":
				character_worship="Triposia"
			elif character_deity=="37":
				character_worship="Merriala"
			elif character_deity=="38":
				character_worship="Sarek"
			elif character_deity=="39":
				character_worship="Codronos"
			elif character_deity=="40":
				character_worship="Zinix"
			elif character_deity=="41":
				character_worship="Narshad"
			elif character_deity=="42":
				character_worship="Alirade"
			elif character_deity=="43":
				character_worship="Tylia"
			elif character_deity=="44":
				character_worship="Elos"
			elif character_deity=="45":
				character_worship="Ryali"
			elif character_deity=="46":
				character_worship="Nytris"
			elif character_deity=="47":
				character_worship="Nemina"
			elif character_deity=="48":
				character_worship="Igran"
			elif character_deity=="49":
				character_worship="Derisha"
			elif character_deity=="50":
				character_worship="Kromar"
			else:
				print("Not a valid choice, try again")
		elif character_world=="Restricted":
			character_worship="None"

	global character_class, magic_type, mage_worship, race_worship, character_manalevel, character_spells
	while character_class is None:
		if character_race=="Faerie":
			class_choice=input("""
			Choose your character class from the list below by entering the relevant number:
			1 - Warrior
			2 - Mage
			3 - Scout
			4 - Defender
			5 - Non-Combatant

			> """)
			if class_choice=="1":
				character_class="Warrior"
			elif class_choice=="2":
				character_class="Mage"
			elif class_choice=="3":
				character_class="Scout"
			elif class_choice=="4":
				character_class="Defender"
			elif class_choice=="5":
				character_class="Non-Combatant"
			else:
				print("Not a valid choice, try again")
		
		elif character_race=="Giant":
			class_choice=input("""
			Choose your character class from the list below by entering the relevant number:
			1 - Warrior
			2 - Defender
			
			> """)
			if class_choice=="1":
				character_class="Warrior"
			elif class_choice=="2":
				character_class="Defender"
			else:
				print("Not a valid choice, try again")

		elif character_race=="Golem":
			if character_subrace=="Wood Golem":
				character_class="Mage"
			else:
				class_choice=input("""
				Choose your character class from the list below by entering the relevant number:
				1 - Warrior
				2 - Scout
				3 - Defender
				4 - Non-Combatant

				> """)
				if class_choice=="1":
					character_class="Warrior"
				elif class_choice=="2":
					character_class="Scout"
				elif class_choice=="3":
					character_class="Defender"
				elif class_choice=="4":
					character_class="Non-Combatant"
				else:
					print("Not a valid choice, try again")

		elif character_race=="Talis":
			class_choice=input("""
			Choose your character class from the list below by entering the relevant number:
			1 - Warrior
			2 - Mage
			3 - Scout
			4 - Defender
			5 - Non-Combatant

			> """)
			if character_subrace=="Air Talis":
				race_worship="Valira"
			elif character_subrace=="Dark Talis":
				race_worship="Belim"
			elif character_subrace=="Earth Talis":
				race_worship="Faren"
			elif character_subrace=="Fire Talis":
				race_worship="Movan"
			elif character_subrace=="Light Talis":
				race_worship="Novia"
			elif character_subrace=="Water Talis":
				race_worship="Kivena"
			if class_choice=="1":
				character_class="Warrior"
			elif class_choice=="2":
				character_class="Mage"
			elif class_choice=="3":
				character_class="Scout"
			elif class_choice=="4":
				character_class="Defender"
			elif class_choice=="5":
				character_class="Non-Combatant"
			else:
				print("Not a valid choice, try again")

		elif character_subrace=="Yellow Carapace":
			class_choice=input("""
			Choose your character class from the list below by entering the relevant number:
			1 - Warrior
			2 - Mage
			3 - Scout
			4 - Defender
			5 - Non-Combatant

			> """)
			if class_choice=="1":
				character_class="Warrior"
			elif class_choice=="2":
				character_class="Mage"
			elif class_choice=="3":
				character_class="Scout"
			elif class_choice=="4":
				character_class="Defender"
			elif class_choice=="5":
				character_class="Non-Combatant"
			else:
				print("Not a valid choice, try again")

		elif character_race=="Waheela":
			class_choice=input("""
			Choose your character class from the list below by entering the relevant number:
			1 - Warrior
			2 - Mage
			3 - Defender

			> """)
			race_worship="Inauri"
			if class_choice=="1":
				character_class="Warrior"
			elif class_choice=="2":
				character_class="Mage"
			elif class_choice=="3":
				character_class="Defender"
			else:
				print("Not a valid choice, try again")

		elif character_race=="Yuki-Ona":
			class_choice=input("""
			Choose your character class from the list below by entering the relevant number:
			1 - Warrior
			2 - Mage
			3 - Scout
			4 - Defender
			5 - Non-Combatant

			> """)
			race_worship="Ilisium"
			if class_choice=="1":
				character_class="Warrior"
			elif class_choice=="2":
				character_class="Mage"
			elif class_choice=="3":
				character_class="Scout"
			elif class_choice=="4":
				character_class="Defender"
			elif class_choice=="5":
				character_class="Non-Combatant"
			else:
				print("Not a valid choice, try again")

		else:
			roll=randint(1,20)
			if character_world=="Restricted" or roll<15:
				class_choice=input("""
					Choose your character class from the list below by entering the relevant number:
					1 - Warrior
					2 - Scout
					3 - Defender
					4 - Non-Combatant

					> """)
				if class_choice=="1":
					character_class="Warrior"
				elif class_choice=="2":
					character_class="Scout"
				elif class_choice=="3":
					character_class="Defender"
				elif class_choice=="4":
					character_class="Non-Combatant"
				else:
					print("Not a valid choice, try again")
			else:
					class_choice=input("""
					Choose your character class from the list below by entering the relevant number:
					1 - Warrior
					2 - Mage
					3 - Scout
					4 - Defender
					5 - Non-Combatant

					> """)
					if class_choice=="1":
						character_class="Warrior"
					elif class_choice=="2":
						character_class="Mage"
					elif class_choice=="3":
						character_class="Scout"
					elif class_choice=="4":
						character_class="Defender"
					elif class_choice=="5":
						character_class="Non-Combatant"
					else:
						print("Not a valid choice, try again")
		
		if character_class=="Mage":
			if character_world=="Primal Eloria":
				if character_race=="Talis":
					magic_type=""
					mage_worship=""
				elif character_race=="Faerie":
					magic_type=""
					mage_worship=""
				else:
					magic_choice=input("""
					Please choose which deity you wish to worship, which will determine your magic type, by entering the relevant number:
					1 - Belim - Darkness & Death, Patron Deity of Secrets (Dark Magic)
					2 - Faren - Earth & Nature, Patron Deity of Crafts (Earth Magic)
					3 - Kivena - Water & Oceans, Patron Deity of Sailing (Water Magic)
					4 - Movan - Fire & Spirit, Patron Deity of Home (Fire Magic)
					5 - Novia - Light & Life, Patron Deity of Healing (Light Magic)
					6 - Valira - Air & Weather, Patron Deity of Travel (Air Magic)
				
					> """)
					if magic_choice=="1":
						magic_type="Dark"
						mage_worship="Belim"
					elif magic_choice=="2":
						magic_type="Earth"
						mage_worship="Faren"
					elif magic_choice=="3":
						magic_type="Water"
						mage_worship="Kivena"
					elif magic_choice=="4":
						magic_type="Fire"
						mage_worship="Movan"
					elif magic_choice=="5":
						magic_type="Light"
						mage_worship="Novia"
					elif magic_choice=="6":
						magic_type="Air"
						mage_worship="Valira"
					else:
						print("Not a valid choice, try again")
			elif character_world=="Eloria - 175,000 BDT":
				if character_race=="Talis":
					magic_type=""
					mage_worship=""
				elif character_race=="Faerie":
					magic_type=""
					mage_worship=""
				else:
					magic_choice=input("""
					Please choose which deity you wish to worship, which will determine your magic type, by entering the relevant number:
					1 - Belim - Darkness & Death, Patron Deity of Secrets (Dark Magic)
					2 - Faren - Earth & Nature, Patron Deity of Crafts (Earth Magic)
					3 - Kivena - Water & Oceans, Patron Deity of Sailing (Water Magic)
					4 - Movan - Fire & Spirit, Patron Deity of Home (Fire Magic)
					5 - Novia - Light & Life, Patron Deity of Healing (Light Magic)
					6 - Valira - Air & Weather, Patron Deity of Travel (Air Magic)
				
					> """)
					if magic_choice=="1":
						magic_type="Dark"
						mage_worship="Belim"
					elif magic_choice=="2":
						magic_type="Earth"
						mage_worship="Faren"
					elif magic_choice=="3":
						magic_type="Water"
						mage_worship="Kivena"
					elif magic_choice=="4":
						magic_type="Fire"
						mage_worship="Movan"
					elif magic_choice=="5":
						magic_type="Light"
						mage_worship="Novia"
					elif magic_choice=="6":
						magic_type="Air"
						mage_worship="Valira"
					else:
						print("Not a valid choice, try again")
			elif character_world=="Eloria - 156,900 BDT":
				if character_race=="Talis":
					magic_type=""
					mage_worship=""
				elif character_race=="Faerie":
					magic_type=""
					mage_worship=""
				else:
					magic_choice=input("""
					Please choose which deity you wish to worship, which will determine your magic type, by entering the relevant number:
					1 - Belim - Darkness & Death, Patron Deity of Secrets (Dark Magic)
					2 - Faren - Earth & Nature, Patron Deity of Crafts (Earth Magic)
					3 - Kivena - Water & Oceans, Patron Deity of Sailing (Water Magic)
					4 - Movan - Fire & Spirit, Patron Deity of Home (Fire Magic)
					5 - Novia - Light & Life, Patron Deity of Healing (Light Magic)
					6 - Valira - Air & Weather, Patron Deity of Travel (Air Magic)
				
					> """)
					if magic_choice=="1":
						magic_type="Dark"
						mage_worship="Belim"
					elif magic_choice=="2":
						magic_type="Earth"
						mage_worship="Faren"
					elif magic_choice=="3":
						magic_type="Water"
						mage_worship="Kivena"
					elif magic_choice=="4":
						magic_type="Fire"
						mage_worship="Movan"
					elif magic_choice=="5":
						magic_type="Light"
						mage_worship="Novia"
					elif magic_choice=="6":
						magic_type="Air"
						mage_worship="Valira"
					else:
						print("Not a valid choice, try again")
			elif character_world=="Eloria - 100,000 BDT":
				if character_race=="Talis":
					magic_type=""
					mage_worship=""
				elif character_race=="Faerie":
					magic_type=""
					mage_worship=""
				elif character_subrace=="Wood Golem":
					magic_type=""
					mage_worship=""
				else:
					magic_choice=input("""
					Please choose which deity you wish to worship, which will determine your magic type, by entering the relevant number:
					1 - Belim - Darkness & Death, Patron Deity of Secrets (Dark Magic)
					2 - Faren - Earth & Nature, Patron Deity of Crafts (Earth Magic)
					3 - Kivena - Water & Oceans, Patron Deity of Sailing (Water Magic)
					4 - Movan - Fire & Spirit, Patron Deity of Home (Fire Magic)
					5 - Novia - Light & Life, Patron Deity of Healing (Light Magic)
					6 - Valira - Air & Weather, Patron Deity of Travel (Air Magic)
				
					> """)
					if magic_choice=="1":
						magic_type="Dark"
						mage_worship="Belim"
					elif magic_choice=="2":
						magic_type="Earth"
						mage_worship="Faren"
					elif magic_choice=="3":
						magic_type="Water"
						mage_worship="Kivena"
					elif magic_choice=="4":
						magic_type="Fire"
						mage_worship="Movan"
					elif magic_choice=="5":
						magic_type="Light"
						mage_worship="Novia"
					elif magic_choice=="6":
						magic_type="Air"
						mage_worship="Valira"
					else:
						print("Not a valid choice, try again")
			elif character_world=="Eloria - 15,000 BDT":
				if character_race=="Talis":
					magic_type=""
					mage_worship=""
				elif character_race=="Faerie":
					magic_type=""
					mage_worship=""
				elif character_subrace=="Wood Golem":
					magic_type=""
					mage_worship=""
				else:
					magic_choice=input("""
					Please choose which deity you wish to worship, which will determine your magic type, by entering the relevant number:
					1 - Belim - Darkness & Death, Patron Deity of Secrets (Dark Magic)
					2 - Faren - Earth & Nature, Patron Deity of Crafts (Earth Magic)
					3 - Kivena - Water & Oceans, Patron Deity of Sailing (Water Magic)
					4 - Movan - Fire & Spirit, Patron Deity of Home (Fire Magic)
					5 - Novia - Light & Life, Patron Deity of Healing (Light Magic)
					6 - Valira - Air & Weather, Patron Deity of Travel (Air Magic)
				
					> """)
					if magic_choice=="1":
						magic_type="Dark"
						mage_worship="Belim"
					elif magic_choice=="2":
						magic_type="Earth"
						mage_worship="Faren"
					elif magic_choice=="3":
						magic_type="Water"
						mage_worship="Kivena"
					elif magic_choice=="4":
						magic_type="Fire"
						mage_worship="Movan"
					elif magic_choice=="5":
						magic_type="Light"
						mage_worship="Novia"
					elif magic_choice=="6":
						magic_type="Air"
						mage_worship="Valira"
					else:
						print("Not a valid choice, try again")
			elif character_world=="Eloria - 6,250 BDT":
				if character_race=="Talis":
					magic_type=""
					mage_worship=""
				elif character_race=="Faerie":
					magic_type=""
					mage_worship=""
				elif character_subrace=="Wood Golem":
					magic_type=""
					mage_worship=""
				else:
					magic_choice=input("""
					Please choose which deity you wish to worship, which will determine your magic type, by entering the relevant number:
					1 - Belim - Darkness & Death, Patron Deity of Secrets (Dark Magic)
					2 - Faren - Earth & Nature, Patron Deity of Crafts (Earth Magic)
					3 - Kivena - Water & Oceans, Patron Deity of Sailing (Water Magic)
					4 - Movan - Fire & Spirit, Patron Deity of Home (Fire Magic)
					5 - Novia - Light & Life, Patron Deity of Healing (Light Magic)
					6 - Valira - Air & Weather, Patron Deity of Travel (Air Magic)
				
					> """)
					if magic_choice=="1":
						magic_type="Dark"
						mage_worship="Belim"
					elif magic_choice=="2":
						magic_type="Earth"
						mage_worship="Faren"
					elif magic_choice=="3":
						magic_type="Water"
						mage_worship="Kivena"
					elif magic_choice=="4":
						magic_type="Fire"
						mage_worship="Movan"
					elif magic_choice=="5":
						magic_type="Light"
						mage_worship="Novia"
					elif magic_choice=="6":
						magic_type="Air"
						mage_worship="Valira"
					else:
						print("Not a valid choice, try again")
			elif character_world=="Eloria - 5,000 BDT":
				if character_race=="Talis":
					magic_type=""
					mage_worship=""
				elif character_race=="Faerie":
					magic_type=""
					mage_worship=""
				elif character_subrace=="Wood Golem":
					magic_type=""
					mage_worship=""
				else:
					magic_choice=input("""
					Please choose which deity you wish to worship, which will determine your magic type, by entering the relevant number:
					1 - Belim - Darkness & Death, Patron Deity of Secrets (Dark Magic)
					2 - Faren - Earth & Nature, Patron Deity of Crafts (Earth Magic)
					3 - Kivena - Water & Oceans, Patron Deity of Sailing (Water Magic)
					4 - Movan - Fire & Spirit, Patron Deity of Home (Fire Magic)
					5 - Novia - Light & Life, Patron Deity of Healing (Light Magic)
					6 - Valira - Air & Weather, Patron Deity of Travel (Air Magic)
				
					> """)
					if magic_choice=="1":
						magic_type="Dark"
						mage_worship="Belim"
					elif magic_choice=="2":
						magic_type="Earth"
						mage_worship="Faren"
					elif magic_choice=="3":
						magic_type="Water"
						mage_worship="Kivena"
					elif magic_choice=="4":
						magic_type="Fire"
						mage_worship="Movan"
					elif magic_choice=="5":
						magic_type="Light"
						mage_worship="Novia"
					elif magic_choice=="6":
						magic_type="Air"
						mage_worship="Valira"
					else:
						print("Not a valid choice, try again")
			elif character_world=="Eloria - 2,085 BDT":
				if character_race=="Talis":
					magic_type=""
					mage_worship=""
				elif character_race=="Faerie":
					magic_type=""
					mage_worship=""
				elif character_subrace=="Wood Golem":
					magic_type=""
					mage_worship=""
				else:
					magic_choice=input("""
					Please choose which deity you wish to worship, which will determine your magic type, by entering the relevant number:
					1 - Belim - Darkness & Death, Patron Deity of Secrets (Dark Magic)
					2 - Faren - Earth & Nature, Patron Deity of Crafts (Earth Magic)
					3 - Kivena - Water & Oceans, Patron Deity of Sailing (Water Magic)
					4 - Movan - Fire & Spirit, Patron Deity of Home (Fire Magic)
					5 - Novia - Light & Life, Patron Deity of Healing (Light Magic)
					6 - Valira - Air & Weather, Patron Deity of Travel (Air Magic)
				
					> """)
					if magic_choice=="1":
						magic_type="Dark"
						mage_worship="Belim"
					elif magic_choice=="2":
						magic_type="Earth"
						mage_worship="Faren"
					elif magic_choice=="3":
						magic_type="Water"
						mage_worship="Kivena"
					elif magic_choice=="4":
						magic_type="Fire"
						mage_worship="Movan"
					elif magic_choice=="5":
						magic_type="Light"
						mage_worship="Novia"
					elif magic_choice=="6":
						magic_type="Air"
						mage_worship="Valira"
					else:
						print("Not a valid choice, try again")
			elif character_world=="Eloria":
				if character_race=="Talis":
					magic_type=""
					mage_worship=""
				elif character_subrace=="Wood Golem":
					magic_type=""
					mage_worship=""
				elif character_race=="Faerie":
					magic_type=""
					mage_worship=""
				else:
					magic_choice=input("""
					Please choose which deity you wish to worship, which will determine your magic type, by entering the relevant number:
					1 - Belim - Darkness & Death, Patron Deity of Secrets (Dark Magic)
					2 - Faren - Earth & Nature, Patron Deity of Crafts (Earth Magic)
					3 - Kivena - Water & Oceans, Patron Deity of Sailing (Water Magic)
					4 - Movan - Fire & Spirit, Patron Deity of Home (Fire Magic)
					5 - Novia - Light & Life, Patron Deity of Healing (Light Magic)
					6 - Valira - Air & Weather, Patron Deity of Travel (Air Magic)
				
					> """)
					if magic_choice=="1":
						magic_type="Dark"
						mage_worship="Belim"
					elif magic_choice=="2":
						magic_type="Earth"
						mage_worship="Faren"
					elif magic_choice=="3":
						magic_type="Water"
						mage_worship="Kivena"
					elif magic_choice=="4":
						magic_type="Fire"
						mage_worship="Movan"
					elif magic_choice=="5":
						magic_type="Light"
						mage_worship="Novia"
					elif magic_choice=="6":
						magic_type="Air"
						mage_worship="Valira"
					else:
						print("Not a valid choice, try again")
			elif character_world=="Primal Ta'bros":
				if character_race=="Waheela":
					magic_type=""
					mage_worship=""
				elif character_race=="Imp":
					magic_type=""
					mage_worship=""
				else:
					magic_choice=input("""
					Please choose which deity you wish to worship, which will determine your magic type, by entering the relevant number:
					1 - Emolat - Darkness & Destruction, Patron Deity of Hunting (Dark Magic)
					2 - Rigath - Earth & The Forge, Patron Deity of Trading (Earth Magic)
					3 - Hurüsh - Air & Storms, Patron Deity of Vengeance (Air Magic)
					4 - Magarab - Fire & Chaos, Patron Deity of War (Fire Magic)
					5 - Inauri - Water & Oceans, Patron Deity of The Unknown (Water Magic)
					
					> """)
					if magic_choice=="1":
						magic_type="Dark"
						mage_worship="Emolat"
					elif magic_choice=="2":
						magic_type="Earth"
						mage_worship="Rigath"
					elif magic_choice=="3":
						magic_type="Air"
						mage_worship="Hurüsh"
					elif magic_choice=="4":
						magic_type="Fire"
						mage_worship="Magarab"
					elif magic_choice=="5":
						magic_type="Water"
						mage_worship="Inauri"
					else:
						print("Not a valid choice, try again")
			elif character_world=="Ta'bros":
				if character_race=="Waheela":
					magic_type=""
					mage_worship=""
				elif character_race=="Imp":
					magic_type=""
					mage_worship=""
				else:
					magic_choice=input("""
					Please choose which deity you wish to worship, which will determine your magic type, by entering the relevant number:
					1 - Emolat - Darkness & Destruction, Patron Deity of Hunting (Dark Magic)
					2 - Rigath - Earth & The Forge, Patron Deity of Trading (Earth Magic)
					3 - Hurüsh - Air & Storms, Patron Deity of Vengeance (Air Magic)
					4 - Magarab - Fire & Chaos, Patron Deity of War (Fire Magic)
					5 - Inauri - Water & Oceans, Patron Deity of The Unknown (Water Magic)
					
					> """)
					if magic_choice=="1":
						magic_type="Dark"
						mage_worship="Emolat"
					elif magic_choice=="2":
						magic_type="Earth"
						mage_worship="Rigath"
					elif magic_choice=="3":
						magic_type="Air"
						mage_worship="Hurüsh"
					elif magic_choice=="4":
						magic_type="Fire"
						mage_worship="Magarab"
					elif magic_choice=="5":
						magic_type="Water"
						mage_worship="Inauri"
					else:
						print("Not a valid choice, try again")
			elif character_world=="Unified":
				if character_race=="Vinori":
					magic_choice=input("""
					Please choose which deity you wish to worship, which will determine your magic type, by entering the relevant number:
					1 - Elushaan - Lust & Control, Patron Deity of Seduction (Lust Magic)
					2 - Gormis - Rage & Power, Patron Deity of War (Rage Magic)
					3 - Halis - Light & Fire, Patron Deity of The Sun (Light Magic)
					4 - Ogrom - Animals & Earth, Patron Deity of Hunting (Animal Magic)
					5 - Shumid - Water & Tides, Patron Deity of Life (Tidal Magic)
					6 - Tyamir - Storms & Air, Patron Deity of Weather (Storm Magic)
					7 - Viran - Fear & Night, Patron Deity of Death (Fear Magic)
					
					> """)
					if magic_choice=="1":
						magic_type="Lust"
						mage_worship="Elushaan"
					elif magic_choice=="2":
						magic_type="Rage"
						mage_worship="Gormis"
					elif magic_choice=="3":
						magic_type="Light"
						mage_worship="Halis"
					elif magic_choice=="4":
						magic_type="Animal"
						mage_worship="Ogrom"
					elif magic_choice=="5":
						magic_type="Tidal"
						mage_worship="Shumid"
					elif magic_choice=="6":
						magic_type="Storm"
						mage_worship="Tyamir"
					elif magic_choice=="7":
						magic_type="Fear"
						mage_worship="Viran"
					else:
						print("Not a valid choice, try again")
				elif character_race=="Talis":
					magic_type=""
					mage_worship=""
				elif character_subrace=="Wood Golem":
					magic_type=""
					mage_worship=""
				elif character_race=="Faerie":
					magic_type=""
					mage_worship=""
				elif character_race=="Imp":
					magic_type=""
					mage_worship=""
				elif character_race=="Waheela":
					magic_type=""
					mage_worship=""
				else:
					magic_choice=input("""
					Your choice of available deities to worship depends on the world in which """+character_name+""" was born, either Eloria or Ta'bros.
					Eloria:
						Please choose which deity you wish to worship, which will determine your magic type, by entering the relevant number:
						1 - Belim - Darkness & Death, Patron Deity of Secrets (Dark Magic)
						2 - Faren - Earth & Nature, Patron Deity of Crafts (Earth Magic)
						3 - Kivena - Water & Oceans, Patron Deity of Sailing (Water Magic)
						4 - Movan - Fire & Spirit, Patron Deity of Home (Fire Magic)
						5 - Novia - Light & Life, Patron Deity of Healing (Light Magic)
						6 - Valira - Air & Weather, Patron Deity of Travel (Air Magic)
					
					Ta'bros:
						7 - Rigath - Earth & The Forge, Patron Deity of Trading (Earth Magic)
						8 - Inauri - Water & Oceans, Patron Deity of The Unknown (Water Magic)
						9 - Elos - Light & Stars, Patron Deity of Hope (Light Magic)
					
					> """)
					if magic_choice=="1":
						magic_type="Dark"
						mage_worship="Belim"
					elif magic_choice=="2":
						magic_type="Earth"
						mage_worship="Faren"
					elif magic_choice=="3":
						magic_type="Water"
						mage_worship="Kivena"
					elif magic_choice=="4":
						magic_type="Fire"
						mage_worship="Movan"
					elif magic_choice=="5":
						magic_type="Light"
						mage_worship="Novia"
					elif magic_choice=="6":
						magic_type="Air"
						mage_worship="Valira"
					elif magic_choice=="7":
						magic_type="Earth"
						mage_worship="Rigath"
					elif magic_choice=="8":
						magic_type="Water"
						mage_worship="Inauri"
					elif magic_choice=="9":
						magic_type="Light"
						mage_worship="Elos"
					else:
						print("Not a valid choice, try again")			
			character_manalevel=input("""
			What is """+character_name+"""'s Mana Level? This will determine """+character_name+"""'s magical attacks.
			
			> """)

			if magic_type=="Air":
				if character_manalevel=="1":
					character_spells="""Wind Spear - d4 + 4 AIR DMG (Suffocate) -2 Mana
	Whirling Tunnel - d6 + 6 AIR DMG (Suffocate) -4 Mana"""
				elif character_manalevel=="2":
					character_spells="""Wind Spear - d4 + 4 AIR DMG (Suffocate) -2 Mana
	Whirling Tunnel - d6 + 6 AIR DMG (Suffocate) -4 Mana
	Wind Wall - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Sky Armour - +4 Armour Rating on self + 4 AIR DMG against physical contact (Suffocate) (3 turns) -6 Mana"""
				elif character_manalevel=="3":
					character_spells="""Wind Spear - d4 + 4 AIR DMG (Suffocate) -2 Mana
	Whirling Tunnel - d6 + 6 AIR DMG (Suffocate) -4 Mana
	Wind Wall - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Sky Armour - +4 Armour Rating on self + 4 AIR DMG against physical contact (Suffocate) (3 turns) -6 Mana
	Cloud Charge - d4 + 4 AIR DMG (Suffocate) + 1/2 DMG nearby -6 Mana
	Tornado Blast - d6 + 6 AIR DMG (Suffocate) -8 Mana"""
			elif magic_type=="Dark":
				if character_manalevel=="1":
					character_spells="""Shadow Sphere - d4 + 4 DARK DMG (Blind) -2 Mana
	Shrouding Shade - d6 + 6 DARK DMG (Blind) -4 Mana"""
				elif character_manalevel=="2":
					character_spells="""Shadow Sphere - d4 + 4 DARK DMG (Blind) -2 Mana
	Shrouding Shade - d6 + 6 DARK DMG (Blind) -4 Mana
	Midnight Shield - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Reflectionless Armour - +4 Armour Rating on self + 4 DARK DMG against physical contact (Blind) (3 turns) -6 Mana"""
				elif character_manalevel=="3":
					character_spells="""Shadow Sphere - d4 + 4 DARK DMG (Blind) -2 Mana
	Shrouding Shade - d6 + 6 DARK DMG (Blind) -4 Mana
	Midnight Shield - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Reflectionless Armour - +4 Armour Rating on self + 4 DARK DMG against physical contact (Blind) (3 turns) -6 Mana
	Shadow Bomb - d4 + 4 DARK DMG (Blind) + 1/2 DMG nearby -6 Mana
	Night Curtain - d6 + 6 DARK DMG (Blind) -8 Mana"""
			elif magic_type=="Earth":
				if character_manalevel=="1":
					character_spells="""Rock Bolt - d4 + 4 EARTH DMG (Splinter) -2 Mana
	Sand Blast - d6 + 6 EARTH DMG (Splinter) -4 Mana"""
				elif character_manalevel=="2":
					character_spells="""Rock Bolt - d4 + 4 EARTH DMG (Splinter) -2 Mana
	Sand Blast - d6 + 6 EARTH DMG (Splinter) -4 Mana
	Stone Shield - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Spiked Skin - +4 Armour Rating on self + 4 EARTH DMG against physical contact (Splinter) (3 turns) -6 Mana"""
				elif character_manalevel=="3":
					character_spells="""Rock Bolt - d4 + 4 EARTH DMG (Splinter) -2 Mana
	Sand Blast - d6 + 6 EARTH DMG (Splinter) -4 Mana
	Stone Shield - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Spiked Skin - +4 Armour Rating on self + 4 EARTH DMG against physical contact (Splinter) (3 turns) -6 Mana
	Boulder Blast - d4 + 4 EARTH DMG (Splinter) + 1/2 DMG nearby -6 Mana
	Scouring Cone - d6 + 6 EARTH DMG (Splinter) -8 Mana"""
			elif magic_type=="Fire":
				if character_manalevel=="1":
					character_spells="""Fire Ball - d4 + 4 FIRE DMG (Burn) -2 Mana
	Flame Breath - d6 + 6 FIRE DMG (Burn) -4 Mana"""
				elif character_manalevel=="2":
					character_spells="""Fire Ball - d4 + 4 FIRE DMG (Burn) -2 Mana
	Flame Breath - d6 + 6 FIRE DMG (Burn) -4 Mana
	Burning Wall - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Inferno Armour - +4 Armour Rating on self + 4 FIRE DMG against physical contact (Burn) (3 turns) -6 Mana"""
				elif character_manalevel=="3":
					character_spells="""Fire Ball - d4 + 4 FIRE DMG (Burn) -2 Mana
	Flame Breath - d6 + 6 FIRE DMG (Burn) -4 Mana
	Burning Wall - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Inferno Armour - +4 Armour Rating on self + 4 FIRE DMG against physical contact (Burn) (3 turns) -6 Mana
	Flame Blast - d4 + 4 FIRE DMG (Burn) + 1/2 DMG nearby -6 Mana
	Cone of Fire - d6 + 6 FIRE DMG (Burn) -8 Mana"""
			elif magic_type=="Light":
				if character_manalevel=="1":
					character_spells="""Blinding Ball - d4 + 4 LIGHT DMG (Blind) -2 Mana
	Shining Beam - d6 + 6 LIGHT DMG (Blind) -4 Mana"""
				elif character_manalevel=="2":
					character_spells="""Blinding Ball - d4 + 4 LIGHT DMG (Blind) -2 Mana
	Shining Beam - d6 + 6 LIGHT DMG (Blind) -4 Mana
	Sunlight Shield - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Reflecting Armour - +4 Armour Rating on self + 4 LIGHT DMG against physical contact (Blind) (3 turns) -6 Mana"""
				elif character_manalevel=="3":
					character_spells="""Blinding Ball - d4 + 4 LIGHT DMG (Blind) -2 Mana
	Shining Beam - d6 + 6 LIGHT DMG (Blind) -4 Mana
	Sunlight Shield - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Reflecting Armour - +4 Armour Rating on self + 4 LIGHT DMG against physical contact (Blind) (3 turns) -6 Mana
	Star Bomb - d4 + 4 LIGHT DMG (Blind) + 1/2 DMG nearby -6 Mana
	Shining Blast - d6 + 6 LIGHT DMG (Blind) -8 Mana"""
			elif magic_type=="Water":
				if character_manalevel=="1":
					character_spells="""Aqua Ball - d4 + 4 WATER DMG (Sense Obscure) -2 Mana
	Torrential Blast - d6 + 6 WATER DMG (Sense Obscure) -4 Mana"""
				elif character_manalevel=="2":
					character_spells="""Aqua Ball - d4 + 4 WATER DMG (Sense Obscure) -2 Mana
	Torrential Blast - d6 + 6 WATER DMG (Sense Obscure) -4 Mana
	Water Wall - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Aquatic Armour - +4 Armour Rating on self + 4 WATER DMG against physical contact (Sense Obscure) (3 turns) -6 Mana"""
				elif character_manalevel=="3":
					character_spells="""Aqua Ball - d4 + 4 WATER DMG (Sense Obscure) -2 Mana
	Torrential Blast - d6 + 6 WATER DMG (Sense Obscure) -4 Mana
	Water Wall - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Aquatic Armour - +4 Armour Rating on self + 4 WATER DMG against physical contact (Sense Obscure) (3 turns) -6 Mana
	Hydro Bomb - d4 + 4 WATER DMG (Sense Obscure) + 1/2 DMG nearby -6 Mana
	Tidal Stream - d6 + 6 WATER DMG (Sense Obscure) -8 Mana"""
			elif magic_type=="Lust":
				if character_manalevel=="1":
					character_spells="""Enchanting Motes - d4 + 4 LUST DMG (Enthrall) -2 Mana
	Enticing Breeze - d6 + 6 LUST DMG (Enthrall) -4 Mana"""
				elif character_manalevel=="2":
					character_spells="""Enchanting Motes - d4 + 4 LUST DMG (Enthrall) -2 Mana
	Enticing Breeze - d6 + 6 LUST DMG (Enthrall) -4 Mana
	Pheramonal Shield - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Sensual Armour - +4 Armour Rating on self + 4 LUST DMG against physical contact (Enthrall) (3 turns) -6 Mana"""
				elif character_manalevel=="3":
					character_spells="""Enchanting Motes - d4 + 4 LUST DMG (Enthrall) -2 Mana
	Enticing Breeze - d6 + 6 LUST DMG (Enthrall) -4 Mana
	Pheramonal Shield - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Sensual Armour - +4 Armour Rating on self + 4 LUST DMG against physical contact (Enthrall) (3 turns) -6 Mana
	Enchanting Blast - d4 + 4 LUST DMG (Enthrall) + 1/2 DMG nearby -6 Mana
	Lusting Wave - d6 + 6 LUST DMG (Enthrall) -8 Mana"""
			elif magic_type=="Rage":
				if character_manalevel=="1":
					character_spells="""Anger Shot - d4 + 4 RAGE DMG (Berzerk) -2 Mana
	Fury Shout - d6 + 6 RAGE DMG (Berzerk) -4 Mana"""
				elif character_manalevel=="2":
					character_spells="""Anger Shot - d4 + 4 RAGE DMG (Berzerk) -2 Mana
	Fury Shout - d6 + 6 RAGE DMG (Berzerk) -4 Mana
	Intimidating Stare - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Rage Skin - +4 Armour Rating on self + 4 RAGE DMG against physical contact (Berzerk) (3 turns) -6 Mana"""
				elif character_manalevel=="3":
					character_spells="""Anger Shot - d4 + 4 RAGE DMG (Berzerk) -2 Mana
	Fury Shout - d6 + 6 RAGE DMG (Berzerk) -4 Mana
	Intimidating Stare - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Rage Skin - +4 Armour Rating on self + 4 RAGE DMG against physical contact (Berzerk) (3 turns) -6 Mana
	Anger Bomb - d4 + 4 RAGE DMG (Berzerk) + 1/2 DMG nearby -6 Mana
	Fury Scream - d6 + 6 RAGE DMG (Berzerk) -8 Mana"""
			elif magic_type=="Animal":
				if character_manalevel=="1":
					character_spells="""Untamed Blast - d4 + 4 ANIMAL DMG (Bestial Prey) -2 Mana
	Bestial Screech - d6 + 6 ANIMAL DMG (Bestial Prey) -4 Mana"""
				elif character_manalevel=="2":
					character_spells="""Untamed Blast - d4 + 4 ANIMAL DMG (Bestial Prey) -2 Mana
	Bestial Screech - d6 + 6 ANIMAL DMG (Bestial Prey) -4 Mana
	Wild Wall - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Feral Cloak - +4 Armour Rating on self + 4 ANIMAL DMG against physical contact (Bestial Prey) (3 turns) -6 Mana"""
				elif character_manalevel=="3":
					character_spells="""Untamed Blast - d4 + 4 ANIMAL DMG (Bestial Prey) -2 Mana
	Bestial Screech - d6 + 6 ANIMAL DMG (Bestial Prey) -4 Mana
	Wild Wall - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Feral Cloak - +4 Armour Rating on self + 4 ANIMAL DMG against physical contact (Bestial Prey) (3 turns) -6 Mana
	Beast Bomb - d4 + 4 ANIMAL DMG (Bestial Prey) + 1/2 DMG nearby -6 Mana
	Bestial Roar - d6 + 6 ANIMAL DMG (Bestial Prey) -8 Mana"""
			elif magic_type=="Storm":
				if character_manalevel=="1":
					character_spells="""Lightning Bolt - d4 + 4 LIGHTNING DMG (Shock)
	Thunder Tether - d6 + 6 LIGHTNING DMG (Shock)"""
				elif character_manalevel=="2":
					character_spells="""Lightning Bolt - d4 + 4 LIGHTNING DMG (Shock)
	Thunder Tether - d6 + 6 LIGHTNING DMG (Shock)
	Shock Barrier - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Charge Armour - +4 Armour Rating on self + 4 LIGHTNING DMG against physical contact (Shock) (3 turns) -6 Mana"""
				elif character_manalevel=="3":
					character_spells="""Lightning Bolt - d4 + 4 LIGHTNING DMG (Shock)
	Thunder Tether - d6 + 6 LIGHTNING DMG (Shock)
	Shock Barrier - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Charge Armour - +4 Armour Rating on self + 4 LIGHTNING DMG against physical contact (Shock) (3 turns) -6 Mana
	Lightning Blast - d4 + 4 LIGHTNING DMG (Shock) + 1/2 DMG nearby -6 Mana
	Storm Funnel - d6 + 6 LIGHTNING DMG (Shock) -8 Mana"""
			elif magic_type=="Fear":
				if character_manalevel=="1":
					character_spells="""Fear Ball - d4 + 4 FEAR DMG (Terrified) -2 Mana
	Fright Beam - d6 + 6 FEAR DMG (Terrified) -4 Mana"""
				elif character_manalevel=="2":
					character_spells="""Fear Ball - d4 + 4 FEAR DMG (Terrified) -2 Mana
	Fright Beam - d6 + 6 FEAR DMG (Terrified) -4 Mana
	Terror Barrier - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Panic Aura - +4 Armour Rating on self + 4 FEAR DMG against physical contact (Terrified) (3 turns) -6 Mana"""
				elif character_manalevel=="3":
					character_spells="""Fear Ball - d4 + 4 FEAR DMG (Terrified) -2 Mana
	Fright Beam - d6 + 6 FEAR DMG (Terrified) -4 Mana
	Terror Barrier - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Panic Aura - +4 Armour Rating on self + 4 FEAR DMG against physical contact (Terrified) (3 turns) -6 Mana
	Terror Blast - d4 + 4 FEAR DMG (Terrified) + 1/2 DMG nearby -6 Mana
	Dread Roar - d6 + 6 FEAR DMG (Terrified) -8 Mana"""

	global character_role
	character_role=input("""
		What is """+character_name+"""'s profession?

		>""")
	
	global character_alignment
	while character_alignment is None:
		alignment_choice=input("""
		What is """+character_name+"""'s moral alignment?
		This can change throughout the story as """+character_name+""" develops and grows.
		1 - Lawful Good: Will always strive to help others and follow the local laws
		2 - Neutral Good: Will always strive to help others, even if it means bending or breaking the law to do so
		3 - Chaotic Good: Will always strive to help others, and are more than happy to break the law to do so

		4 - Lawful Neutral: Follows the law, regardless of the affects this would have on the people involved
		5 - Neutral Neutral: Follows only their own personal sense of justice
		6 - Chaotic Neutral: Follows their heart, regardless of rules and tradition

		7 - Lawful Evil: Will stick to the law, purely out of self interest, but has no qualms about paying, threatening or tricking others into doing their dirty work
		8 - Neutral Evil: Will follow their own self-interest above all else, even if it brings harm to others, but won't cause harm unnecessarily
		9 - Chaotic Evil: Will follow their own self-interest and care little for the lives of those around them, happy to bring misery or pain for little to no reason

		10 - Unaligned: For beings that have no sense of morality, operating purely on instinct

		> """)
		if alignment_choice=="1":
			character_alignment="Lawful Good"
		elif alignment_choice=="2":
			character_alignment="Neutral Good"
		elif alignment_choice=="3":
			character_alignment="Chaotic Good"
		elif alignment_choice=="4":
			character_alignment="Lawful Neutral"
		elif alignment_choice=="5":
			character_alignment="Neutral Neutral"
		elif alignment_choice=="6":
			character_alignment="Chaotic Neutral"
		elif alignment_choice=="7":
			character_alignment="Lawful Evil"
		elif alignment_choice=="8":
			character_alignment="Neutral Evil"
		elif alignment_choice=="9":
			character_alignment="Chaotic Evil"
		elif alignment_choice=="10":
			character_alignment="Unaligned"
		else:
			print("Not a valid choice, try again")

create_character()

def create_character_skill_sheet():
	cls()
	global character_name, character_class, character_age, character_role, character_gender, character_race, character_subrace, character_level, character_xp, character_strength, character_speed, character_stamina, character_agility, character_dexterity, character_constitution, character_perception, character_intelligence, character_mana, character_manapower, character_manalevel, character_charisma, character_stealth, character_luck, character_armour, character_skills, class_skills, character_spells, race_attacks, magic_type, character_worship, race_worship, mage_worship, character_era
	print("""
	Now, let's determine """+character_name+"""'s skills, which you will use throughout the game.
	In this game, """+character_name+""" has 13 skills:

	- Strength - Used in combat or strength tests
	- Speed - How quickly you can move
	- Stamina - Determines how long you can perform an action before tiring
	- Agility - How fast your reaction or dodging speed is
	- Dexterity - How good you are at performing tricky tasks with your hands
	- Constitution - Your life energy. If this hits 0, """+character_name+""" is on the verge of death
	- Perception - How well you notice details in your surroundings
	- Intelligence - How smart """+character_name+""" is, good for understanding things
	- Mana - How often """+character_name+""" can use your magic (if any)
	- Mana Power - How strong """+character_name+"""'s magic power is (if any)
	- Charisma - How charming and persuasive you are
	- Stealth - Your ability to sneak and remain undetected relies on this
	- Luck - This determines how often hidden events are triggered, as well as what loot your may find

	Depending on your race and class, you will have a certain point-base already calculated by the game.
	You will shortly be able to increase your skills by rolling a 6-faced die.

	Here is your base Character Skills Sheet:
	""")
	character_strength=5
	character_speed=5
	character_stamina=5
	character_agility=5
	character_dexterity=5
	character_constitution=10
	character_perception=5
	character_intelligence=5
	character_mana=0
	character_manapower=0
	character_manalevel=0
	character_charisma=5
	character_stealth=5
	character_luck=5
	character_armour=0
	if character_race=="Aamon":
		character_strength=character_strength+6
		character_speed=character_speed+3
		character_stamina=character_stamina+7
		character_agility=character_agility+4
		character_dexterity=character_dexterity+3
		character_constitution=character_constitution+6
		character_perception=character_perception+7
		character_intelligence=character_intelligence+7
		character_charisma=character_charisma+4
		character_stealth=character_stealth+6
		character_skills="""Flight
	Dark Vision/Enhanced Vision
	Silent Flight"""
		race_attacks="Slash - d4 + 6 Slashing DMG"
	elif character_race=="Ackirian":
		character_strength=character_strength+5
		character_speed=character_speed+5
		character_stamina=character_stamina+6
		character_agility=character_agility+6
		character_dexterity=character_dexterity+5
		character_constitution=character_constitution+6
		character_perception=character_perception+6
		character_intelligence=character_intelligence+4
		character_charisma=character_charisma+4
		character_stealth=character_stealth+6
		character_skills="""Dark Vision
	Thermal Camouflage
	Blood Drain"""
		race_attacks="""Punch - d4 + 2 Bludgeoning DMG
	Bite - d4 + 4 Piercing DMG + Heal 1/2 DMG Dealt"""
	elif character_race=="Adlet":
		character_strength=character_strength+6
		character_speed=character_speed+8
		character_stamina=character_stamina+5
		character_agility=character_agility+4
		character_dexterity=character_dexterity+4
		character_constitution=character_constitution+8
		character_perception=character_perception+6
		character_intelligence=character_intelligence+3
		character_charisma=character_charisma+2
		character_stealth=character_stealth+7
		character_skills="""Enhanced Senses
	Dark Vision"""
		race_attacks="""Slash - d4 + 4 Slashing DMG
	Bite - d4 + 6 Piercing DMG"""
	elif character_race=="Bokabu":
		character_strength=character_strength+4
		character_speed=character_speed+5
		character_stamina=character_stamina+7
		character_agility=character_agility+3
		character_dexterity=character_dexterity+6
		character_constitution=character_constitution+9
		character_perception=character_perception+7
		character_intelligence=character_intelligence+4
		character_charisma=character_charisma+3
		character_stealth=character_stealth+7
		character_armour=10
		character_skills="""Botanical Knowledge
	Photosynthesis
	Elder Advice
	Natural Bark Armour
	Regeneration"""
		race_attacks="Slap - d4 Bludgeoning DMG"
		race_worship="Palitar"
	elif character_race=="Cecaelia":
		character_strength=character_strength+5
		character_speed=character_speed+7
		character_stamina=character_stamina+6
		character_agility=character_agility+9
		character_dexterity=character_dexterity+9
		character_constitution=character_constitution+6
		character_perception=character_perception+7
		character_intelligence=character_intelligence+5
		character_charisma=character_charisma+5
		character_stealth=character_stealth+7
		character_skills="""Aquatic
	Dark Vision
	Regeneration"""
		race_attacks="""Punch - d4 + 2 Bludgeoning DMG
	Bind - Target rolls either Strength or Dexterity against Strength to escape, or remains immobilised"""
	elif character_race=="Centaur":
		character_strength=character_strength+6
		character_speed=character_speed+9
		character_stamina=character_stamina+7
		character_agility=character_agility+6
		character_dexterity=character_dexterity+3
		character_constitution=character_constitution+4
		character_perception=character_perception+4
		character_intelligence=character_intelligence+5
		character_charisma=character_charisma+6
		character_stealth=character_stealth+1
		character_skills="Perfected Stamina"
		race_attacks="""Punch - d4 + 3 Bludgeoning DMG
	Kick - d8 + 2 Bludgeoning DMG"""
	elif character_race=="Daoine Sith":
		character_strength=character_strength+4
		character_speed=character_speed+4
		character_stamina=character_stamina+6
		character_agility=character_agility+6
		character_dexterity=character_dexterity+6
		character_constitution=character_constitution+3
		character_perception=character_perception+5
		character_intelligence=character_intelligence+5
		character_charisma=character_charisma+5
		character_stealth=character_stealth+5
		if character_subrace=="Hürdin":
			character_skills="""Enhanced Senses
		Animal Transformation ("+str(h_subrace)+")"""
			race_attacks="""Punch - d4 + 2 Bludgeoning DMG
		Hürdin ? (Partial Transformation) - ? DMG
		Hürdin ? (Full Transformation) - ? DMG"""
		else:
			character_skills="Enhanced Hearing"
			race_attacks="Punch - d4 + 2 Bludgeoning DMG"
	elif character_race=="Delphyne":
		character_strength=character_strength+6
		character_speed=character_speed+4
		character_stamina=character_stamina+4
		character_agility=character_agility+6
		character_dexterity=character_dexterity+6
		character_constitution=character_constitution+6
		character_perception=character_perception+7
		character_intelligence=character_intelligence+5
		character_charisma=character_charisma+4
		character_stealth=character_stealth+6
		character_skills="""Deadly Venom
	Wall Scaling
	Dark Vision
	Thermal Vision
	Regeneration
	Enhanced Senses of Taste and Smell"""
		race_attacks="""Punch - d4 + 2 Bludgeoning
	Slash - d4 + 2 Slashing
	Bite - d4 + Venom (Target takes 1 d4 Poison DMG on each turn, then rolls current Constitution to try and purge the venom (roll against Charisma or Intelligence)"""
	elif character_race=="Dökkálfar":
		character_strength=character_strength+5
		character_speed=character_speed+4
		character_stamina=character_stamina+5
		character_agility=character_agility+6
		character_dexterity=character_dexterity+6
		character_constitution=character_constitution+4
		character_perception=character_perception+5
		character_intelligence=character_intelligence+5
		character_charisma=character_charisma+4
		character_stealth=character_stealth+6
		character_skills="""Enhanced Hearing
	Dark Vision"""
		race_attacks="Punch - d4 + 2 Bludgeoning"
	elif character_subrace=="Northern Dragon":
		character_strength=character_strength+25
		character_speed=character_speed+10
		character_stamina=character_stamina+15
		character_agility=character_agility+12
		character_dexterity=character_dexterity+10
		character_constitution=character_constitution+125
		character_perception=character_perception+8
		character_intelligence=character_intelligence+20
		character_charisma=character_charisma+8
		character_stealth=character_stealth+5
		character_armour=15
		character_skills="""Flight
	Scale Armour
	Enhanced Vision
	Regeneration"""
		race_attacks="""Slash - d12 + 10 Slahing DMG
	Bite - d12 + 12 Piercing DMG
	Stomp - d10 + 12 Bludgeoning DMG
	Tail Slam - d10 + 8 Bludgeoning DMG"""
	elif character_subrace=="Southern Dragon":
		character_strength=character_strength+15
		character_speed=character_speed+11
		character_stamina=character_stamina+25
		character_agility=character_agility+17
		character_dexterity=character_dexterity+12
		character_constitution=character_constitution+100
		character_perception=character_perception+10
		character_intelligence=character_intelligence+20
		character_charisma=character_charisma+7
		character_stealth=character_stealth+7
		character_armour=15
		character_skills="""Flight
	Scale Armour
	Enhanced Vision
	Regeneration"""
		race_attacks="""Slash - d12 + 10 Slahing DMG
	Bite - d12 + 12 Piercing DMG
	Bind - Target rolls either Strength or Dexterity against Strength to escape, or remains immobilised
	Tail Slam - d10 + 8 Bludgeoning DMG"""
		race_worship="Valira"
	elif character_subrace=="Sea Dragon":
		character_strength=character_strength+20
		character_speed=character_speed+30
		character_stamina=character_stamina+20
		character_agility=character_agility+20
		character_dexterity=character_dexterity+7
		character_constitution=character_constitution+110
		character_perception=character_perception+12
		character_intelligence=character_intelligence+20
		character_charisma=character_charisma+4
		character_stealth=character_stealth+10
		character_armour=15
		character_skills="""Aquatic
	Scale Armour
	Enhanced Vision
	Regeneration"""
		race_attacks="""Slash - d12 + 10 Slahing DMG
	Bite - d12 + 12 Piercing DMG"""
		race_worship="Kivena"
	elif character_race=="Dwarf":
		character_strength=character_strength+7
		character_speed=character_speed+2
		character_stamina=character_stamina+7
		character_agility=character_agility+3
		character_dexterity=character_dexterity+7
		character_constitution=character_constitution+7
		character_perception=character_perception+6
		character_intelligence=character_intelligence+6
		character_charisma=character_charisma+4
		character_stealth=character_stealth+3
		race_worship="Faren"
		if character_subrace=="Hürdin":
			character_skills="""Craft Appraisal
		Enhanced Senses
		Animal Transformation ("+str(h_subrace)+")"""
			race_attacks="""Punch - d4 + 4 Bludgeoning DMG
		Hürdin ? (Partial Transformation) - ? DMG
		Hürdin ? (Full Transformation) - ? DMG"""
		else:
			character_skills="""Craft Appraisal
		Dark Vision"""
			race_attacks="Punch - d4 + 4 Bludgeoning DMG"
	elif character_race=="Elfling":
		character_strength=character_strength+4
		character_speed=character_speed+5
		character_stamina=character_stamina+5
		character_agility=character_agility+6
		character_dexterity=character_dexterity+5
		character_constitution=character_constitution+6
		character_perception=character_perception+5
		character_intelligence=character_intelligence+5
		character_charisma=character_charisma+4
		character_stealth=character_stealth+3
		character_skills="Enhanced Hearing"
		race_attacks="Punch - d4 + 2 Bludgeoning DMG"
	elif character_subrace=="Alven":
		character_strength=character_strength+2
		character_speed=character_speed+7
		character_stamina=character_stamina+7
		character_agility=character_agility+12
		character_dexterity=character_dexterity+7
		character_constitution=character_constitution+3
		character_perception=character_perception+7
		character_intelligence=character_intelligence+8
		character_mana=character_mana+5
		character_manapower=character_manapower+6
		character_charisma=character_charisma+8
		character_stealth=character_stealth+10
		character_skills="""Flight
	Semi-Aquatic
	Lvl1 Water Magic"""
		race_attacks="""Aqua Ball - d4 + 4 WATER DMG (Sense Obscure)
	Torrential Blast - d6 + 6 WATER DMG (Sense Obscure)"""
	elif character_subrace=="Ariel":
		character_strength=character_strength+2
		character_speed=character_speed+12
		character_stamina=character_stamina+8
		character_agility=character_agility+10
		character_dexterity=character_dexterity+7
		character_constitution=character_constitution+3
		character_perception=character_perception+6
		character_intelligence=character_intelligence+8
		character_mana=character_mana+5
		character_manapower=character_manapower+6
		character_charisma=character_charisma+8
		character_stealth=character_stealth+12
		character_skills="""Flight
	Lvl1 Air Magic"""
		race_attacks="""Wind Spear - d4 + 4 AIR DMG (Suffocate) -2 Mana
	Whirling Tunnel - d6 + 6 AIR DMG (Suffocate) -4 Mana"""
	elif character_subrace=="Domovik":
		character_strength=character_strength+4
		character_speed=character_speed+3
		character_stamina=character_stamina+6
		character_agility=character_agility+5
		character_dexterity=character_dexterity+8
		character_constitution=character_constitution+4
		character_perception=character_perception+7
		character_intelligence=character_intelligence+9
		character_mana=character_mana+5
		character_manapower=character_manapower+6
		character_charisma=character_charisma+10
		character_stealth=character_stealth+8
		character_skills="""Camouflage
	Lvl1 Food Magic"""
		race_attacks="""Grain Manifest - d4 + 4 FOOD DMG (Beast Attract) -2 Mana
	Rice Stream - d6 + 6 FOOD DMG (Beast Attract) -4 Mana"""
	elif character_subrace=="Drachen":
		character_strength=character_strength+4
		character_speed=character_speed+7
		character_stamina=character_stamina+6
		character_agility=character_agility+7
		character_dexterity=character_dexterity+7
		character_constitution=character_constitution+4
		character_perception=character_perception+6
		character_intelligence=character_intelligence+8
		character_mana=character_mana+5
		character_manapower=character_manapower+7
		character_charisma=character_charisma+6
		character_stealth=character_stealth+3
		character_skills="""Flight
	Heat Tolerance
	Lvl1 Fire Magic"""
		race_attacks="""Fire Ball - d4 + 4 FIRE DMG (Burn) -2 Mana
	Flame Breath - d6 + 6 FIRE DMG (Burn) -4 Mana"""
	elif character_subrace=="Ghille Dhu":
		character_strength=character_strength+4
		character_speed=character_speed+6
		character_stamina=character_stamina+6
		character_agility=character_agility+8
		character_dexterity=character_dexterity+7
		character_constitution=character_constitution+4
		character_perception=character_perception+7
		character_intelligence=character_intelligence+8
		character_mana=character_mana+5
		character_manapower=character_manapower+5
		character_charisma=character_charisma+3
		character_stealth=character_stealth+17
		character_skills="""Flight
	Camouflage
	Lvl1 Wild Magic"""
		race_attacks="""Forest Bolt - d4 + 4 WILD DMG (Thorny Terrain) -2 Mana
	Jungle Barrage - d6 + 6 WILD DMG (Thorny Terrain) -4 Mana"""
	elif character_subrace=="Kobold":
		character_strength=character_strength+7
		character_speed=character_speed+6
		character_stamina=character_stamina+7
		character_agility=character_agility+4
		character_dexterity=character_dexterity+7
		character_constitution=character_constitution+5
		character_perception=character_perception+7
		character_intelligence=character_intelligence+6
		character_mana=character_mana+5
		character_manapower=character_manapower+5
		character_charisma=character_charisma+4
		character_stealth=character_stealth+7
		character_armour=4
		character_skills="""Dark Vision
	Thick Skin
	Lvl1 Earth Magic"""
		race_attacks="""Rock Bolt - d4 + 4 EARTH DMG (Splinter) -2 Mana
	Sand Blast - d6 + 6 EARTH DMG (Splinter) -4 Mana"""
	elif character_subrace=="Lunantishee":
		character_strength=character_strength+4
		character_speed=character_speed+7
		character_stamina=character_stamina+6
		character_agility=character_agility+7
		character_dexterity=character_dexterity+8
		character_constitution=character_constitution+4
		character_perception=character_perception+6
		character_intelligence=character_intelligence+8
		character_mana=character_mana+5
		character_manapower=character_manapower+6
		character_charisma=character_charisma+4
		character_stealth=character_stealth+4
		character_skills="""Flight
	Lvl1 War Magic"""
		race_attacks="""Rage Point - d4 + 4 WAR DMG (Berzerk) -2 Mana
	War Scream - d6 + 6 WAR DMG (Berzerk) -4 Mana"""
	elif character_subrace=="Pixie":
		character_strength=character_strength+2
		character_speed=character_speed+7
		character_stamina=character_stamina+6
		character_agility=character_agility+9
		character_dexterity=character_dexterity+7
		character_constitution=character_constitution+3
		character_perception=character_perception+6
		character_intelligence=character_intelligence+8
		character_mana=character_mana+5
		character_manapower=character_manapower+3
		character_charisma=character_charisma+8
		character_stealth=character_stealth+7
		character_skills="""Flight
	Lvl1 Plant Magic"""
		race_attacks="""Flora Shard - d4 + 4 PLANT DMG (Bind) -2 Mana
	Seed Barrage - d6 + 6 PLANT DMG (Bind) -4 Mana"""
	elif character_subrace=="Sprite":
		character_strength=character_strength+2
		character_speed=character_speed+8
		character_stamina=character_stamina+6
		character_agility=character_agility+10
		character_dexterity=character_dexterity+7
		character_constitution=character_constitution+3
		character_perception=character_perception+6
		character_intelligence=character_intelligence+8
		character_mana=character_mana+5
		character_manapower=character_manapower+3
		character_charisma=character_charisma+8
		character_stealth=character_stealth+5
		character_skills="""Flight
	Lvl1 Plant Magic"""
		race_attacks="""Flora Shard - d4 + 4 PLANT DMG (Bind) -2 Mana
	Seed Barrage - d6 + 6 PLANT DMG (Bind) -4 Mana"""
	elif character_subrace=="Tuatha De Danaan":
		character_strength=character_strength+4
		character_speed=character_speed+7
		character_stamina=character_stamina+7
		character_agility=character_agility+12
		character_dexterity=character_dexterity+9
		character_constitution=character_constitution+4
		character_perception=character_perception+8
		character_intelligence=character_intelligence+8
		character_mana=character_mana+5
		character_manapower=character_manapower+5
		character_charisma=character_charisma+2
		character_stealth=character_stealth+18
		character_skills="""Flight
	Dark Vision
	Lvl1 Time Magic"""
		race_attacks="""Temporal Shiv - d4 + 4 TIME DMG (Pause Time) -2 Mana
	Reversal Stream - d6 + 6 TIME DMG (Pause Time) -4 Mana"""
	elif character_subrace=="Vardogl":
		character_strength=character_strength+2
		character_speed=character_speed+9
		character_stamina=character_stamina+7
		character_agility=character_agility+11
		character_dexterity=character_dexterity+7
		character_constitution=character_constitution+3
		character_perception=character_perception+7
		character_intelligence=character_intelligence+8
		character_mana=character_mana+5
		character_manapower=character_manapower+6
		character_charisma=character_charisma+8
		character_stealth=character_stealth+17
		character_skills="""Flight
	Dark Vision
	Lvl1 Dark Magic
	Lvl1 Music Magic"""
		race_attacks="""Shadow Sphere - d4 + 4 DARK DMG (Blind) -2 Mana
	Shrouding Shade - d6 + 6 DARK DMG (Blind) -4 Mana
	Sweet Seranade - + d4 to all allies next rolls -2 Mana
	Trembling Chords - All enemies in hearing range make their next rolls with disadvantage -4 Mana"""
	elif character_subrace=="Venusleutes":
		character_strength=character_strength+2
		character_speed=character_speed+7
		character_stamina=character_stamina+9
		character_agility=character_agility+12
		character_dexterity=character_dexterity+8
		character_constitution=character_constitution+3
		character_perception=character_perception+8
		character_intelligence=character_intelligence+8
		character_mana=character_mana+5
		character_manapower=character_manapower+3
		character_charisma=character_charisma+8
		character_stealth=character_stealth+6
		character_skills="""Flight
	Lvl1 Love Magic"""
		race_attacks="""Crushing Orb - d4 + 4 LOVE DMG (Infatuate) -2 Mana
	Beam of Heartache - d6 + 6 LOVE DMG (Infatuate) -4 Mana"""
	elif character_race=="Garikon":
		character_strength=character_strength+8
		character_speed=character_speed+3
		character_stamina=character_stamina+7
		character_agility=character_agility+2
		character_dexterity=character_dexterity+5
		character_constitution=character_constitution+7
		character_perception=character_perception+4
		character_intelligence=character_intelligence+5
		character_charisma=character_charisma+5
		character_stealth=character_stealth+2
		character_armour=12
		character_skills="""Stone Skin
	Four Arms
	Rock Digestion
	Dark Vision"""
		race_attacks="""Single Punch - d4 + 2 Bludgeoning DMG
	Multi-Fist Pummel - d4 + 2 Bludgeoning DMG (x number of fists)"""
		race_worship="Faren"
	elif character_race=="Garuda":
		character_strength=character_strength+6
		character_speed=character_speed+3
		character_stamina=character_stamina+7
		character_agility=character_agility+4
		character_dexterity=character_dexterity+3
		character_constitution=character_constitution+6
		character_perception=character_perception+7
		character_intelligence=character_intelligence+5
		character_charisma=character_charisma+5
		character_stealth=character_stealth+6
		character_skills="""Flight
	Dark Vision
	Enhanced Distance Vision"""
		race_attacks="""Punch - d4 + 2 Bludgeoning DMG
	Slash - d4 + 4 Slashing DMG"""
	elif character_race=="Giant":
		character_strength=character_strength+15
		character_speed=character_speed+8
		character_stamina=character_stamina+12
		character_agility=character_agility+4
		character_dexterity=character_dexterity+6
		character_constitution=character_constitution+55
		character_perception=character_perception+7
		character_intelligence=character_intelligence+3
		character_charisma=character_charisma+2
		character_stealth=character_stealth+2
		character_armour=4
		character_skills="""Thick Skin
	Enhanced Pain Tolerance"""
		race_attacks="""Punch - d8 + 6 Bludgeoning DMG
	Slam - d8 + 8 Bludgeoning DMG"""
	elif character_race=="Goblin":
		character_strength=character_strength+4
		character_speed=character_speed+6
		character_stamina=character_stamina+7
		character_agility=character_agility+5
		character_dexterity=character_dexterity+5
		character_constitution=character_constitution+7
		character_perception=character_perception+4
		character_intelligence=character_intelligence+4
		character_charisma=character_charisma+2
		character_stealth=character_stealth+6
		character_skills="""Increased Pain Tolerance
	Dark Vision"""
		race_attacks="""Punch - d4 Bludgeoning DMG
	Slash - d4 + 2 Slashing DMG
	Bite - d4 + 4 Piercing DMG"""
	elif character_subrace=="Clay Golem":
		character_strength=character_strength+5
		character_speed=character_speed+6
		character_stamina=character_stamina+20
		character_agility=character_agility+4
		character_dexterity=character_dexterity+6
		character_constitution=character_constitution+7
		character_perception=character_perception+6
		character_intelligence=character_intelligence+6
		character_charisma=character_charisma+3
		character_stealth=character_stealth+6
		character_skills="""Poison Immunity
	Insomnia
	Breathless"""
		race_attacks="Punch - d4 + 4 Bludgeoning DMG"
	elif character_subrace=="Stone Golem":
		character_strength=character_strength+8
		character_speed=character_speed+3
		character_stamina=character_stamina+20
		character_agility=character_agility+3
		character_dexterity=character_dexterity+7
		character_constitution=character_constitution+9
		character_perception=character_perception+6
		character_intelligence=character_intelligence+6
		character_charisma=character_charisma+5
		character_stealth=character_stealth+7
		character_armour=12
		character_skills="""Stone Skin
	Poison Immunity
	Insomnia
	Breathless"""
		race_attacks="Punch - d6 + 4 Bludgeoning DMG"
	elif character_subrace=="Wood Golem":
		character_strength=character_strength+5
		character_speed=character_speed+5
		character_stamina=character_stamina+20
		character_agility=character_agility+5
		character_dexterity=character_dexterity+8
		character_constitution=character_constitution+5
		character_perception=character_perception+6
		character_intelligence=character_intelligence+9
		character_mana=character_mana+5
		character_manapower=character_manapower+8
		character_charisma=character_charisma+8
		character_stealth=character_stealth+6
		character_armour=10
		character_skills="""Bark Armour
	Insomnia
	Breathless
	Lvl1 Earth Magic
	Lvl1 Light Magic
	Lvl2 Life Magic"""
		race_attacks="""Punch d4 + 2 Bludgeoning DMG
	Rock Bolt - d4 + 4 EARTH DMG (Splinter) -2 Mana
	Sand Blast - d6 + 6 EARTH DMG (Splinter) -4 Mana
	Blinding Ball - d4 + 4 LIGHT DMG (Blind) -2 Mana
	Shining Beam - d6 + 6 LIGHT DMG (Blind) -4 Mana
	Healing Orb - d4 + 4 HP (Heal) -2 Mana
	Rejuvinate - d6 + 6 HP (Heal) -4 Mana
	Heartbeat Shield - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Lifeblood Armour - +4 Armour Rating on self + 4 HP to allies with physical contact (Heal) (3 turns) -6 Mana"""
		race_worship="Faren"
	elif character_subrace=="Gold Golem":
		character_strength=character_strength+7
		character_speed=character_speed+4
		character_stamina=character_stamina+20
		character_agility=character_agility+4
		character_dexterity=character_dexterity+7
		character_constitution=character_constitution+7
		character_perception=character_perception+6
		character_intelligence=character_intelligence+6
		character_charisma=character_charisma+5
		character_stealth=character_stealth+2
		character_armour=6
		character_skills="""Weak Metal Body
	Poison Immunity
	Insomnia
	Breathless"""
		race_attacks="Punch - d4 + 4 Bludgeoning DMG"
	elif character_subrace=="Crystal Golem":
		character_strength=character_strength+10
		character_speed=character_speed+3
		character_stamina=character_stamina+20
		character_agility=character_agility+4
		character_dexterity=character_dexterity+7
		character_constitution=character_constitution+12
		character_perception=character_perception+6
		character_intelligence=character_intelligence+7
		character_charisma=character_charisma+4
		character_stealth=character_stealth+2
		character_armour=18
		character_skills="""Crystal Body
	Poison Immunity
	Insomnia
	Breathless
	Magic Immunity"""
		race_attacks="Punch - d4 + 6 Bludgeoning"
	elif character_subrace=="Iron Golem":
		character_strength=character_strength+12
		character_speed=character_speed+4
		character_stamina=character_stamina+20
		character_agility=character_agility+3
		character_dexterity=character_dexterity+7
		character_constitution=character_constitution+10
		character_perception=character_perception+6
		character_intelligence=character_intelligence+5
		character_charisma=character_charisma+4
		character_stealth=character_stealth+4
		character_armour=15
		character_skills="""Metal Body
	Poison Immunity
	Insomnia
	Breathless"""
		race_attacks="Punch - d6 + 4 Bludgeoning DMG"
	elif character_race=="Greftaga":
		character_strength=character_strength+8
		character_speed=character_speed+1
		character_stamina=character_stamina+9
		character_agility=character_agility+1
		character_dexterity=character_dexterity+8
		character_constitution=character_constitution+8
		character_perception=character_perception+3
		character_intelligence=character_intelligence+4
		character_charisma=character_charisma+2
		character_stealth=character_stealth+7
		character_armour=10
		character_skills="""Botanical Knowledge
	Dark Vision
	Parasitism
	Bark Armour
	Regeneration"""
		race_attacks="""Punch - d6 + 6 Bludgeoning DMG
	Thorn Whip - d6 + 4 Slashing DMG"""
		race_worship="Rigath"
	elif character_race=="Harpy":
		character_strength=character_strength+3
		character_speed=character_speed+7
		character_stamina=character_stamina+4
		character_agility=character_agility+8
		character_dexterity=character_dexterity+5
		character_constitution=character_constitution+4
		character_perception=character_perception+6
		character_intelligence=character_intelligence+5
		character_charisma=character_charisma+6
		character_stealth=character_stealth+4
		character_skills="""Flight
	Arial Agility"""
		race_attacks="Slash - d4 + 4 Slashing DMG"
		race_worship="Valira"
	elif character_race=="Human":
		character_strength=character_strength+5
		character_speed=character_speed+5
		character_stamina=character_stamina+5
		character_agility=character_agility+5
		character_dexterity=character_dexterity+5
		character_constitution=character_constitution+5
		character_perception=character_perception+5
		character_intelligence=character_intelligence+5
		character_charisma=character_charisma+5
		character_stealth=character_stealth+5
		if character_subrace=="Hürdin":
			character_skills="""AdaptableEnhanced Senses
		Animal Transformation ("""+str(h_subrace)+""")"""
			race_attacks="Punch - d4 + 2 Bludgeoning DMG"
		else:
			character_skills="Adaptable"
			race_attacks="Punch - d4 + 2 Bludgeoning DMG"
	elif character_race=="Ibrigat":
		character_strength=character_strength+6
		character_speed=character_speed+3
		character_stamina=character_stamina+7
		character_agility=character_agility+6
		character_dexterity=character_dexterity+6
		character_constitution=character_constitution+6
		character_perception=character_perception+6
		character_intelligence=character_intelligence+4
		character_charisma=character_charisma+3
		character_stealth=character_stealth+6
		character_armour=15
		character_skills="""Scale Armour
	Regeneration
	Enhanced Sense of Taste and Smell"""
		race_attacks="""Slash - d4 + 4 Slashing DMG
	Bite - d4 + 6 Piercing DMG
	Tail Slam - d4 + 2 Bludgeoning DMG"""
	elif character_race=="Imp":
		character_strength=character_strength+2
		character_speed=character_speed+8
		character_stamina=character_stamina+6
		character_agility=character_agility+10
		character_dexterity=character_dexterity+7
		character_constitution=character_constitution+3
		character_perception=character_perception+6
		character_intelligence=character_intelligence+8
		character_mana=character_mana+5
		character_manapower=character_manapower+3
		character_charisma=character_charisma+3
		character_stealth=character_stealth+8
		character_skills="""Flight
	Shapeshifter
	Lvl1 Dark Magic"""
		race_attacks="""Slash - d4 + 2 Slashing DMG
	Bite - d4 + 2 Piercing DMG
	Shadow Sphere - d4 + 4 DARK DMG (Blind) -2 Mana
	Shrouding Shade - d6 + 6 DARK DMG (Blind) -4 Mana"""
		if character_world=="Unified":
			race_worship="Zinix"
		else:
			race_worship="Emolat"
	elif character_race=="Jorogumo":
		character_strength=character_strength+6
		character_speed=character_speed+6
		character_stamina=character_stamina+3
		character_agility=character_agility+7
		character_dexterity=character_dexterity+8
		character_constitution=character_constitution+3
		character_perception=character_perception+7
		character_intelligence=character_intelligence+6
		character_charisma=character_charisma+1
		character_stealth=character_stealth+7
		character_skills="""Paralysing Venom
	Sticky Silk Webs
	Surface Climbing
	Dark Vision
	270º Field of Vision
	Vibration Sense"""
		race_attacks="""Slash - d4 + 4 Slashing DMG
	Bite - d4 + Venom (Target is immobilised due to paralysis, then rolls current Constitution to try and purge the venom (roll against Charisma or Intelligence)
	Web Snare - Target rolls Strength against Charisma or Intelligence to escape, or remains immobilised"""
	elif character_subrace=="Brown Carapace":
		character_strength=character_strength+7
		character_speed=character_speed+4
		character_stamina=character_stamina+7
		character_agility=character_agility+4
		character_dexterity=character_dexterity+6
		character_constitution=character_constitution+6
		character_perception=character_perception+3
		character_intelligence=character_intelligence+4
		character_charisma=character_charisma+3
		character_stealth=character_stealth+6
		character_armour=10
		character_skills="""Extra Tough Carapace
	Hive Knowledge
	Dark Vision
	Enhanced Senses of Hearing and Smell
	Flight"""
		race_attacks="Slash - d4 + 6 Slashing DMG"
	elif character_subrace=="Green Carapace":
		character_strength=character_strength+6
		character_speed=character_speed+5
		character_stamina=character_stamina+7
		character_agility=character_agility+5
		character_dexterity=character_dexterity+7
		character_constitution=character_constitution+5
		character_perception=character_perception+6
		character_intelligence=character_intelligence+4
		character_charisma=character_charisma+3
		character_stealth=character_stealth+8
		character_armour=8
		character_skills="""Tough Carapace
	Camouflage
	Hive Knowledge
	Dark Vision
	Enhanced Senses of Hearing and Smell
	Flight"""
		race_attacks="Slash - d4 + 6 Slashing DMG"
	elif character_subrace=="Blue Carapace":
		character_strength=character_strength+5
		character_speed=character_speed+5
		character_stamina=character_stamina+7
		character_agility=character_agility+4
		character_dexterity=character_dexterity+6
		character_constitution=character_constitution+5
		character_perception=character_perception+8
		character_intelligence=character_intelligence+4
		character_charisma=character_charisma+3
		character_stealth=character_stealth+6
		character_armour=8
		character_skills="""Tough Carapace
	Hive Knowledge
	Dark Vision
	Enhanced Senses
	Flight"""
		race_attacks="Slash - d4 + 6 Slashing DMG"
	elif character_subrace=="White Carapace":
		character_strength=character_strength+5
		character_speed=character_speed+4
		character_stamina=character_stamina+7
		character_agility=character_agility+4
		character_dexterity=character_dexterity+8
		character_constitution=character_constitution+5
		character_perception=character_perception+6
		character_intelligence=character_intelligence+5
		character_charisma=character_charisma+4
		character_stealth=character_stealth+3
		character_armour=8
		character_skills="""Tough Carapace
	Telepathic Links
	Hive Knowledge
	Dark Vision
	Enhanced Senses of Hearing and Smell
	Flight"""
		race_attacks="Slash - d4 + 6 Slashing DMG"
	elif character_subrace=="Yellow Carapace":
		character_strength=character_strength+5
		character_speed=character_speed+4
		character_stamina=character_stamina+7
		character_agility=character_agility+4
		character_dexterity=character_dexterity+8
		character_constitution=character_constitution+5
		character_perception=character_perception+5
		character_intelligence=character_intelligence+6
		character_mana=character_mana+5
		character_manapower=character_manapower+7
		character_charisma=character_charisma+4
		character_stealth=character_stealth+5
		character_armour=8
		character_skills="""Tough Carapace
	Hive Knowledge
	Dark Vision
	Enhanced Senses of Hearing and Smell
	Flight"""
		race_attacks="Slash - d4 + 6 Slashing DMG"
	elif character_subrace=="Black Carapace":
		character_strength=character_strength+8
		character_speed=character_speed+5
		character_stamina=character_stamina+8
		character_agility=character_agility+4
		character_dexterity=character_dexterity+7
		character_constitution=character_constitution+7
		character_perception=character_perception+4
		character_intelligence=character_intelligence+4
		character_charisma=character_charisma+4
		character_stealth=character_stealth+7
		character_armour=10
		character_skills="""Extra Tough Carapace
	Hive Knowledge
	Dark Vision
	Enhanced Senses of Hearing and Smell
	Flight"""
		race_attacks="Slash - d4 + 6 Slashing DMG"
	elif character_subrace=="Red Carapace":
		character_strength=character_strength+8
		character_speed=character_speed+5
		character_stamina=character_stamina+8
		character_agility=character_agility+4
		character_dexterity=character_dexterity+7
		character_constitution=character_constitution+9
		character_perception=character_perception+5
		character_intelligence=character_intelligence+5
		character_charisma=character_charisma+5
		character_stealth=character_stealth+3
		character_armour=12
		character_skills="""Spiked Carapace
	Hive Knowledge
	Dark Vision
	Enhanced Senses of Hearing and Smell
	Flight"""
		race_attacks="Slash - d4 + 6 Slashing DMG"
	elif character_subrace=="Purple Carapace":
		character_strength=character_strength+4
		character_speed=character_speed+6
		character_stamina=character_stamina+8
		character_agility=character_agility+6
		character_dexterity=character_dexterity+7
		character_constitution=character_constitution+5
		character_perception=character_perception+5
		character_intelligence=character_intelligence+7
		character_charisma=character_charisma+6
		character_stealth=character_stealth+3
		character_armour=8
		character_skills="""Tough Carapace
	Hive Knowledge
	Dark Vision
	Lower Caste Control
	Enhanced Senses of Hearing and Smell
	Flight"""
		race_attacks="Slash - d4 + 6 Slashing DMG"
	elif character_race=="Kitsune":
		character_strength=character_strength+4
		character_speed=character_speed+4
		character_stamina=character_stamina+6
		character_agility=character_agility+6
		character_dexterity=character_dexterity+6
		character_constitution=character_constitution+3
		character_perception=character_perception+5
		character_intelligence=character_intelligence+5
		character_mana=character_mana+5
		character_manapower=character_manapower+7
		character_charisma=character_charisma+2
		character_stealth=character_stealth+5
		character_skills="""Enhanced Senses
	Lvl1 Fire Magic
	Fox Transformation"""
		race_attacks="""Punch - d4 + 2 Bludgeoning DMG
	Slash (Partial Transformation) - d4 + 4 Slashing DMG
	Bite (Partial Transformation) - d6 + 4 Piercing DMG
	Bite (Fox Form) - d6 + 4 Piercing DMG
	Fire Ball - d4 + 4 FIRE DMG (Burn)
	Flame Breath - d6 + 6 FIRE DMG (Burn)"""
		race_worship="Movan"
	elif character_race=="Merrow":
		character_strength=character_strength+5
		character_speed=character_speed+7
		character_stamina=character_stamina+8
		character_agility=character_agility+9
		character_dexterity=character_dexterity+7
		character_constitution=character_constitution+7
		character_perception=character_perception+7
		character_intelligence=character_intelligence+5
		character_charisma=character_charisma+6
		character_stealth=character_stealth+7
		character_skills="""Aquatic
	Dark Vision"""
		race_attacks="Tail Slap - d4 + 6 Bludgeoning DMG"
		race_worship="Kivena"
	elif character_race=="Minotaur":
		character_strength=character_strength+8
		character_speed=character_speed+6
		character_stamina=character_stamina+8
		character_agility=character_agility+2
		character_dexterity=character_dexterity+4
		character_constitution=character_constitution+7
		character_perception=character_perception+2
		character_intelligence=character_intelligence+5
		character_charisma=character_charisma+4
		character_stealth=character_stealth+3
		character_armour=4
		character_skills="""Thick Skin
	Horns
	Enhanced Hearing"""
		race_attacks="""Punch - d4 + 5 Bludgeoning DMG
	Gore - d6 + 6 Piercing DMG"""
	elif character_race=="Nagual":
		character_strength=character_strength+4
		character_speed=character_speed+4
		character_stamina=character_stamina+6
		character_agility=character_agility+6
		character_dexterity=character_dexterity+6
		character_constitution=character_constitution+3
		character_perception=character_perception+5
		character_intelligence=character_intelligence+5
		character_mana=character_mana+5
		character_manapower=character_manapower+6
		character_charisma=character_charisma+2
		character_stealth=character_stealth+6
		character_skills="""Enhanced Senses
	Dark Vision
	Lvl1 Wind Magic
	Dog Transformation"""
		race_attacks="""Punch - d4 + 2 Bludgeoning DMG
	Slash (Partial Transformation) - d4 + 4 Slashing DMG
	Bite (Partial Transformation) - d6 + 4 Piercing DMG
	Bite (Dog Form) - d6 + 4 Piercing DMG
	Wind Spear - d4 + 4 AIR DMG (Suffocate)
	Whirling Tunnel - d6 + 6 AIR DMG (Suffocate)"""
		if character_world=="Unified":
			race_worship="Valira"
		else:
			race_worship="Hurüsh"
	elif character_race=="Ogre":
		character_strength=character_strength+7
		character_speed=character_speed+3
		character_stamina=character_stamina+7
		character_agility=character_agility+3
		character_dexterity=character_dexterity+5
		character_constitution=character_constitution+7
		character_perception=character_perception+4
		character_intelligence=character_intelligence+4
		character_charisma=character_charisma+4
		character_stealth=character_stealth+7
		character_armour=6
		character_skills="""Extra Thick Skin
	Dark Vision
	Enhanced Pain Tolerance"""
		race_attacks="""Punch - d4 + 6 Bludgeoning DMG
	Slash - d6 + 5 Slashing DMG"""
	elif character_race=="Ponaturi":
		character_strength=character_strength+6
		character_speed=character_speed+6
		character_stamina=character_stamina+7
		character_agility=character_agility+6
		character_dexterity=character_dexterity+4
		character_constitution=character_constitution+4
		character_perception=character_perception+4
		character_intelligence=character_intelligence+5
		character_charisma=character_charisma+2
		character_stealth=character_stealth+7
		character_skills="""Amphibious
	Dark Vision
	Seaside Knowledge
	Enhanced Pain Tolerance"""
		race_attacks="""Slash - d4 + 2 Slashing DMG
	Tail Slap - d6 + 3 Bludgeoning DMG"""
		race_worship="Inauri"
	elif character_race=="Quetzal":
		character_strength=character_strength+7
		character_speed=character_speed+6
		character_stamina=character_stamina+7
		character_agility=character_agility+6
		character_dexterity=character_dexterity+6
		character_constitution=character_constitution+8
		character_perception=character_perception+6
		character_intelligence=character_intelligence+5
		character_charisma=character_charisma+2
		character_stealth=character_stealth+2
		character_armour=15
		character_skills="""Flight
	Scale Armour
	Regeneration"""
		race_attacks="""Slash - d4 + 5 Slashing DMG
	Bite - d4 + 3 Piercing DMG
	Tail Slam - d4 + 2 Bludgeoning DMG"""
	elif character_race=="Redcap":
		character_strength=character_strength+4
		character_speed=character_speed+6
		character_stamina=character_stamina+7
		character_agility=character_agility+5
		character_dexterity=character_dexterity+5
		character_constitution=character_constitution+7
		character_perception=character_perception+4
		character_intelligence=character_intelligence+4
		character_charisma=character_charisma+2
		character_stealth=character_stealth+6
		character_skills="""Dark Vision
	Enhanced Pain Tolerance"""
		race_attacks="""Slash - d4 + 2 Slashing DMG
	Bite - d4 + 4 Piercing DMG"""
	elif character_race=="Rionnath":
		character_strength=character_strength+5
		character_speed=character_speed+5
		character_stamina=character_stamina+6
		character_agility=character_agility+5
		character_dexterity=character_dexterity+5
		character_constitution=character_constitution+4
		character_perception=character_perception+5
		character_intelligence=character_intelligence+5
		character_charisma=character_charisma+6
		character_stealth=character_stealth+4
		character_skills="""Photosynthesis
	Rionnu Communication"""
		race_attacks="Punch - d4 + 2 Bludgeoning DMG"
		race_worship="Elos & Ryali"
	elif character_race=="Satyr":
		character_strength=character_strength+4
		character_speed=character_speed+5
		character_stamina=character_stamina+6
		character_agility=character_agility+8
		character_dexterity=character_dexterity+7
		character_constitution=character_constitution+6
		character_perception=character_perception+5
		character_intelligence=character_intelligence+5
		character_charisma=character_charisma+6
		character_stealth=character_stealth+3
		character_skills="""Enhanced Sense of Hearing & Taste
	Climbing
	Musical Knowledge"""
		race_attacks="""Headbutt - d4 + 4 Bludgeoning DMG
	Punch - d4 + 2 Bludgeoning DMG
	Kick - d4 + 4 Bludgeoning DMG"""
	elif character_race=="Shurgan":
		character_strength=character_strength+8
		character_speed=character_speed+2
		character_stamina=character_stamina+8
		character_agility=character_agility+2
		character_dexterity=character_dexterity+5
		character_constitution=character_constitution+7
		character_perception=character_perception+3
		character_intelligence=character_intelligence+5
		character_charisma=character_charisma+5
		character_stealth=character_stealth+2
		character_armour=12
		character_skills="""Rock Armour
	Dark Vision
	Lava Regeneration"""
		race_attacks="""Punch - d4 + 6 Bludgeoning DMG (Burn)
	Slash - d6 + 6 Slashing DMG (Burn)
	Bite - d6 + 6 Piercing DMG (Burn)"""
		if character_world=="Unified":
			race_worship="Sharam"
		else:
			race_worship="Magarab"
	elif character_race=="Siren":
		character_strength=character_strength+3
		character_speed=character_speed+7
		character_stamina=character_stamina+4
		character_agility=character_agility+8
		character_dexterity=character_dexterity+5
		character_constitution=character_constitution+4
		character_perception=character_perception+7
		character_intelligence=character_intelligence+5
		character_charisma=character_charisma+6
		character_stealth=character_stealth+4
		character_skills="""Flight
	Dark Vision
	Arial Agility"""
		race_attacks="Slash - d4 + 4 Slashing DMG"
	elif character_race=="Strigoi":
		character_strength=character_strength+4
		character_speed=character_speed+3
		character_stamina=character_stamina+6
		character_agility=character_agility+6
		character_dexterity=character_dexterity+4
		character_constitution=character_constitution+7
		character_perception=character_perception+6
		character_intelligence=character_intelligence+6
		character_charisma=character_charisma+6
		character_stealth=character_stealth+7
		character_skills="""Dark Vision
	Thermal Camouflage
	Blood Drain
	Charm"""
		race_attacks="""Punch - d4 + 3 Bludgeoning DMG
	Slash - d4 + 5 Slashing DMG
	Bite - d4 + 4 Piercing DMG + Heal 1/2 Damage
	Mesmerize - Target must make an Intelligence or Charisma roll against either Intelligence or Charisma"""
		if character_world=="Unified":
			race_worship=""
		else:
			race_worship="Emolat"
	elif character_subrace=="Air Talis":
		character_strength=character_strength+5
		character_speed=character_speed+8
		character_stamina=character_stamina+5
		character_agility=character_agility+8
		character_dexterity=character_dexterity+5
		character_constitution=character_constitution+5
		character_perception=character_perception+5
		character_intelligence=character_intelligence+5
		character_mana=character_mana+7
		character_manapower=character_manapower+8
		character_charisma=character_charisma+5
		character_stealth=character_stealth+5
		character_skills="""Air Magic Immunity
	Lvl3 Air Magic"""
		race_attacks="""Punch - d4 + 2 Bludgeoning DMG
	Wind Spear - d4 + 4 AIR DMG (Suffocate) -2 Mana
	Whirling Tunnel - d6 + 6 AIR DMG (Suffocate) -4 Mana
	Wind Wall - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Sky Armour - +4 Armour Rating on self + 4 AIR DMG against physical contact (Suffocate) (3 turns) -6 Mana
	Cloud Charge - d4 + 4 AIR DMG (Suffocate) + 1/2 DMG nearby -6 Mana
	Tornado Blast - d6 + 6 AIR DMG (Suffocate) -8 Mana"""
	elif character_subrace=="Dark Talis":
		character_strength=character_strength+5
		character_speed=character_speed+5
		character_stamina=character_stamina+5
		character_agility=character_agility+5
		character_dexterity=character_dexterity+8
		character_constitution=character_constitution+5
		character_perception=character_perception+5
		character_intelligence=character_intelligence+5
		character_mana=character_mana+7
		character_manapower=character_manapower+8
		character_charisma=character_charisma+5
		character_stealth=character_stealth+8
		character_skills="""Dark Magic Immunity
	Lvl3 Dark Magic"""
		race_attacks="""Punch - d4 + 2 Bludgeoning DMG
	Shadow Sphere - d4 + 4 DARK DMG (Blind) -2 Mana
	Shrouding Shade - d6 + 6 DARK DMG (Blind) -4 Mana
	Midnight Shield - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Reflectionless Armour - +4 Armour Rating on self + 4 DARK DMG against physical contact (Blind) (3 turns) -6 Mana
	Shadow Bomb - d4 + 4 DARK DMG (Blind) + 1/2 DMG nearby -6 Mana
	Night Curtain - d6 + 6 DARK DMG (Blind) -8 Mana"""
	elif character_subrace=="Earth Talis":
		character_strength=character_strength+8
		character_speed=character_speed+5
		character_stamina=character_stamina+5
		character_agility=character_agility+5
		character_dexterity=character_dexterity+5
		character_constitution=character_constitution+8
		character_perception=character_perception+5
		character_intelligence=character_intelligence+5
		character_mana=character_mana+7
		character_manapower=character_manapower+8
		character_charisma=character_charisma+5
		character_stealth=character_stealth+5
		character_skills="""Earth Magic Immunity
	Lvl3 Earth Magic"""
		race_attacks="""Punch - d4 + 2 Bludgeoning DMG
	Rock Bolt - d4 + 4 EARTH DMG (Splinter) -2 Mana
	Sand Blast - d6 + 6 EARTH DMG (Splinter) -4 Mana
	Stone Shield - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Spiked Skin - +4 Armour Rating on self + 4 EARTH DMG against physical contact (Splinter) (3 turns) -6 Mana
	Boulder Blast - d4 + 4 EARTH DMG (Splinter) + 1/2 DMG nearby -6 Mana
	Scouring Cone - d6 + 6 EARTH DMG (Splinter) -8 Mana"""
	elif character_subrace=="Fire Talis":
		character_strength=character_strength+5
		character_speed=character_speed+5
		character_stamina=character_stamina+5
		character_agility=character_agility+5
		character_dexterity=character_dexterity+5
		character_constitution=character_constitution+5
		character_perception=character_perception+8
		character_intelligence=character_intelligence+5
		character_mana=character_mana+7
		character_manapower=character_manapower+8
		character_charisma=character_charisma+8
		character_stealth=character_stealth+5
		character_skills="""Fire Magic Immunity
	Lvl3 Fire Magic"""
		race_attacks="""Punch - d4 + 2 Bludgeoning DMG
	Fire Ball - d4 + 4 FIRE DMG (Burn) -2 Mana
	Flame Breath - d6 + 6 FIRE DMG (Burn) -4 Mana
	Burning Wall - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Inferno Armour - +4 Armour Rating on self + 4 FIRE DMG against physical contact (Burn) (3 turns) -6 Mana
	Flame Blast - d4 + 4 FIRE DMG (Burn) + 1/2 DMG nearby -6 Mana
	Cone of Fire - d6 + 6 FIRE DMG (Burn) -8 Mana"""
	elif character_subrace=="Light Talis":
		character_strength=character_strength+5
		character_speed=character_speed+5
		character_stamina=character_stamina+5
		character_agility=character_agility+5
		character_dexterity=character_dexterity+8
		character_constitution=character_constitution+5
		character_perception=character_perception+5
		character_intelligence=character_intelligence+8
		character_mana=character_mana+7
		character_manapower=character_manapower+8
		character_charisma=character_charisma+5
		character_stealth=character_stealth+5
		character_skills="""Light Magic Immunity
	Lvl3 Light Magic"""
		race_attacks="""Punch - d4 + 2 Bludgeoning DMG
	Blinding Ball - d4 + 4 LIGHT DMG (Blind) -2 Mana
	Shining Beam - d6 + 6 LIGHT DMG (Blind) -4 Mana
	Sunlight Shield - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Reflecting Armour - +4 Armour Rating on self + 4 LIGHT DMG against physical contact (Blind) (3 turns) -6 Mana
	Star Bomb - d4 + 4 LIGHT DMG (Blind) + 1/2 DMG nearby -6 Mana
	Shining Blast - d6 + 6 LIGHT DMG (Blind) -8 Mana"""
	elif character_subrace=="Water Talis":
		character_strength=character_strength+5
		character_speed=character_speed+5
		character_stamina=character_stamina+8
		character_agility=character_agility+5
		character_dexterity=character_dexterity+5
		character_constitution=character_constitution+5
		character_perception=character_perception+5
		character_intelligence=character_intelligence+5
		character_mana=character_mana+7
		character_manapower=character_manapower+8
		character_charisma=character_charisma+8
		character_stealth=character_stealth+5
		character_skills="""Water Magic Immunity
	Lvl3 Water Magic"""
		race_attacks="""Punch - d4 + 2 Bludgeoning DMG
	Aqua Ball - d4 + 4 WATER DMG (Sense Obscure) -2 Mana
	Torrential Blast - d6 + 6 WATER DMG (Sense Obscure) -4 Mana
	Water Wall - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Aquatic Armour - +4 Armour Rating on self + 4 WATER DMG against physical contact (Sense Obscure) (3 turns) -6 Mana
	Hydro Bomb - d4 + 4 WATER DMG (Sense Obscure) + 1/2 DMG nearby -6 Mana
	Tidal Stream - d6 + 6 WATER DMG (Sense Obscure) -8 Mana"""
	elif character_race=="Thrael":
		character_strength=character_strength+6
		character_speed=character_speed+7
		character_stamina=character_stamina+8
		character_agility=character_agility+7
		character_dexterity=character_dexterity+6
		character_constitution=character_constitution+5
		character_perception=character_perception+4
		character_intelligence=character_intelligence+5
		character_charisma=character_charisma+5
		character_stealth=character_stealth+7
		character_skills="""Amphibious
	Dark Vision"""
		race_attacks="""Punch - d4 + 2 Bludgeoning DMG"""
	elif character_subrace=="Mountain Troll":
		character_strength=character_strength+7
		character_speed=character_speed+3
		character_stamina=character_stamina+7
		character_agility=character_agility+3
		character_dexterity=character_dexterity+5
		character_constitution=character_constitution+7
		character_perception=character_perception+4
		character_intelligence=character_intelligence+4
		character_charisma=character_charisma+4
		character_stealth=character_stealth+7
		character_armour=6
		character_skills="""Extra Thick Skin
	Enhanced Pain Tolerance"""
		race_attacks="""Punch - d6 + 6 Bludgeoning DMG
	Grab - Target rolls Strength against Strength to escape, or remains immobilised"""
	elif character_subrace=="Cave Troll":
		character_strength=character_strength+7
		character_speed=character_speed+3
		character_stamina=character_stamina+7
		character_agility=character_agility+3
		character_dexterity=character_dexterity+5
		character_constitution=character_constitution+7
		character_perception=character_perception+4
		character_intelligence=character_intelligence+4
		character_charisma=character_charisma+4
		character_stealth=character_stealth+7
		character_armour=6
		character_skills="""Extra Thick Skin
	Dark Vision
	Enhanced Pain Tolerance"""
		race_attacks="""Punch - d6 + 6 Bludgeoning DMG
	Grab - Target rolls Strength against Strength to escape, or remains immobilised"""
	elif character_subrace=="Jungle Troll":
		character_strength=character_strength+7
		character_speed=character_speed+3
		character_stamina=character_stamina+7
		character_agility=character_agility+3
		character_dexterity=character_dexterity+5
		character_constitution=character_constitution+7
		character_perception=character_perception+4
		character_intelligence=character_intelligence+4
		character_charisma=character_charisma+4
		character_stealth=character_stealth+7
		character_armour=6
		character_skills="""Extra Thick Skin
	Camouflage
	Enhanced Pain Tolerance"""
		race_attacks="""Punch - d6 + 6 Bludgeoning DMG
	Grab - Target rolls Strength against Strength to escape, or remains immobilised"""
	elif character_subrace=="Snow Troll":
		character_strength=character_strength+7
		character_speed=character_speed+3
		character_stamina=character_stamina+7
		character_agility=character_agility+3
		character_dexterity=character_dexterity+5
		character_constitution=character_constitution+7
		character_perception=character_perception+4
		character_intelligence=character_intelligence+4
		character_charisma=character_charisma+4
		character_stealth=character_stealth+7
		character_armour=6
		character_skills="""Extra Thick Skin
	Camouflage
	Cold Tolerance
	Enhanced Pain Tolerance"""
		race_attacks="""Punch - d6 + 6 Bludgeoning DMG
	Grab - Target rolls Strength against Strength to escape, or remains immobilised"""
		race_worship="Ilisium"
	elif character_race=="Varah":
		character_strength=character_strength+7
		character_speed=character_speed+5
		character_stamina=character_stamina+8
		character_agility=character_agility+3
		character_dexterity=character_dexterity+4
		character_constitution=character_constitution+7
		character_perception=character_perception+4
		character_intelligence=character_intelligence+5
		character_charisma=character_charisma+4
		character_stealth=character_stealth+3
		character_armour=4
		character_skills="""Thick Skin
	Dark Vision
	Enhanced Smell"""
		race_attacks="""Punch - d4 + 4 Bludgeoning DMG
	Gore - d6 + 4 Piercing DMG"""
	elif character_race=="Vinori":
		character_strength=character_strength+7
		character_speed=character_speed+6
		character_stamina=character_stamina+7
		character_agility=character_agility+6
		character_dexterity=character_dexterity+4
		character_constitution=character_constitution+8
		character_perception=character_perception+7
		character_intelligence=character_intelligence+3
		character_charisma=character_charisma+1
		character_stealth=character_stealth+4
		character_armour=4
		character_skills="""Thick Skin
	Enhanced Senses
	Enhanced Pain Tolerance"""
		race_attacks="""Punch - d4 + 5 Bludgeoning DMG
	Slash - d6 + 5 Slashing DMG
	Bite - d4 + 7 Piercing DMG"""
	elif character_race=="Waheela":
		character_strength=character_strength+18
		character_speed=character_speed+11
		character_stamina=character_stamina+20
		character_agility=character_agility+9
		character_dexterity=character_dexterity+6
		character_constitution=character_constitution+100
		character_perception=character_perception+7
		character_intelligence=character_intelligence+10
		character_mana=character_mana+10
		character_manapower=character_manapower+8
		character_charisma=character_charisma+4
		character_stealth=character_stealth+4
		character_armour=6
		character_skills="""Extra Thick Skin
	Enhanced Senses
	Dark Vision
	Lvl3 Ice Magic"""
		race_attacks="""Slash - d12 + 10 Slahing DMG
	Bite - d12 + 12 Piercing DMG
	Stomp - d10 + 12 Bludgeoning DMG
	Ice Dart - d4 + 4 ICE DMG (Freeze) -2 Mana
	Frost Breath - d6 + 6 ICE DMG (Freeze) -4 Mana
	Ice Wall - +6 Armour Rating to self or ally (1 turn) -4 Mana
	Glacial Armour - +4 Armour Rating on self + 4 ICE DMG against physical contact (Freeze) (3 turns) -6 Mana
	Icicle Spear - d4 + 4 ICE DMG (Freeze) + 1/2 DMG nearby -6 Mana
	Blizzard Breath - d6 + 6 ICE DMG (Freeze) -8 Mana"""
	elif character_race=="Wulver":
		character_strength=character_strength+6
		character_speed=character_speed+7
		character_stamina=character_stamina+6
		character_agility=character_agility+4
		character_dexterity=character_dexterity+5
		character_constitution=character_constitution+7
		character_perception=character_perception+7
		character_intelligence=character_intelligence+5
		character_charisma=character_charisma+4
		character_stealth=character_stealth+3
		character_skills="""Enhanced Senses
	Fish Knowledge"""
		race_attacks="""Slash - d4 + 4 Slashing DMG
	Bite - d4 + 6 Piercing DMG"""
	elif character_race=="Yuki-Ona":
		character_strength=character_strength+4
		character_speed=character_speed+4
		character_stamina=character_stamina+6
		character_agility=character_agility+6
		character_dexterity=character_dexterity+6
		character_constitution=character_constitution+3
		character_perception=character_perception+5
		character_intelligence=character_intelligence+5
		character_mana=character_mana+5
		character_manapower=character_manapower+7
		character_charisma=character_charisma+2
		character_stealth=character_stealth+5
		character_skills="""Enhanced Senses
	Lvl1 Ice Magic"""
		race_attacks="""Punch - d4 + 2 Bludgeoning DMG
	Ice Dart - d4 + 4 ICE DMG (Freeze) -2 Mana
	Frost Breath - d6 + 6 ICE DMG (Freeze) -4 Mana"""
	
	if character_class=="Warrior":
		character_strength=character_strength+8
		character_speed=character_speed+2
		character_stamina=character_stamina+5
		character_constitution=character_constitution+5
		class_skills="Martial Weaponry"
	elif character_class=="Mage":
		character_dexterity=character_dexterity+4
		character_intelligence=character_intelligence+6
		character_mana=character_mana+10
		character_manapower=character_manapower+5
		character_manalevel=character_manalevel+1
		class_skills="Lvl"+str(character_manalevel)+" "+str(magic_type)+" Magic"
	elif character_class=="Scout":
		character_dexterity=character_dexterity+3
		character_speed=character_speed+3
		character_agility=character_agility+3
		character_perception=character_perception+3
		character_charisma=character_charisma+3
		character_stealth=character_stealth+5
		class_skills="""Ranged Weaponry
		Small Bladed Weaponry"""
	elif character_class=="Defender":
		character_strength=character_strength+4
		character_stamina=character_stamina+5
		character_agility=character_agility+1
		character_dexterity=character_dexterity+1
		character_constitution=character_constitution+9
		class_skills="Defensive Techniques"
	elif character_class=="Non-Combatant":
		character_strength=character_strength+1
		character_speed=character_speed+1
		character_stamina=character_stamina+1
		character_constitution=character_constitution+2

	if character_level != 5 or character_level != 10:
		character_strength=character_strength+character_level-1
		character_speed=character_speed+character_level-1
		character_agility=character_agility+character_level-1
		character_dexterity=character_dexterity+character_level-1
		character_constitution=character_constitution+character_level-1
	elif character_level=="5":
		if character_class=="Mage":
			character_strength=character_strength+4
			character_speed=character_speed+4
			character_agility=character_agility+4
			character_dexterity=character_dexterity+4
			character_constitution=character_constitution+4
			character_mana=character_mana+5
			character_manapower=character_manapower+5
			character_manalevel=character_manalevel+1
		else:
			character_strength=character_strength+4
			character_speed=character_speed+4
			character_agility=character_agility+4
			character_dexterity=character_dexterity+4
			character_constitution=character_constitution+4
	elif character_level=="10":
		if character_class=="Mage":
			character_strength=character_strength+9
			character_speed=character_speed+9
			character_agility=character_agility+9
			character_dexterity=character_dexterity+9
			character_constitution=character_constitution+9
			character_perception=character_perception+2
			character_intelligence=character_intelligence+2
			character_charisma=character_charisma+2
			character_stealth=character_stealth+2
			character_luck=character_luck+1
			character_mana=character_mana+10
			character_manapower=character_manapower+10
			character_manalevel=character_manalevel+1
		else:
			character_strength=character_strength+9
			character_speed=character_speed+9
			character_agility=character_agility+9
			character_dexterity=character_dexterity+9
			character_constitution=character_constitution+9
			character_perception=character_perception+2
			character_intelligence=character_intelligence+2
			character_charisma=character_charisma+2
			character_stealth=character_stealth+2
			character_luck=character_luck+1

	if character_subrace=="None":
		print("""
		Name: """+character_name+
		"""
		Species: """+character_race+
		"""
		Gender: """+character_gender+
		"""
		Age: """+character_age+
		"""
		Class: """+character_class+
		"""
		Occupation: """+character_role+
		"""
		Level: """+str(character_level)+
		"""
		XP: """+character_xp+
		"""

		Strength: """+str(character_strength)+
		"""
		Speed: """+str(character_speed)+
		"""
		Stamina: """+str(character_stamina)+
		"""
		Agility: """+str(character_agility)+
		"""
		Dexterity: """+str(character_dexterity)+
		"""
		Constitution: """+str(character_constitution)+
		"""
		Perception: """+str(character_perception)+
		"""
		Intelligence: """+str(character_intelligence)+
		"""
		Mana: """+str(character_mana)+
		"""
		Mana Power: """+str(character_manapower)+
		"""
		Charisma: """+str(character_charisma)+
		"""
		Stealth: """+str(character_stealth)+
		"""
		Luck: """+str(character_luck)+
		"""
		Armour Rating: """+str(character_armour)+
		"""

		Species Skills: """+str(character_skills)+"""
		Class Skills: """+str(class_skills)+"""
		Racial Attacks:"""+str(race_attacks)+"""
		Spells:"""+str(character_spells)+"""
		

		""")
		input("Press Enter to apply your skill modifiers")
	else:
		print("""
		Name: """+character_name+
		"""
		Species: """+character_race+
		"""
		Subspecies: """+character_subrace+
		"""
		Gender: """+character_gender+
		"""
		Age: """+character_age+
		"""
		Class: """+character_class+
		"""
		Occupation: """+character_role+
		"""
		Level: """+character_level+
		"""
		XP: """+character_xp+
		"""

		Strength: """+str(character_strength)+
		"""
		Speed: """+str(character_speed)+
		"""
		Stamina: """+str(character_stamina)+
		"""
		Agility: """+str(character_agility)+
		"""
		Dexterity: """+str(character_dexterity)+
		"""
		Constitution: """+str(character_constitution)+
		"""
		Perception: """+str(character_perception)+
		"""
		Intelligence: """+str(character_intelligence)+
		"""
		Mana: """+str(character_mana)+
		"""
		Mana Power: """+str(character_manapower)+
		"""
		Charisma: """+str(character_charisma)+
		"""
		Stealth: """+str(character_stealth)+
		"""
		Luck: """+str(character_luck)+
		"""
		Armour Rating: """+str(character_armour)+
		"""

		Species Skills: """+str(character_skills)+"""
		Class Skills: """+str(class_skills)+"""
		Racial Attacks:"""+str(race_attacks)+"""
		Spells:"""+str(character_spells)+"""

		""")
		input("Press Enter to apply your skill modifiers")

create_character_skill_sheet()

def modify_skills():
	cls()
	global character_strength, character_speed, character_stamina, character_agility, character_dexterity, character_constitution, character_perception, character_intelligence, character_charisma, character_stealth, character_mana, character_manapower, character_luck, character_armour, character_skills, class_skills, race_attacks, character_spells, magic_type, character_era, character_worship, race_worship, mage_worship
	print("To modify your skills, roll a 6-sided die for each of your skills, and the game will add your score to the relevant skill.")
	input("Press Enter to roll for Strength")
	roll=randint(1,6)
	print("You rolled: "+str(roll))
	character_strength=character_strength+roll
	input("Press Enter to roll for Speed")
	roll=randint(1,6)
	print("You rolled: "+str(roll))
	character_speed=character_speed+roll
	input("Press Enter to roll for Stamina")
	roll=randint(1,6)
	print("You rolled: "+str(roll))
	character_stamina=character_stamina+roll
	input("Press Enter to roll for Agility")
	roll=randint(1,6)
	print("You rolled: "+str(roll))
	character_agility=character_agility+roll
	input("Press Enter to roll for Dexterity")
	roll=randint(1,6)
	print("You rolled: "+str(roll))
	character_dexterity=character_dexterity+roll
	input("Press Enter to roll for Constitution")
	roll=randint(1,6)
	print("You rolled: "+str(roll))
	character_constitution=character_constitution+roll
	input("Press Enter to roll for Perception")
	roll=randint(1,6)
	print("You rolled: "+str(roll))
	character_perception=character_perception+roll
	input("Press Enter to roll for Intelligence")
	roll=randint(1,6)
	print("You rolled: "+str(roll))
	character_intelligence=character_intelligence+roll
	input("Press Enter to roll for Charisma")
	roll=randint(1,6)
	print("You rolled: "+str(roll))
	character_charisma=character_charisma+roll
	input("Press Enter to roll for Stealth")
	roll=randint(1,6)
	print("You rolled: "+str(roll))
	character_stealth=character_stealth+roll
	input("Press Enter to roll for Luck")
	roll=randint(1,10)
	print("You rolled: "+str(roll))
	character_luck=character_luck+roll
	if character_class=="Mage":
		print("Press Enter to roll for Mana")
		roll=randint(1,10)
		print("You rolled: "+str(roll))
		character_mana=character_mana+roll
		print("Press Enter to roll for Mana Power")
		roll=randint(1,6)
		print("You rolled: "+str(roll))
		character_manapower=character_manapower+roll
	input("Press Enter to continue...")
	cls()
	if character_subrace=="None":
		print("""
		Congratulations! You have completed your character creation!
		Your final character sheet is:

		Name: """+character_name+
		"""
		Species: """+character_race+
		"""
		Gender: """+character_gender+
		"""
		Age: """+character_age+
		"""
		Class: """+character_class+
		"""
		Occupation: """+character_role+
		"""
		Level: """+str(character_level)+
		"""
		XP: """+character_xp+
		"""

		Strength: """+str(character_strength)+
		"""
		Speed: """+str(character_speed)+
		"""
		Stamina: """+str(character_stamina)+
		"""
		Agility: """+str(character_agility)+
		"""
		Dexterity: """+str(character_dexterity)+
		"""
		Constitution: """+str(character_constitution)+
		"""
		Perception: """+str(character_perception)+
		"""
		Intelligence: """+str(character_intelligence)+
		"""
		Mana: """+str(character_mana)+
		"""
		Mana Power: """+str(character_manapower)+
		"""
		Charisma: """+str(character_charisma)+
		"""
		Stealth: """+str(character_stealth)+
		"""
		Luck: """+str(character_luck)+
		"""
		Armour Rating: """+str(character_armour)+
		"""

		Species Skills: """+str(character_skills)+"""
		Class Skills: """+str(class_skills)+"""
		Racial Attacks:"""+str(race_attacks)+"""
		Spells:"""+str(character_spells)+"""
		
		""")
		input("Press Enter to save!")
	else:
		print("""
		Congratulations! You have completed your character creation!
		Your final character sheet is:

		Name: """+character_name+
		"""
		Species: """+character_race+
		"""
		Subspecies: """+character_subrace+
		"""
		Gender: """+character_gender+
		"""
		Age: """+character_age+
		"""
		Class: """+character_class+
		"""
		Occupation: """+character_role+
		"""
		Level: """+str(character_level)+
		"""
		XP: """+character_xp+
		"""

		Strength: """+str(character_strength)+
		"""
		Speed: """+str(character_speed)+
		"""
		Stamina: """+str(character_stamina)+
		"""
		Agility: """+str(character_agility)+
		"""
		Dexterity: """+str(character_dexterity)+
		"""
		Constitution: """+str(character_constitution)+
		"""
		Perception: """+str(character_perception)+
		"""
		Intelligence: """+str(character_intelligence)+
		"""
		Mana: """+str(character_mana)+
		"""
		Mana Power: """+str(character_manapower)+
		"""
		Charisma: """+str(character_charisma)+
		"""
		Stealth: """+str(character_stealth)+
		"""
		Luck: """+str(character_luck)+
		"""
		Armour Rating: """+str(character_armour)+
		"""

		Species Skills: """+str(character_skills)+"""
		Class Skills: """+str(class_skills)+"""
		Racial Attacks:"""+str(race_attacks)+"""
		Spells:"""+str(character_spells)+"""

		""")
		input("Press Enter to save!")

modify_skills()

def save_file():
		f = open(r"character.txt", mode = "r+")
		f.write("""
Name: """+character_name+"""
Species: """+character_race+"""
Subspecies: """+character_subrace+"""
Gender: """+character_gender+"""
Age: """+character_age+"""
Class: """+character_class+"""
Occupation: """+character_role+"""
Level: """+str(character_level)+"""
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

# def subspecremove(): #Not working yet. Not sure why - Rowanas
# 	f = open(r"character.txt", mode = "r+")
# 	d = f.readlines()
# 	f.seek(0)
# 	for i in d:
# 		if i != "Subspecies: None":
# 			f.write(i)
# 	f.close

# subspecremove()

save_file()
