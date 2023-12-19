"""
Advent of Code - Day 5: If You Give A Seed A Fertilizer
"""

with open("input.txt", "r") as input:
    almanac = input.read()
    almanac = almanac.split("\n\n")


def remove_whitespace(input_list):
    return [item for item in input_list if item != ""]


def line_split(input_line):
    split_line = input_line.split(" ")
    return int(split_line[0]), int(split_line[1]), int(split_line[2])


seeds = [int(value) for value in (almanac[0].split(": ")[1].split(" "))]

almanac_list = []
for section in almanac[1:]:
    map = section.split(":")
    lines = remove_whitespace(map[1].split("\n"))
    lines = [line_split(line) for line in lines]
    almanac_list.append(lines)

###########
# Part One
###########
lowest_location_number = float("inf")

for seed in seeds:
    destination_number = seed

    for section in almanac_list:
        for line in section:
            source_start, destination_start, range_length = line[1], line[0], line[2]
            source_end = source_start + range_length - 1

            if destination_number >= source_start and destination_number <= source_end:
                destination_number = (
                    destination_number - source_start + destination_start
                )
                break

    lowest_location_number = min(lowest_location_number, destination_number)

print(lowest_location_number)


###########
# Part Two
###########
almanac_list_reversed = list(reversed(almanac_list))

current_destination_number = 0
while True:
    destination_number = current_destination_number
    seed_found = False

    for section in almanac_list_reversed:
        for line in section:
            source_start, destination_start, range_length = line[1], line[0], line[2]
            source_end = source_start + range_length - 1

            if (
                destination_number >= destination_start
                and destination_number < destination_start + range_length
            ):
                destination_number = (
                    destination_number - destination_start + source_start
                )
                break

    for i, s in enumerate(seeds[::2]):
        if (destination_number >= s) and (destination_number < s + seeds[2 * i + 1]):
            print(current_destination_number)
            seed_found = True
            break

    if seed_found:
        break

    current_destination_number += 1
