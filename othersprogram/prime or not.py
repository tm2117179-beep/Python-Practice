n = int(input("Enter n: "))

if n <= 1:
    print("Not prime")
else:
    num = 2
    while num < n:
        if n % num == 0:
            print("Not prime")
            break
        num += 1
    else:
        print("Prime")

