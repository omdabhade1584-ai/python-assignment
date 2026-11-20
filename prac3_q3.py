# Q3. Write a program that:
# • Generates a random number between 1 and 100.
# • Finds its square root using the math module
import math
import random
r_num=random.randint(1,100)
sq_rt=math.sqrt(r_num)
print("Random Number generated:",r_num)
print("Square root of that Random number:",sq_rt)