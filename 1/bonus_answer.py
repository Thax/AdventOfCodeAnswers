#! /usr/bin/env python

import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('input')

options = parser.parse_args()

input_text = open("./" + options.input, 'r')

contents = input_text.read().split('\n')

target = 2020

for line in contents:
    for subline in contents:
        if line == '' or subline == '' or line == subline:
            continue
        first_two = int(line) + int (subline)
        if first_two < target:
            for subsubline in contents:
                if (subsubline == ''):
                    continue
                total = first_two + int(subsubline)
                if (total == target):
                    print line + " * " + subline + " * " + subsubline + " = " + str(int(line) * int (subline) * int (subsubline))
                    exit()