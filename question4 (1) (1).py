a = int(input("Enter three numbers: "))
b = int(input())
c = int(input())

if a > b and a > c:
    print("Largest:", a)
elif b > c:
    print("Largest:", b)
else:
    print("Largest:", c)