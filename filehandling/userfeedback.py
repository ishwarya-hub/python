feedback=input("enter the feedback:")
with open ("feedback.txt","a") as file:
    file.write(feedback + "\n")
print("thank you")    