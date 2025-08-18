for i in range(1, 6):
    for a in range(1, 6-i):
        print(" ", end= " ")

    for j in range(1, i+1):
        print(" * ", end= " ")

    print()
print("-------------------------------")
for b in range(1,6):
    for i in range(1, b+1):
        print("*", end= " ")
    
    print()
print("-------------------------------")
for i in range(1, 6):
    for j in range(1, i):
        print(" ", end= " ")

    for a in range(1, 7-i):
        print(" * ", end= " ")

    print()
print("-------------------------------")   
for b in range(1,6):
    for j in range(1, 7-b):
        print("*", end= " ")

    print()    
print("-------------------------------")
for i in range(1, 6):
    for a in range(1, 6-i):
        print(" ", end=" ")
    for j in range(1, 1+i):
        print("*", end=" ")

    print()
print("-------------------------------")