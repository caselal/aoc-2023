"""
Advent of Code - Day 4: Scratchcards
"""

# load data file
with open("input.txt", "r") as input:
    scratchcards = input.read()
    scratchcards = scratchcards.splitlines()


#
def remove_whitespace(input_list):
    strnum_list = input_list
    new_list = []
    for strnum in strnum_list:
        if strnum != "":
            new_list.append(strnum.strip())
    return new_list


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
scratchcard_dict = {}

for scratchcard in scratchcards:
    card = int(scratchcard.split(": ")[0].split(" ")[-1])
    scratchcard_dict[card] = 1

for scratchcard in scratchcards:
    card = int(scratchcard.split(": ")[0].split(" ")[-1])
    all_numbers = scratchcard.split(": ")[1].split(" | ")
    winning_numbers = remove_whitespace(all_numbers[0].split(" "))
    elf_numbers = remove_whitespace(all_numbers[1].split(" "))

    winning_numbers_set = set(winning_numbers)
    elf_numbers_set = set(elf_numbers)
    matching_numbers = winning_numbers_set & elf_numbers_set

    if len(matching_numbers) > 0:
        i = 1
        for index, num in enumerate(matching_numbers):
            if scratchcard_dict.get(card + i) is None:
                pass
            else:
                scratchcard_dict[card + i] += scratchcard_dict.get(card)
                i += 1

print(sum(scratchcard_dict.values()))
