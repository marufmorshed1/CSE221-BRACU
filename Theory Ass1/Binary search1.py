def binSearch(a, n, key):
    l = 0
    r = n
    mid = 0
    while l < r:
        mid = (r + l) // 2
        if a[mid] == key:
             while mid + 1 < n and a[mid+1] == key:
                 mid += 1
             break
        elif a[mid] > key:
            r = mid
        else:
            l = mid + 1
    while mid > -1 and a[mid] > key:
        mid -= 1
    return mid + 1


a, b = input().split() #input
arr1 = input().split()
arr2 = input().split()
finalArray = []
a = int(a) #intConversion
b = int(b)
i = 0
j = 0
while i < a:
    temp = int(arr1[i])
    arr1[i] = temp
    i += 1
while j < b:
    temp = int(arr2[j])
    arr2[j] = temp
    j += 1
for i in arr2:
    x = binSearch(arr1, b, i)
    finalArray.append(x)

print(finalArray)