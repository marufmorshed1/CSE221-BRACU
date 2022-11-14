import sys

sys.stdin = open("input4.txt", "r")
sys.stdout = open("output4.txt", "w")
file1 = open("input4.txt", "r")


def merge(arr, left, mid, right):
    m = mid - left + 1
    n = right - mid
    L = [None] * (m)
    R = [None] * (n)
    for i in range(0, m):
        L[i] = arr[left + i]

    for j in range(0, n):
        R[j] = arr[mid + 1 + j]
    i = 0
    j = 0
    k = left

    while i < m and j < n:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < m:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_Sort(arr, left, right):
    if left < right:
        m = (left + (right - 1)) // 2
        merge_Sort(arr, left, m)
        merge_Sort(arr, m + 1, right)
        merge(arr, left, m, right)


n = file1.readline()
n = int(n)

arr = file1.readline().split()
arr = list(map(int, arr))

merge_Sort(arr, 0, n - 1)

for i in arr:
    print(i, end=" ")