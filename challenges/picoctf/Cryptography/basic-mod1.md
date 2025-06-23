#!/usr/bin/env python3

numbers = [350, 63, 353, 198, 114, 369, 346, 184, 202, 322, 94, 235, 114, 110, 185, 188, 225, 212, 366, 374, 261, 213]

def to_char(num):
    if num < 26:
        return chr(ord('A') + num)
    elif num < 36:
        return str(num - 26)
    elif num == 36:
        return '_'
    else:
        raise ValueError("Number must be between 0 and 36")

characters = [to_char(num % 37) for num in numbers]

print("".join(characters))
