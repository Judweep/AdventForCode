# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 00:35:42 2020

@author: Judith
"""


import re

input = open("C:\\Users\\Judith\\Documents\\AdventForCode\\day4_input.txt", "r"). readlines()
lst = []
entry = ""

for line in input:
    if  not re.match("^\n", line):
        entry += line
    else:
        lst.append(entry)
        entry = ""
lst.append(entry)

# file = [" ".join(element) for element in lst]
file = lst

regex_byr = re.compile(r"byr:(19[^01]\d|200[012])\s")
regex_iyr = re.compile(r"iyr:20(1\d|20)\s")
regex_eyr = re.compile(r"eyr:20(2\d|30)\s")
regex_hgt = re.compile(r"hgt:(1([5678]\d|9[0123])cm|(59|6\d|7[^789])in)\s")
regex_hcl = re.compile(r"hcl:#[\dabcdef]{6}\s")
regex_ecl = re.compile(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)\s")
regex_pid = re.compile(r"pid:\d{9}\s")
regex_lst = [regex_byr, regex_iyr, regex_eyr, regex_hgt, regex_hcl, regex_ecl, regex_pid]
                       
valid = 0
for person in file:
    if all([field in person for field in ["iyr", "ecl", "byr", "hcl", "eyr", "hgt", "pid"]]):
        if all([re.search(pattern, person) for pattern in regex_lst]):
            valid += 1

print(f"Out of {len(file)} entries, {valid} are valid")

