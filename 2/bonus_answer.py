#! /usr/bin/env python

import sys
import argparse
import os
sys.path.append(os.path.abspath('../'))
from Helpers import string_helpers

parser = argparse.ArgumentParser()

parser.add_argument('input')

options = parser.parse_args()

input_text = open("./" + options.input, 'r')

contents = input_text.read().split('\n')

good_passwords = 0

check_string = ""

for line in contents:
    if line == '':
        continue
    # print line
    index_1 = int(line[0:string_helpers.find_index_of_character(line, '-')]) - 1
    index_2 = int(line[string_helpers.find_index_of_character(line, '-') + 1:string_helpers.find_index_of_character(line, ' ')]) - 1
    target = line[string_helpers.find_index_of_character(line, ':')-1:string_helpers.find_index_of_character(line, ':')]
    password = line[string_helpers.find_index_of_character(line, ':') + 2:]
    
    if ((password[index_1] == target) ^ (password[index_2] == target)):
        good_passwords += 1

print "Good Passwords: " + str(good_passwords)