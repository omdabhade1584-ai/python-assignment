# Q4. Employee Salary Calculator using Function Arguments (4 Marks)
# Create a function:
# calculate_salary(basic_salary, bonus=2000)
# The function should calculate and display:
# Total Salary = Basic Salary + Bonus
# Demonstrate the use of:
# • Positional Arguments
# • Keyword Arguments
# • Default Arguments
def calculate_salary(basic_salary, bonus=2000):
   total_salary=basic_salary+bonus
   return total_salary
emp_1=calculate_salary(85000,4500)#1.Positional Argument
emp_2=calculate_salary(bonus=5000, basic_salary=70000,)#2.Keyword Argument
emp_3=calculate_salary(90737)#3.Default Argument (bonus defaults to 2000)
print("Employee 1 Salary: ",emp_1)
print("Employee 2 Salary: ",emp_2)
print("Employee 3 Salary: ",emp_3)