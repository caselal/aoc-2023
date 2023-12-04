"""
Advent of Code - Day 4: Scratchcards
"""

# load data file
with open("input.txt", "r") as input:
    scratchcards = input.read()
    scratchcards = scratchcards.splitlines()


def remove_whitespace(input_list):
    return [num.strip() for num in input_list if num != ""]


###########
# Part One
###########
total_points_all_scratchcards = 0

for scratchcard in scratchcards:
    total_points_card = 0

    all_numbers = scratchcard.split(": ")[1].split(" | ")
    winning_numbers = remove_whitespace(all_numbers[0].split(" "))
    elf_numbers = remove_whitespace(all_numbers[1].split(" "))

    winning_numbers_set = set(winning_numbers)
    elf_numbers_set = set(elf_numbers)
    matching_numbers = winning_numbers_set & elf_numbers_set

    if len(matching_numbers) > 0:
        total_points_card = 2 ** (len(matching_numbers) - 1)

    total_points_all_scratchcards += total_points_card

print(total_points_all_scratchcards)


###########
# Part Two
###########
total_scratchcards = 0
scratchcard_counts = {}
all_matching_numbers = {}

for scratchcard in scratchcards:
    card = int(scratchcard.split(": ")[0].split(" ")[-1])
    scratchcard_counts[card] = 1

    all_numbers = scratchcard.split(": ")[1].split(" | ")
    winning_numbers = remove_whitespace(all_numbers[0].split(" "))
    elf_numbers = remove_whitespace(all_numbers[1].split(" "))

    winning_numbers_set = set(winning_numbers)
    elf_numbers_set = set(elf_numbers)
    matching_numbers = winning_numbers_set & elf_numbers_set
    all_matching_numbers[card] = matching_numbers

for scratchcard in scratchcards:
    card = int(scratchcard.split(": ")[0].split(" ")[-1])

    for i, num in enumerate(all_matching_numbers.get(card)):
        if scratchcard_counts.get(card + i + 1) is None:
            pass
        else:
            scratchcard_counts[card + i + 1] += scratchcard_counts.get(card)

print(sum(scratchcard_counts.values()))
