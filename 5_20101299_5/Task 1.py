import sys

sys.stdin = open("task1_input.txt", "r")
# sys.stdout = open("task1_output.txt", "w")

file = open("task1_input.txt", "r")


def schedule_interval(arr, a):
    for i in range(0, a):
        for j in range(0, a - i - 1):
            if arr[j][1] > arr[j + 1][1]:
                tempo = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tempo
    print(arr)

    Selected = []
    Selected.append(arr[0])
    # print(Selected)
    f = Selected[0][1]
    # print(f)
    for i in arr:
        if i[0] >= f:
            Selected.append(i)
            f = i[1]

    return Selected


n = file.readline()

arr = []

for i in range(int(n)):
    text = file.readline().split()
    count = 0
    while count <= 1:
        text[count] = int(text[count])
        count += 1
    arr.append(text)


ans = schedule_interval(arr, int(n))
print(len(ans))
for i in ans:
    print(i[0], i[1])
