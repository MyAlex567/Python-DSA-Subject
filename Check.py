text1 = "aabbcc"


A = ""

for i in range(len(text1)):
    notFound = True

    for a in range(len(A)):
        if text1[i] == A[a]:
            notFound = False
            break
    if notFound:
        A = A + text1[i]

print(A)