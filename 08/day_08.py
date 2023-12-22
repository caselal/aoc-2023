"""
Advent of Code - Day 8: Haunted Wasteland
"""
from math import gcd
from functools import reduce
import numpy as np

with open("input.txt", "r") as input:
    documents = input.read()
    documents = documents.splitlines()

instructions = documents[0]
network = documents[2:]


def split_node_information(input_string):
    string = input_string.split(" = ")
    node = string[0]
    next_element = string[1][1:-1]
    left_element, right_element = next_element.split(", ")
    return node, left_element, right_element


nodes = {}
for line in network:
    node, left, right = split_node_information(line)
    nodes[node] = {"L": left, "R": right}


# function to determine next element
def next_node(input_node, direction):
    return nodes.get(input_node).get(direction)


# function to calculate LCM
def calculate_lcm(numbers):
    lcm = numbers[0]
    for i in range(1, len(numbers)):
        lcm = lcm * numbers[i] // gcd(lcm, numbers[i])
    return lcm


# function to calculate LCM
def calculate_lcm2(denominators):
    return reduce(lambda a, b: a * b // gcd(a, b), denominators)


###########
# Part One
###########
steps = 0
current_node = "AAA"
while current_node != "ZZZ":
    current_node = next_node(current_node, instructions[steps % len(instructions)])
    steps += 1

print(steps)

###########
# Part Two
###########
all_steps = []
starting_nodes = {node: node for node in nodes.keys() if node[-1] == "A"}
current_nodes = starting_nodes

for node in current_nodes:
    step = 0
    while node[-1] != "Z":
        node = next_node(node, instructions[step % len(instructions)])
        step += 1

    all_steps.append(step)

print(np.lcm.reduce(all_steps))
# print(calculate_lcm(all_steps))
# print(calculate_lcm2(all_steps))
