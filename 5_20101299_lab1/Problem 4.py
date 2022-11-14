import sys


sys.stdin = open("input4.txt", "r")
#sys.stdout = open("output4.txt", "w")


file1 = open("input4.txt", "r")

global n
n = file1.readline()
n = int(n)


A = []
for i in range(n):
    A.append([0] * n)
print(A)
B = []
for i in range(n):
    B.append([0] * n)
print(B)


for i in range(int(n)):
    line = file1.readline()
    print(line)
    list2 = line.split()
    print(list2)
    for l in range(int(n)):
        temp = int(list2[l])
        list2[l] = temp
    print(list2)
    A[i] = list2

file1.readline()

for i in range(int(n)):
    line = file1.readline()
    print(line)
    list6 = line.split()
    for k in range(int(n)):
        temp = int(list6[k])
        list6[k] = temp

    B[i] = list6


def Multiply_matrix(A, B):
    global n
    C = []
    for i in range(n):
        C.append([0] * n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += int(A[i][k]) * int(B[k][j])

    return C


C = Multiply_matrix(A, B)
for i in C:
    j = 0
    while j < 3:
        print(i[j], end=" ")
        j += 1
    print()
