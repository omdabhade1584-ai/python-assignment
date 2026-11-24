#Q1. Function Scope and Built-in Functions (2 Marks)
#Write a function analyze_numbers() that accepts a list of numbers and displays:
#1. Maximum value
#2. Minimum value
#3. Sum of all values
#4. Average value
def analyse_numbers(numbers):
 print("Maximun Value in List:",max(numbers))
 print("Minimun Value in List:",min(numbers))
 print("Sum of all values in List:",sum(numbers))
 print("Average value of List:",sum(numbers)/len(numbers))

n=int(input("Enter num of a elements in a list:"))
numbers=[]
for i in range(n):
 num=int(input("Enter a number:"))
 numbers.append(num)
print(numbers)
analyse_numbers(numbers)
