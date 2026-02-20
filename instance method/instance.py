class myclass:
    
    def instance_method(self):
        print("called instance")
        
    @classmethod
    def class_method(cls):
        print("called class method")

    @staticmethod
    def static_method():
        print("called static method")

obj = myclass()
obj.instance_method()
myclass.class_method()
myclass.static_method()
    