array = [1,2,3,4,5,6,7,8,9,10]

length = len(array)

for i in range(length-1):
    high = i
    for a in range(i+1, length):
        if array[a] > array[high]:
            high = a
    array[i], array[high] = array[high], array[i]

for x in array:
    print(x)