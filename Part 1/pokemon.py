import os, csv
import itertools
from PIL import Image 

_TYPE_MATRIX = (                                                                     # v Attack
#   Nor Fig Fly Poi Gro Roc Bug Gho Ste Fir Wat Gra Ele Psy Ice Dra Dar Fai ??? None # < Defend
    (1,  1,  1,  1,  1, .5,  1,  0, .5,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1), # NORMAL
    (2,  1, .5, .5,  1,  2, .5,  0,  2,  1,  1,  1,  1, .5,  2,  1,  2, .5,  1,  1), # FIGHTING
    (1,  2,  1,  1,  1, .5,  2,  1, .5,  1,  1,  2, .5,  1,  1,  1,  1,  1,  1,  1), # FLYING
    (1,  1,  1, .5, .5, .5,  1, .5,  0,  1,  1,  2,  1,  1,  1,  1,  1,  2,  1,  1), # POISON
    (1,  1,  0,  2,  1,  2, .5,  1,  2,  2,  1, .5,  2,  1,  1,  1,  1,  1,  1,  1), # GROUND
    (1, .5,  2,  1, .5,  1,  2,  1, .5,  2,  1,  1,  1,  1,  2,  1,  1,  1,  1,  1), # ROCK
    (1, .5, .5, .5,  1,  1,  1, .5, .5, .5,  1,  2,  1,  2,  1,  1,  2, .5,  1,  1), # BUG
    (0,  1,  1,  1,  1,  1,  1,  2,  1,  1,  1,  1,  1,  2,  1,  1, .5,  1,  1,  1), # GHOST
    (1,  1,  1,  1,  1,  2,  1,  1, .5, .5, .5,  1, .5,  1,  2,  1,  1,  2,  1,  1), # STEEL
    (1,  1,  1,  1,  1, .5,  2,  1,  2, .5, .5,  2,  1,  1,  2, .5,  1,  1,  1,  1), # FIRE
    (1,  1,  1,  1,  2,  2,  1,  1,  1,  2, .5, .5,  1,  1,  1, .5,  1,  1,  1,  1), # WATER
    (1,  1, .5, .5,  2,  2, .5,  1, .5, .5,  2, .5,  1,  1,  1, .5,  1,  1,  1,  1), # GRASS
    (1,  1,  2,  1,  0,  1,  1,  1,  1,  1,  2, .5, .5,  1,  1, .5,  1,  1,  1,  1), # ELECTRIC
    (1,  2,  1,  2,  1,  1,  1,  1, .5,  1,  1,  1,  1, .5,  1,  1,  0,  1,  1,  1), # PSYCHIC
    (1,  1,  2,  1,  2,  1,  1,  1, .5, .5, .5,  2,  1,  1, .5,  2,  1,  1,  1,  1), # ICE
    (1,  1,  1,  1,  1,  1,  1,  1, .5,  1,  1,  1,  1,  1,  1,  2,  1,  0,  1,  1), # DRAGON
    (1, .5,  1,  1,  1,  1,  1,  2,  1,  1,  1,  1,  1,  2,  1,  1, .5, .5,  1,  1), # DARK
    (1,  2,  1, .5,  1,  1,  1,  1, .5, .5,  1,  1,  1,  1,  1,  2,  2,  1,  1,  1), # FAIRY
    (1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1), # None
#   Nor Fig Fly Poi Gro Roc Bug Gho Ste Fir Wat Gra Ele Psy Ice Dra Dar Fai ??? None # < Defend
)                                                                                    # ^ Attack

_INDEXES = {'Normal': 0, 'Fighting': 1, 'Flying': 2, 'Poison': 3, 'Ground': 4,
            'Rock': 5, 'Bug': 6, 'Ghost': 7, 'Steel': 8, 'Fire': 9, 'Water': 10,
            'Grass': 11, 'Electric': 12, 'Psychic': 13, 'Ice': 14, 'Dragon': 15,
            'Dark': 16, 'Fairy': 17, 'None': 18}

def type_matchup(atk_type, def_type):
    return _TYPE_MATRIX[_INDEXES[atk_type]][_INDEXES[def_type]]

def find_weakness(type1, type2):
    weaknesses = []
    for type in _INDEXES:
        if type_matchup(type, type1)*type_matchup(type,type2) > 1.0:
            weaknesses.append(type)
    return weaknesses


###############################################################################


INPUT = csv.reader(open("pokemon.csv"))#, quoting=csv.QUOTE_NONNUMERIC)

class pokedex(object):

	# initializer
	def __init__(self, file):
		self.input = file
		self.file = csv.reader(open(file))
		next(self.file)

	# opens csv file
	def reset(self):
		self.file = csv.reader(open(self.input))
		next(self.file)

	# returns a list of pokemon of a given type
	def type_search(self, type):
		type_match = []
		for row in self.file:
			if type == row[2] or type == row[3]:
				type_match.append(row[1])
		return type_match

	# returns a set of pokemon with values higher than the given value for any given statistic
	def stat_search(self, stat, value):
		stat_match = {}
		for row in self.file:
			if stat == "Total":
				if value <= int(row[4]):
					stat_match[row[1]] = int(row[4])
			elif stat == "HP":
				if value <= int(row[5]):
					stat_match[row[1]] = int(row[5])
			elif stat == "Attack": 
				if value <= int(row[6]):
					stat_match[row[1]] = int(row[6])
			elif stat == "Defense":
				if value <= int(row[7]): 
					stat_match[row[1]] = int(row[7])
			elif stat == "Sp. Atk":
				if value <= int(row[8]): 
					stat_match[row[1]] = int(row[8])
			elif stat == "Sp. Def":
				if value <= int(row[9]):
					stat_match[row[1]] = int(row[9])
		return stat_match

	# return a list of legendary pokemon
	def legend_search(self):
		legend_match = []
		for row in self.file:
			if row[12] == "True":
				legend_match.append(row[1])
		return legend_match 

	# given a pokemon name, print all known statistics and information
	def pokemon_search(self, name):
		for row in self.file: 
			if name == row[1]:
				return row
		print("Pokemon not found")

	# given a pokemon number, print all known statistics and information
	def number_search(self, number):
		for row in self.file: 
			if number == row[0]:
				return row
		print("Pokemon number not found")


	# given a pokemon name, open corresponding png image
	def image_search(self, pokemon):
		file = "Images/" + pokemon.lower() + ".png"
		img = Image.open(file)
		img.show()

	# return list of types that are super effective against a given pokemon
	def stronger_type_search(self, pokemon):
		type1 = None
		type2 = None
		for row in self.file: 
			if pokemon == row[1]:
				type1 = row[2]
				type2 = row[3]
		if type2 == '': type2 = 'None'
		set = find_weakness(type1, type2)
		return set

	# return list of pokemon that are stronger against a given pokemon based on stats
	def stronger_stat_search(self, pokemon):
		total = 0
		opponents = []
		for row in self.file:
			if pokemon == row[1]:
				total = int(row[4])
		self.reset()
		for row in self.file:
			if total < int(row[4]):
				opponents.append(row[1])
		return opponents

	# returns list of pokemon that are as strong or weaker than a given pokemon based on stats
	def weaker_stat_search(self, pokemon):
		all_pokemon = []
		for row in self.file:
			all_pokemon.append(row[1])
		self.reset()
		stronger_pokemon = self.stronger_stat_search(pokemon)
		return list(set(all_pokemon) - set(stronger_pokemon))

	# based on stats AND type, return list of pokemon that are stronger than a given pokemon
	def stronger_pokemon_search(self, pokemon):
		stronger_pokemon = []
		opponents = self.stronger_stat_search(pokemon)
		self.reset()
		types = self.stronger_type_search(pokemon)
		for type in types:
			for opponent in opponents:
				self.reset()
				op = self.pokemon_search(opponent)
				type1 = op[2]
				type2 = op[3]
				if type1 == type or type2 == type:
					stronger_pokemon.append(opponent)
		return stronger_pokemon









