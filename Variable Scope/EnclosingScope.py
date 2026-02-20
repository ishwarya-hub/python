#Enclosing Scope Variable

def card():
    discount=10
    def checkout():
        print("Applying ",discount)
    checkout()
card()
