#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

number_abs = abs(number)

last_digit = number_abs % 10

end_str = ""

if last_digit > 5:
    end_str = "and is greater then 5"
elif last_digit == 0:
    end_str = "and is 0"
else:
    end_str = "and is less than 6 and not 0"

print("Last digit of {} is {} {}".format(number, last_digit, end_str))
