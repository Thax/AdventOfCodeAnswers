#! /usr/bin/env python

import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('input')

options = parser.parse_args()

input_text = open("./" + options.input, 'r')

lines = input_text.read().strip().split('\n\n')

required_fields_count = 7
good_passport_count = 0

def validate_byr(byr_val):
    try:
        int_byr_val = int(byr_val)
    except ValueError:
        return false
    
    if int_byr_val > 1920 and int_byr_val < 2002:
        return true

validators = ['byr' => validate_byr]


for line in lines:
    fields = line.split()
    if len(fields) < required_fields_count:
        continue

    required_fields = ['byr', 'iyr', 'eyr', 'hcl', 'hgt', 'ecl', 'pid']
    for field in fields:
        print field
        field_name = field.split(":")[0]
        if (field_name in required_fields):
            required_fields.remove(field_name)

    if len(required_fields) == 0:
        good_passport_count += 1

print "Good Passports: " + str(good_passport_count)
