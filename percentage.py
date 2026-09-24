student = {
    "ram" : [50, 30, 70],
    "shyam" : [10, 40 , 20]
}

student_name = input("Enter a name of studnet:")

n = student[student_name]
total = sum(n)
print(f"The average of {student_name} is  {total/3}")