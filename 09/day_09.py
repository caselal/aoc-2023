"""
Advent of Code - Day 9: Mirage Maintenance
"""

with open("input.txt", "r") as input:
    report = input.read()
    report = report.splitlines()

for i, history in enumerate(report):
    report[i] = [int(value) for value in history.split(" ")]


# function to determine a sequence of differences for an input sequence
def find_one_difference(input_sequence):
    return [
        input_sequence[i] - input_sequence[i - 1]
        for i, num in enumerate(input_sequence[1:], 1)
    ]


# function to determine all sequences of differences, until all differences are zero
def find_all_differences(input_sequence):
    new_sequence = input_sequence
    all_sequences = [new_sequence]

    while all(value == new_sequence[0] for value in new_sequence) is False:
        new_sequence = find_one_difference(new_sequence)
        all_sequences.append(new_sequence)

    return all_sequences


###########
# Part One
###########
sum_of_extrapolated_values = 0
for history in report:
    all_sequences = find_all_differences(history)
    next_value = 0

    for sequence in all_sequences:
        next_value += sequence[-1]

    sum_of_extrapolated_values += next_value

print(sum_of_extrapolated_values)

###########
# Part Two
###########
sum_of_backwards_extrapolated_values = 0
for history in report:
    next_value = 0
    all_sequences = find_all_differences(history)

    for i, sequence in enumerate(all_sequences):
        if i % 2 == 0:
            next_value += sequence[0]
        else:
            next_value -= sequence[0]

    sum_of_backwards_extrapolated_values += next_value

print(sum_of_backwards_extrapolated_values)
