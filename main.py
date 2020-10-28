#LAB 1, VARIANT 4
#Maxim Pupykin, group 6312

import re
correct_numbers = []

with open("phone-numbers", "r") as numbers:
    contents = numbers.read()
    strings_1 = re.findall(r"\D9\d{9}\D", contents)
    strings_2 = re.findall(r"\D8\d{10}\D", contents)
    strings_3 = re.findall(r"\D7\d{10}\D", contents)

for string in strings_1:
    correct_numbers.append(string[1:11])
for string in strings_2:
    correct_numbers.append(string[1:12])
for string in strings_3:
    correct_numbers.append(string[1:12])

with open("correct-numbers", "w") as numbers:
    for number in correct_numbers:
        numbers.write(number + "\n")