"""
Advent of Code - Day 1: Science for Hungry People
"""

# load data file
with open("input.txt", "r") as input:
    calibration_document = input.read()
    text = calibration_document.splitlines()

###########
# Part One
###########
sum_of_all_calibration_values = 0

for line in text:
    number = ""
    for i in line:
        if i.isnumeric():
            number += i
    final_number = int(number[0] + number[-1])
    sum_of_all_calibration_values += final_number

print(sum_of_all_calibration_values)


###########
# Part Two
###########
sum_of_all_calibration_values = 0

valid_digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def find_digit(i, input_string):
    digit = ""
    if input_string[i].isnumeric():
        digit = input_string[i]
    else:
        match input_string[i : i + 2]:
            case "on":
                digit = "1"
            case "tw":
                digit = "2"
            case "th":
                digit = "3"
            case "fo":
                digit = "4"
            case "fi":
                digit = "5"
            case "si":
                digit = "6"
            case "se":
                digit = "7"
            case "ei":
                digit = "8"
            case "ni":
                digit = "9"
    return digit


def find_number(input_string):
    string = input_string
    number = ""
    index_list = []

    for char_index, char in enumerate(string):
        if char.isnumeric():
            index_list.append(char_index)

    valid_digits_list = list(valid_digits.keys())

    for digit in valid_digits_list:
        start = 0
        for i in range(len(string)):
            digit_index = string.find(digit, start)
            if digit_index != -1:
                index_list.append(string.find(digit, start))
                start = digit_index + 1
            else:
                pass

    index_list.sort()

    number = find_digit(index_list[0], string) + find_digit(index_list[-1], string)

    return number


for line in text:
    number = int(find_number(line))
    sum_of_all_calibration_values += number

print(sum_of_all_calibration_values)
