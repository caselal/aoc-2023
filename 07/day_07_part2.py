"""
Advent of Code - Day 7: Camel Cards
"""

###########
# Part Two
###########

with open("input.txt", "r") as input:
    puzzle_input = input.read()
    puzzle_input = puzzle_input.splitlines()

card_values = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}
types = {
    "five_of_a_kind": 7,
    "four_of_a_kind": 6,
    "full_house": 5,
    "three_of_a_kind": 4,
    "two_pair": 3,
    "one_pair": 2,
    "high_card": 1,
}

all_hands = {}
for item in puzzle_input:
    hand_and_bid = item.split(" ")
    hand, bid = hand_and_bid[0], int(hand_and_bid[1])

    unique_cards = set(hand)
    number_unique_cards = len(unique_cards)

    card_count = [hand.count(card) for card in unique_cards]
    max_count = max(card_count)

    match number_unique_cards:
        case 1:
            hand_type, strength = "five_of_a_kind", 7
        case 2:
            if max_count == 4:
                if "J" in hand:
                    hand_type, strength = "five_of_a_kind", 7
                else:
                    hand_type, strength = "four_of_a_kind", 6
            else:
                if "J" in hand:
                    hand_type, strength = "five_of_a_kind", 7
                else:
                    hand_type, strength = "full_house", 5
        case 3:
            if max_count == 3:
                if "J" in hand:
                    hand_type, strength = "four_of_a_kind", 6
                else:
                    hand_type, strength = "three_of_a_kind", 4
            else:
                if "J" in hand:
                    if hand.count("J") == 1:
                        hand_type, strength = "full_house", 5
                    else:
                        hand_type, strength = "four_of_a_kind", 6
                else:
                    hand_type, strength = "two_pair", 3
        case 4:
            if "J" in hand:
                hand_type, strength = "three_of_a_kind", 4
            else:
                hand_type, strength = "one_pair", 2
        case _:
            if "J" in hand:
                hand_type, strength = "one_pair", 2
            else:
                hand_type, strength = "high_card", 1

    all_hands[hand] = {"bid": bid, "hand_type": hand_type, "strength": strength}


all_hands_sorted = dict(
    sorted(
        all_hands.items(),
        key=lambda x: (
            x[1]["strength"],
            card_values.get(x[0][0]),
            card_values.get(x[0][1]),
            card_values.get(x[0][2]),
            card_values.get(x[0][3]),
            card_values.get(x[0][4]),
        ),
    )
)

total_winnings = 0
for i, key in enumerate(all_hands_sorted.keys()):
    total_winnings += (i + 1) * all_hands_sorted.get(key).get("bid")

print(total_winnings)
