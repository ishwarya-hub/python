class empolyee:
    company = "Google"
    
    
    @classmethod
    def change_company(cls, new_name):
        cls.company=new_name
        
        
empolyee.change_company("Amazon")
print(empolyee.company)
        
        