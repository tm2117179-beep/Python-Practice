n=int(input("Enter the n: "))
if(n<0):
    print("Factorial is not defined for negative number")
else:
    factorial=1
    number=1
while(number<=n):
    factorial=factorial*number
    number=number+1
 
print("factorial is: ",factorial)        