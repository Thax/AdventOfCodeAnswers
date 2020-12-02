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
        if (int(line) + int (subline)) == target:
            print line + " * " + subline + " = " + str(int(line) * int (subline))
            exit()