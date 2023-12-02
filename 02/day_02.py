"""
Advent of Code - Day 2:
"""
import numpy as np

# load data file
with open("input.txt", "r") as input:
    game_records = input.read()
    game_records = game_records.splitlines()

###########
# Part One
###########
total_cubes = {"red": 12, "green": 13, "blue": 14}
sum_of_game_ids = 0

list_of_game_ids = []


for game in game_records:
    possible_sets = []
    game_number = int(game.split(": ")[0].split(" ")[1])
    sets = game.split(": ")[1].split("; ")

    for set in sets:
        set_cubes = set.split(", ")
        set_length = len(set_cubes)

        i = 0
        while i < set_length:
            if int(set_cubes[i].split(" ")[0]) <= total_cubes.get(
                set_cubes[i].split(" ")[1]
            ):
                possible_sets.append(1)
            else:
                possible_sets.append(0)
            i += 1

    if all(p == 1 for p in possible_sets):
        sum_of_game_ids += game_number

print(sum_of_game_ids)


###########
# Part Two
###########
sum_of_power_sets = 0

for game in game_records:
    cubes_dict = {"red": 0, "blue": 0, "green": 0}
    game_number = int(game.split(": ")[0].split(" ")[1])
    sets = game.split(": ")[1].split("; ")

    for set in sets:
        set_cubes = set.split(", ")
        set_length = len(set_cubes)

        i = 0
        while i < set_length:
            if cubes_dict.get(set_cubes[i].split(" ")[1]) < int(
                set_cubes[i].split(" ")[0]
            ):
                cubes_dict[set_cubes[i].split(" ")[1]] = int(set_cubes[i].split(" ")[0])
            i += 1

    power = np.prod(list(cubes_dict.values()))
    sum_of_power_sets += power

print(sum_of_power_sets)
