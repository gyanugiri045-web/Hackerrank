students = []

def add_studennt():
    try:
      name = input("Enter student name:")
      grade = int(input("Enter student grade:"))
      roll = int(input("Enter student roll :"))

      marks = []

      print("Enter 5 subject:")

      for i in range(5):
         mark = int(input(f"subject {i + 1}:"))
         marks.append(mark)

         student = {
            "name":name,
            "grade":grade,
            "marks":mark,
            "roll":roll
         }

         students.append(student)

         print("Studnet added successfully!!")

    except ValueError:
       print("Please enter number only!!")

def view_student():
   if len(view_student) == 0:
      print("Invalid number!!")
      return
   
   for student in students:
      print("student name:",student["name"])
      print("roll number:", student["roll"])
      print("marks:", student["marks"])



add_studennt()
view_student()

    
         






