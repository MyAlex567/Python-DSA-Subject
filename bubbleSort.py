array = [5,4,1,3,2]

length = len(array)

for i in range(length-1):
    temp = None
    for a in range(length-i-1):
        if array[a] > array[a+1]:
            temp = array[a+1]
            array[a+1] = array[a]
            array[a] = temp

for x in array:
    print(x)
