import sys

sys.stdin = open("task2_input.txt", "r")
sys.stdout = open("task2_output.txt", "w")

file = open("task2_input.txt", "r")


def LCS(X, Y, Z):
    m = len(X)
    n = len(Y)
    o = len(Z)

    arr = [[[0 for i in range(o + 1)] for j in range(n + 1)] for k in range(m + 1)]

    i = 0
    while i <= m:
        for j in range(n + 1):
            for k in range(o + 1):
                if i == 0 or j == 0 or k == 0:
                    arr[i][j][k] = 0

                elif X[i - 1] == Y[j - 1] and X[i - 1] == Z[k - 1]:
                    arr[i][j][k] = arr[i - 1][j - 1][k - 1] + 1

                else:
                    arr[i][j][k] = max(max(arr[i - 1][j][k], arr[i][j - 1][k]), arr[i][j][k - 1])
        i += 1

    return arr[m][n][o]


X = file.readline()
Y = file.readline()
Z = file.readline()


print(LCS(X, Y, Z))