#! /usr/bin/env python

import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('input')

options = parser.parse_args()

input_text = open("./" + options.input, 'r')

lines = input_text.read().strip().split('\n')

rise = 1
run = 3
horiz_pos = 0
vert_pos = 0
tree_count = 0

for line in lines:
    if horiz_pos >= len(line):
        horiz_pos -= len(line)
    
    if line[horiz_pos] == '#':
        tree_count += 1

    horiz_pos += run
    vert_pos += rise

print "Trees Encountered: " + str(tree_count)