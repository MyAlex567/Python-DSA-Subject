num = int(input("Enter here: "))

divisible = [2,3,5]

if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
    print(num, "is divisible by", end= " ")
else:
    print("can not be divisible by the given number")

for i in range(len(divisible)):
    if i == len(divisible)-1:
        print("and", end= " ")

    if num % divisible[i] == 0:
        print(divisible[i], end= " ")