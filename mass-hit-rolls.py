import sys
from utils import roll

monster_amount = int(sys.argv[1])
attack_bonus = int(sys.argv[2])
average_damage = int(sys.argv[3])
ac = int(sys.argv[4])

attack_rolls = roll(1, 20, monster_amount)
add_attack_bonus = map(lambda x: x + attack_bonus, attack_rolls)

hits = filter(lambda x: x >= ac, add_attack_bonus)

damage = average_damage * len(hits)

print(attack_rolls)
print(add_attack_bonus)
print(hits)
print("Total damage: {}".format(damage))