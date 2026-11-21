# Q5. Map, Filter and Reduce (4 Marks)
# Given:
# numbers = [1,2,3,4,5,6,7,8,9,10]
# Perform the following operations:
# 1. Use map() to generate squares of all numbers.
# 2. Use filter() to extract even numbers.
# 3. Use reduce() to calculate the sum of all numbers.
# Display all results.
from functools import reduce
numbers = [1,2,3,4,5,6,7,8,9,10]
squared= list(map(lambda x:x ** 2, numbers))
print("Square using map fun:",squared)
evens= list(filter(lambda x:x % 2 == 0, numbers))
print("Evens using Filter fun:",evens)
all_sum=reduce(lambda x,y:x+y, numbers)
print("Sum of list using reduce fun:",all_sum)