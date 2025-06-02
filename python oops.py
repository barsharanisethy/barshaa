class barsha:
    n="name"
    
s=barsha()
print(s.n)
#constructor
class student:
    college="sparsh college"#college name same for all of the student so that it will not write in the init constructor
    #default constructor
    # def __init__(self):
    #paramterized constructor
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
        print("adding new name into the function")
        #methods
    
    def child(self):
            print("hello")
        
        
s1=student("swati",45)
print(s1.name)
s1.child()

s2=student("barshaa",33)
print(s2.name,s2.marks)
print(s2.college)
