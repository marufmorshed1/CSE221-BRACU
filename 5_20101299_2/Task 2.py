import sys


sys.stdin = open("input2.txt", "r")
sys.stdout = open("output2.txt", "w")


def selection_sort(a):
    for i in range(len(a) - 1, -1, -1):
        maxidx = i
        for j in range(i):
            if a[j] > a[maxidx]:
                maxidx = j
        temp = a[maxidx]
        a[maxidx] = a[i]
        a[i] = temp
    return a


file1 = open("input2.txt", "r")

a = file1.readline()
n = int(a[2])

arr = file1.readline()
arr = arr.split()
arr = list(map(int, arr))
selection_sort(arr)

arr = arr[:n]

for i in arr:
    print(i, end=" ")