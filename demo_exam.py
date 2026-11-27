import datetime
import threading
import time
import grade


# Q1: Student class with constructor

class Student:

    def __init__(self, rollno, name, marks):

        self.rollno = rollno
        self.name = name
        self.set_marks(marks)

        # Q6: Store admission date
        self.admission_date = datetime.datetime.now()

    # Q3: Setter method

    def set_marks(self, marks):

        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")

        self.__marks = marks

    # Q3: Getter method

    def get_marks(self):

        return self.__marks

    # Q4: Calculate grade using method and external grade module

    def calculate_grade(self):

        return grade.calculate_grade(self.get_marks())

    # Q2: Display student details

    def display_details(self):

        print("\n------ STUDENT DETAILS ------")

        print("Roll Number:", self.rollno)
        print("Name:", self.name)
        print("Marks:", self.get_marks())
        print("Grade:", self.calculate_grade())

        print("Admission Date:",
              self.admission_date.strftime("%d-%m-%Y"))

    # Q8: Report generation using threading

    def generate_report(self):

        print("\nGenerating student report...")

        time.sleep(3)

        print("Student report generated successfully!")


# Q5: Exception handling

try:

    rollno = int(input("Enter Roll Number: "))

    name = input("Enter Student Name: ")

    marks = float(input("Enter Student Marks: "))

    # Q2: Create student object

    student = Student(rollno, name, marks)

    # Display details

    student.display_details()

    # Q3: Demonstrate getter and setter

    print("\nUpdating student marks...")

    student.set_marks(90)

    print("Updated Marks:", student.get_marks())

    print("Updated Grade:", student.calculate_grade())

    # Q8: Create thread for report generation

    t1 = threading.Thread(
        target=student.generate_report
    )

    t1.start()

    t1.join()

    print("\nMain program completed successfully!")


except ValueError as e:

    print("\nInvalid Input:", e)