#LAB 1, VARIANT 4
#Maxim Pupykin, group 6312

import re
correct_numbers = []

with open("phone-numbers.txt", "r") as numbers:
    for number in numbers:
        if re.fullmatch(r"9\d{2}-?\d{3}-?\d{2}-?\d{2}\D?", number):
            correct_numbers.append(number)
        elif re.fullmatch(r"\(9\d{2}\)\d{3}-?\d{2}-?\d{2}\D?", number):
            correct_numbers.append(number)
        elif re.fullmatch(r"8\(\d{3}\)\d{3}-?\d{2}-?\d{2}\D?", number):
            correct_numbers.append(number)
        elif re.fullmatch(r"8-?\d{3}-?\d{3}-?\d{2}-?\d{2}\D?", number):
            correct_numbers.append(number)
        elif re.fullmatch(r"\+?7\(\d{3}\)\d{3}-?\d{2}-?\d{2}\D?", number):
            correct_numbers.append(number)
        elif re.fullmatch(r"\+?7-?\d{3}-?\d{3}-?\d{2}-?\d{2}\D?", number):
            correct_numbers.append(number)

with open("correct-numbers.txt", "w") as numbers:
    for number in correct_numbers:
        numbers.write(number)
