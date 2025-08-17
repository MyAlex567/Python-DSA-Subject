num = int(input("Enter here: "))

if num % 2 == 0 and num % 3 == 0 and num % 5 == 0:
    print(num, "is divisible by 2, 3, and 5")
elif num % 2 == 0 and num % 3 == 0:
    print(num, "is divisible by 2 and 3")
elif num % 2 == 0 and num % 5 == 0:
    print(num, "is divisible by 2 and 5")
elif num % 3 and num % 5 == 0:
    print(num, "is divisible by 3 and 5")
elif num % 2 == 0:
    print(num, "is divisible by 2")
elif num % 3 == 0:
    print(num, "is divisible by 3")
elif num % 3 == 0:
    print(num, "is divisible by 3")
else:
    print("can not be divisible by the given number")