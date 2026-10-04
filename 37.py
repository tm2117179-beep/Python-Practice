n=int(input("Enter a number:"))
if(n<=1):
    print("Not Prime")
else: 
    number=2
    while(n>=number):
        if(n%number==0):
           print("Not prime")
           break
        number=number+2   
    else:
        print("Prime")

