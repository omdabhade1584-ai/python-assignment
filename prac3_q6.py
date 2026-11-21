# Q6. Decorator Implementation (3 Marks)
# Create a decorator named execution_time() that:
# Displays a message before function execution.
# Executes the function.
# Displays a message after function execution.
# Apply this decorator to a function that calculates the factorial of a number.
import math
def execution_time(func):
  def wrapper(n):
    print("Function Started")
    result=func(n)
    print("Factorial:",result)
    print("Function Finished")
  return wrapper
@execution_time
def calculate_factorial(n):
    return math.factorial(n)
calculate_factorial(5)
