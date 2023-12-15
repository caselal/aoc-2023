"""
Advent of Code - Day 6: Wait For It
"""

# load data file
with open("input.txt", "r") as input:
    paper = input.read()
    race_information = paper.splitlines()


# function to remove whitespace from string and add numeric values to a list
def parse_race_info(input_list):
    return [int(value) for value in input_list if value != ""]


# function to remove whitespace from string and add numeric values to a list
def parse_race_info_part2(input_list):
    new_string = ""
    return int(new_string.join(value for value in input_list if value != ""))


###########
# Part One
###########
time = parse_race_info(race_information[0].split(": ")[1].strip().split(" "))
distance = parse_race_info(race_information[1].split(": ")[1].strip().split(" "))

number_of_ways = 1

for i, t in enumerate(time):
    beat_record_count = 0
    for ms in range(t + 1):
        distance_traveled = ms * (t - ms)
        if distance_traveled > distance[i]:
            beat_record_count += 1
    number_of_ways *= beat_record_count

print(number_of_ways)

###########
# Part Two
###########
time = parse_race_info_part2(race_information[0].split(": ")[1].strip().split(" "))
distance = parse_race_info_part2(race_information[1].split(": ")[1].strip().split(" "))

number_of_ways = 0

for ms in range(time + 1):
    distance_traveled = ms * (time - ms)
    if distance_traveled > distance:
        number_of_ways += 1
print(number_of_ways)
