import string
import random
import time


# Syntax for color text: "\033[{YOUR_COLOR}m" #! Replace {YOUR_COLOR} with the color code you want to use 
# At the end of the string (after the "m") you can start typing your text

# Possible Colors 
'''
Default	0
Black	30
Red	31
Green	32
Yellow	33
Blue	34
Purple	35
Cyan	36
White	37
'''
goal = "Hello World" 
compare_string = ""
letters = list(string.ascii_letters)
letters.append(" ")
colors = [31,32,33,34,35,36,37]
r = ''
index = 0
while True:
    letter = random.choice(letters)
    color = random.choice(colors)
    if letter == goal[index]:
        compare_string += letter
        r+= f"\033[{color}m{letter}"
        index += 1
    if compare_string == goal:
        print(r)
        break  
    print(r + f"\033[{color}m{letter}") 
    time.sleep(0.02) 