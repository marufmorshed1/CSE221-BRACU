import sys

sys.stdin = open("task1_input.txt", "r")
sys.stdout = open("task1_output.txt", "w")

file = open("task1_input.txt", "r")


def LCS(X, Y):
    m = len(X)
    n = len(Y)
    arr = [[0 for x in range(n + 1)] for x in range(m + 1)]

    i = 0
    while i <= m:
        for j in range(n + 1):
            if i == 0 or j == 0:
                arr[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                arr[i][j] = arr[i - 1][j - 1] + 1
            else:
                arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
        i += 1

    pattern = ""

    q = m
    w = n
    while q > 0 and w > 0:

        if X[q - 1] == Y[w - 1]:
            pattern = pattern + X[q - 1]
            q -= 1
            w -= 1

        elif arr[q - 1][w] > arr[q][w - 1]:
            q -= 1
        else:
            w -= 1

    return pattern[::-1]


# Driver program

code = {"Y": "Yasnaya", "P": "Pochinki", "S": "School", "R": "Rozhok", "F": "Farm", "M": "Mylta", "H": "Shelter",
        "I": "Prison"}

n = int(file.readline())

X = file.readline()
Y = file.readline()

ans = LCS(X, Y)


main = ''

for i in ans:
    main = main + code[i] + " "

# print(ans)

print(main)
print("Correctness of prediction: " + str(int(len(ans)*100/n)) + "%")