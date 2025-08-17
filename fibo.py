a = 0
b = 1

print(a, end=" ")
print(b, end=" ")

for i in range(10):
    newNum = a + b
    print(newNum, end=" ")
    a = b
    b = newNum
