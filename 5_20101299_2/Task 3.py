import sys

sys.stdin = open("input3.txt", "r")
sys.stdout = open("output3.txt", "w")


def insertion_sort(a, b):
    for i in range(1, len(a)):
        while a[i - 1] > a[i] and i > 0:
            temp1 = a[i - 1]
            a[i - 1] = a[i]
            a[i] = temp1
            temp = b[i - 1]
            b[i - 1] = b[i]
            b[i] = temp
            i -= 1
    return b


file1 = open("input3.txt", "r")

n = file1.readline()

a = file1.readline().split()
a = list(map(int, a))
b = file1.readline().split()
b = list(map(int, b))


insertion_sort(b, a)

a = a[::-1]

for i in a:
    print(i, end=" ")

