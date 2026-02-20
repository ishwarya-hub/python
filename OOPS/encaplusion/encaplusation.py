class order:
    def __init__(self,customer_name,item,total,discount):
        self.customer_name=customer_name
        self.item=item
        self.__total=total
        self.__discount=discount
        
    def __calculator(self):
        return self.__total - self.__discount
    
    def _get_admin(self):
        return {
            "custommer": self.customer_name,
            "items":self.item,
            "total_amount":f"{self.__total}",
            "discount_applied":f"{self.__discount}",
            "final_bill":f"{self.__calculator()}"            
        }
        
    def get_customer(self):
        return{
            "custommer": self.customer_name,
            "items":self.item,
            "fianl_bill":f"{self.__calculator()}"
        }
        
class admin_portal:
    
    def show_order(self,order):
        return order._get_admin()

class customer:
    
    def show_order(self,order):
        return order.get_customer()         
    

order= order(customer_name="John Doe",item=["pizza","bugger"],total=600,discount=150)
admin=admin_portal()
customer=customer()

print("Admin View:")
print(admin.show_order(order))
print("\nCustomer View:")
print(customer.show_order(order))
    