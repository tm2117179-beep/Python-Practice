num=int(input("Enter a num: "))
if(num>0):
    if(num<=10):
        print("number is between 1 to 10 and also equal to 10")
    elif(num>10 and num<=20):
        print("Number is between 1 to 20 and also equal to 20")
    else:
        print("number is above 20 ") 
elif(num<0):
    print("number is negative")
else:
    print("number is zero")
