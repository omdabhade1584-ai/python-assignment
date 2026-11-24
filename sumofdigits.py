a=int(input("Enter a number:"))

sum=0

while a > 0:
    digit = a % 10
    sum += digit
    a = a // 10

print("Sum of digits =", sum)