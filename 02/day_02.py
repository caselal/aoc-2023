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

for game in game_records:
    is_possible = True
    game_string, sets = game.split(": ")
    game_number = int(game_string.split(" ")[1])

    for set in sets.split("; "):
        set_cubes = set.split(", ")

        for cubes in set_cubes:
            count, color = cubes.split(" ")
            if int(count) > total_cubes.get(color):
                is_possible = False

    if is_possible:
        sum_of_game_ids += game_number

print(sum_of_game_ids)


###########
# Part Two
###########
sum_of_power_sets = 0

for game in game_records:
    cubes_dict = {"red": 0, "blue": 0, "green": 0}
    game_string, sets = game.split(": ")
    game_number = int(game_string.split(" ")[1])

    for set in sets.split("; "):
        set_cubes = set.split(", ")

        for cubes in set_cubes:
            count, color = cubes.split(" ")
            cubes_dict[color] = max(cubes_dict.get(color), int(count))

    power = np.prod(list(cubes_dict.values()))
    sum_of_power_sets += power

print(sum_of_power_sets)
