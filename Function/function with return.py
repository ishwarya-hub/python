def create_profile(**kwargs):
    print("User profile created successfully")
    for i in range(0,5):
        for key, value in kwargs.items():
            print(f"{key}: {value}")

create_profile(name=input("Enter name: "), age=21)
 