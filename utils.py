import random
"""
{die_amount} amount of d{die_type} dice a total of {time} times
"""
def roll(die_amount, die_type, times):
	return [
		sum([random.randint(1, die_type) for x in range(0, die_amount)])
		for x in range(0, times)
	]