class Student:

    def __init__(self,name):
        self.name = name
        self.__marks = []

    def add_marks(self, marks):
        if not isinstance(marks, (int, float)):
            raise TypeError("Mars must be numbers")
        if marks < 0  or marks > 100:
            raise ValueError("Marks must be in between 0-100.") 
        
    def average(self):
        if not self.__marks:
            return 0
        
        return sum(self.__marks)/ len(self.__marks)
    
    def get_marks(self):
        return list(self.__marks)
    
    def __str__(self):
        return f"{self.name}: {self.__marks} (avg: {self.average():.2f})"
    

s = Student("Reyan")
s.add_marks(85)
s.add_marks(92)
s.add_marks(78)

print(s)                
print(s.average())       

try:
    s.add_marks(150)
except ValueError as e:
    print("Error:", e)   