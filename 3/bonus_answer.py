#! /usr/bin/env python

import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('input')

options = parser.parse_args()

input_text = open("./" + options.input, 'r')

contents = input_text.read().strip().split('\n')

def find_trees(lines, rise, run):
    horiz_pos = 0
    vert_pos = 0
    tree_count = 0

    while vert_pos < len(lines):
        line = lines[vert_pos]
        if horiz_pos >= len(line):
            horiz_pos -= len(line)
        
        if line[horiz_pos] == '#':
            tree_count += 1

        horiz_pos += run
        vert_pos += rise

    return tree_count

run1 = find_trees(contents, 1, 1)
run2 = find_trees(contents, 1, 3)
run3 = find_trees(contents, 1, 5)
run4 = find_trees(contents, 1, 7)
run5 = find_trees(contents, 2, 1)

print "Trees Encountered (run 1): " + str(run1)
print "Trees Encountered (run 2): " + str(run2)
print "Trees Encountered (run 3): " + str(run3)
print "Trees Encountered (run 4): " + str(run4)
print "Trees Encountered (run 5): " + str(run5)

print "Multiplied: " + str(run1 * run2 * run3 * run4 * run5)