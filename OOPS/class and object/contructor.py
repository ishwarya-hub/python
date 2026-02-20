class id:
    def __init__(self,name,ide):
        self.x=ide
        self.y=name
        
    def name(self):
        print("my name:",self.y)
        
    def ide(self):
        print("my ide:",self.x)
     
     
s1=id(input(),int(input()))
#s2=id(input(),int(input()))
s1.name()
s1.ide()
#s2.name()                   
#s2.ide()                
        
        
