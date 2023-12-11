"""
Advent of Code - Day 3: Gear Ratios
"""

# load data file
with open("input.txt", "r") as input:
    engine_schematic = input.read()
    engine_schematic = engine_schematic.splitlines()


# function to return index of all special characters in a string
def index_of_special_characters(string):
    index_list = []
    for char_index, char in enumerate(string):
        if not char.isnumeric() and char != ".":
            index_list.append(char_index)
    return index_list


# function to return list of numbers found in a string along with positions
def track_numbers(string):
    numbers_list = []
    numbers_index = []

    for char_index, char in enumerate(string):
        if char.isnumeric():
            if char_index == 0:
                numbers_list.append(char)
                numbers_index.append([char_index])
            elif string[char_index - 1].isnumeric():
                numbers_list[-1] += char
                numbers_index[-1].append(char_index)
            else:
                numbers_list.append(char)
                numbers_index.append([char_index])

    return numbers_list, numbers_index


# function to return positions of * symbol
def index_of_gear(string):
    index_list = []
    for char_index, char in enumerate(string):
        if char == "*":
            index_list.append(char_index)
    return index_list


###########
# Part One
###########
sum_of_all_part_numbers = 0

for line_index, line in enumerate(engine_schematic):
    num_list, num_index = track_numbers(line)

    symbols_index = []
    if line_index != 0:
        symbols_above = index_of_special_characters(engine_schematic[line_index - 1])
        symbols_index.extend(symbols_above)
    symbols_line = index_of_special_characters(line)
    if len(symbols_line) > 0:
        symbols_index.extend(symbols_line)
    if line_index != len(engine_schematic) - 1:
        symbols_below = index_of_special_characters(engine_schematic[line_index + 1])
        symbols_index.extend(symbols_below)
    symbols_index = set(symbols_index)

    for i, index in enumerate(num_index):
        for symb in symbols_index:
            if int(symb) >= max(0, int(index[0]) - 1) and int(symb) <= min(
                int(index[-1]) + 1, len(line) - 1
            ):
                sum_of_all_part_numbers += int(num_list[i])
                break

print(sum_of_all_part_numbers)

###########
# Part Two
###########
sum_of_all_gear_ratios = 0

for line_index, line in enumerate(engine_schematic):
    gear_index = index_of_gear(line)
    nums_in_line, nums_in_line_index = track_numbers(line)
    if line_index != 0:
        nums_above, nums_above_index = track_numbers(engine_schematic[line_index - 1])
    if line_index != len(engine_schematic) - 1:
        nums_below, nums_below_index = track_numbers(engine_schematic[line_index + 1])

    for gear in gear_index:
        part_numbers = []
        if line_index != 0:
            for i, num in enumerate(nums_above):
                if int(gear) >= max(0, int(nums_above_index[i][0]) - 1) and int(
                    gear
                ) <= min(int(nums_above_index[i][-1]) + 1, len(line) - 1):
                    part_numbers.append(int(num))
        if line_index != len(engine_schematic) - 1:
            for i, num in enumerate(nums_below):
                if int(gear) >= max(0, int(nums_below_index[i][0]) - 1) and int(
                    gear
                ) <= min(int(nums_below_index[i][-1]) + 1, len(line) - 1):
                    part_numbers.append(int(num))
        for i, num in enumerate(nums_in_line):
            if int(gear) >= max(0, int(nums_in_line_index[i][0]) - 1) and int(
                gear
            ) <= min(int(nums_in_line_index[i][-1]) + 1, len(line) - 1):
                part_numbers.append(int(num))

        if len(part_numbers) == 2:
            sum_of_all_gear_ratios += part_numbers[0] * part_numbers[1]

print(sum_of_all_gear_ratios)
