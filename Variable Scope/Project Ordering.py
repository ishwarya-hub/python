# Project Using the varible Scope

develivery="Swiggy"

def order():
    order="pizza"

    def quantity():
        quantity=2
        print(f"order{order}no of quantity{quantity}using{develivery}")
    quantity()

order()

print(__file__)
