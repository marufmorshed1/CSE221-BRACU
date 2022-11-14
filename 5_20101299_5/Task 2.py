import sys

sys.stdin = open("task2_input.txt", "r")
# sys.stdout = open("task2_output.txt", "w")

file = open("task2_input.txt", "r")


def schedule_interval(arr, a, n):
    for i in range(0, a):
        for j in range(0, a - i - 1):
            if arr[j][1] > arr[j + 1][1]:
                tempo = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tempo

    Selected = []

    for k in range(n):
        Selected.append(arr[0])
        # print(Selected)
        f = Selected[0][1]
        # print(f)
        for i in arr:
            if i[0] >= f:
                Selected.append(i)
                arr.remove(i)
                f = i[1]

    return len(Selected)


n, p = file.readline().split()

arr = []

for i in range(int(n)):
    text = file.readline().split()
    count = 0
    while count <= 1:
        text[count] = int(text[count])
        count += 1
    arr.append(text)

ans = schedule_interval(arr, int(n), int(p))

print(ans)