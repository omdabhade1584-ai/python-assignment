#Q2.Create a lambda function to calculate the square of a number.
# Accept a number from the user and display its square.
square_lambda = lambda num : num ** 2
num=int(input("Enter a number:"))
print("Square of number using lambda function:",square_lambda(num))
