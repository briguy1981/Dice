'''
User input dice roll generator
What is the die number you want to roll?
how many dice do you want to roll"

'''

import random
from random import randint


def final_num(dice, rolls):
    results = 0
    final_num = 0
    for i in range(0,rolls):
        results = random.randint(dice, rolls)
        print("The %d die rolled %d." % (i + rolls, results))
        return final_num

# What number die do you want to roll?
dice = int(input("What size die would like to roll?"))

# how many times do you want it rolled?
rolls = int(input("How many dice do want rolled?"))

results = final_num(dice, rolls)
print(results)