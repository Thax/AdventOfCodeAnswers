#! /usr/bin/env python

import sys
import argparse
import string

def validate_byr(byr_val):
    if len(byr_val) != 4:
        return False
    try:
        int_byr_val = int(byr_val)
    except ValueError:
        return False
    
    if int_byr_val >= 1920 and int_byr_val <= 2002:
        return True

def validate_iyr(iyr_val):
    if len(iyr_val) != 4:
        return False
    try:
        int_iyr_val = int(iyr_val)
    except ValueError:
        return False
    
    if int_iyr_val >= 2010 and int_iyr_val <= 2020:
        return True

def validate_eyr(eyr_val):
    if len(eyr_val) != 4:
        return False
    try:
        int_eyr_val = int(eyr_val)
    except ValueError:
        return False
    
    if int_eyr_val >= 2020 and int_eyr_val <= 2030:
        return True

def validate_hgt(hgt_val):
    if len(hgt_val) > 5 or len(hgt_val) < 4:
        return False

    hgt_units = hgt_val[-2:]
    try:
        hgt_number = int(hgt_val[:-2])
    except ValueError:
        return False

    if (hgt_units == 'cm'):
        if (hgt_number >= 150 and hgt_number <= 193):
            return True

        return False
    if (hgt_units == 'in'):
        if (hgt_number >= 59 and hgt_number <= 76):
            return True

        return False

    return False

def validate_hcl(hcl_val):
    if len(hcl_val) != 7:
        return False

    if hcl_val[0] != '#':
        return False

    return all(character in string.hexdigits for character in hcl_val[1:])

def validate_ecl(ecl_val):
    allowed_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return ecl_val in allowed_ecl

def validate_pid(pid_val):
    if (len(pid_val) != 9):
        return False

    try:
        int(pid_val)
        return True
    except ValueError:
        return False

 
validators = {
    'byr' : validate_byr,
    'iyr' : validate_iyr,
    'eyr' : validate_eyr,
    'hcl' : validate_hcl,
    'hgt' : validate_hgt,
    'ecl' : validate_ecl,
    'pid' : validate_pid
}

def passport_valid(passport_fields):
    
    required_fields = ['byr', 'iyr', 'eyr', 'hcl', 'hgt', 'ecl', 'pid']

    for field in passport_fields:
        
        field_name = field.split(":")[0]
        field_val  = field.split(":")[1]
        if (field_name in required_fields):
            required_fields.remove(field_name)
            if (not validators[field_name](field_val)):
                return False


    return len(required_fields) == 0

def main():
    
    parser = argparse.ArgumentParser()

    parser.add_argument('input')

    options = parser.parse_args()

    input_text = open("./" + options.input, 'r')

    lines = input_text.read().strip().split('\n\n')

    required_fields_count = 7
    good_passport_count = 0

    for line in lines:
        fields = line.split()
        if len(fields) < required_fields_count:
            continue

        print fields    
        if passport_valid(fields):
            good_passport_count += 1

    print "Good Passports: " + str(good_passport_count)

main()