n= int(input("Enter the n: "))
number = 2

if n < 2:
    print("Nothing")
else:
    while number <= n:
        print(number, end=" ")
        number += 2