#code used for summm
import random
import sys

def roll(amount, die_amount, die_type):
	return [
		sum([random.randint(1, die_type) for x in range(0, die_amount)])
		for x in range(0, amount)
	]

monster_amount = int(sys.argv[1])
summon_chance = int(sys.argv[2])

summon_die_arg = sys.argv[3].split("d")
summon_die_amount = int(summon_die_arg[0])
summon_die = int(summon_die_arg[1])

print(roll(10, 2, 6))
sucesses = filter(lambda x: x<summon_chance, roll(monster_amount, 1, 100))

summons = roll(len(sucesses), summon_die_amount, summon_die)

print("Total sucesses: {}".format(len(sucesses)))
print("Summon amounts: {}".format(summons))
print("Total summons: {}".format(sum(summons)))

	
