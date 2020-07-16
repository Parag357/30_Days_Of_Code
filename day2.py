import math
import os
import random
import re
import sys

def solve(m, t1, t2):
     print(int(round(m+(m*t1/100)+(m*t2/100))))
if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
