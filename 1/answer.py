#! /usr/bin/env python

import sys
import argparse
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument('input')

options = parser.parse_args()

input_text = open("./" + options.input, 'r')

contents = input_text.read().split('\n')



for line in contents:
    for subline in contents:
        if line == '' or subline == '' or line == subline:
            continue
        if (int(line) + int (subline)) == 2020:
            print int(line) * int (subline)
            exit