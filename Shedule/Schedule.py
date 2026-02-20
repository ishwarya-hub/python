import sys

#if len(sys.argv)==2:
fullname=sys.argv[1:]
email=fullname.lower().replace(" ",".")+"@company.com"

print("\n----- your profile----")
print("Full Name:",fullname)
print("Email ID:",email)