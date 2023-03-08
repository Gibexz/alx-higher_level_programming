#!/usr/bin/python3
import random
number = random.randint(-10, 10)

end_str = ""

if number > 0:
    end_str = "is positive"
elif number == 0:
    end_str = "is zero"
else:
    end_str = "is negative"

print("{} {}".format(number, end_str))
