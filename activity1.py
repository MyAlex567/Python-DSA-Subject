num = int(input("Enter here: "))

if num >= 90 and num <= 100:
    print("Your Grade is A")
elif num >= 80 and num <= 89:
    print("Your Grade is B")
elif num >= 70 and num < 79:
    print("Your Grade is C")
elif num >= 65 and num <= 69:
    print("Your Grade is D")
elif num > 100:
    print("Error")
else:
    print("Failed")

