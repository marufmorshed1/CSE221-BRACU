import sys

sys.stdin = open('input1.txt', 'r')
sys.stdout = open("output1.txt", 'w')
file = open('input1.txt', 'r')


def bubblesort(a):
    i = 1
    while i < len(a):                                          # So, for the best case, we will be provided with a sorted loop. So, only the while
        if a[i] < a[i - 1]:                                    # loop will execute and run for n times. So the time complexity will be "θ(n)".
            a[i] = a[i] + a[i - 1]                             # (the inner comparison will be false everytime.)
            a[i - 1] = a[i] - a[i - 1]
            a[i] = a[i] - a[i - 1]
            i = 0
        i += 1

    return a


n = file.readline()
arr = file.readline().split()
arr = list(map(int, arr))

bubblesort(arr)

for j in arr:
    print(j, end=" ")
