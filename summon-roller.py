#code used for the variant: summon X monsters.

"""
This code takes in 3 command line arguments: the amount of monsters using this feature, the chance that it will summon a monster, and the die used to summon it
Monster amount: int
Summon chance: int, 1-100, it represents a percentage chance
Summon Die: string, described in a (x)d(y) where x is the number of dice used, and y is the type of die (1d4, 2d6, 3d20, etc.)
"""
import random
import sys
from utils import roll

monster_amount = int(sys.argv[1])
summon_chance = int(sys.argv[2])

summon_die_arg = sys.argv[3].split("d")
summon_die_amount = int(summon_die_arg[0])
summon_die = int(summon_die_arg[1])

sucesses = filter(lambda x: x<summon_chance, roll(1, 100, monster_amount))

summons = roll(summon_die_amount, summon_die, len(sucesses))

print("Total sucesses: {}".format(len(sucesses)))
print("Summon amounts: {}".format(summons))
print("Total summons: {}".format(sum(summons)))

	
