# 삽입정렬

array = [7,5,9,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in reversed(range(i)):
        if array[i]>array[j]:
            insert = array[i]
            array[j+2:i+1] = array[j+1:i]
            array[j+1] = insert
            break
        elif j==0:
            insert = array[i]
            array[1:i+1] = array[0:i]
            array[0] = insert

print(list(reversed(range(3))))
print(array)