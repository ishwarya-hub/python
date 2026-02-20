class student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade    
        
    def name(self):
        print("my name is",self.name)
        
    def grade(self):
        print("my grade is",self.grade)
        
s1=student("nithish","112")
s1.name()
s1.grade()
  