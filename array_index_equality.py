import array as Array
arr=Array.array('i',[-8,0,2,5])
for i in range(0, len(arr)-1):
    if arr[i]==i:
        print(i)
