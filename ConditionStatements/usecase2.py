order=1000
days="sat"
membership='no'

if(order>=1000 and days in['sat','sun'])or membership=='gold':
    print("20% discount")

else:
    print("no discount")