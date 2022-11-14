import sys

sys.stdin = open("task3_input.txt", "r")
sys.stdout = open("task3_output.txt", "w")

file = open("task3_input.txt", "r")


def Work(arr, n, seq):
    arr.sort()
    jack = 0
    jill = 0
    wSeq = []
    str_seq = ''

    for i in seq:
        if i == "J":
            jack += arr[0]
            wSeq.append(arr[0])
            str_seq = str_seq + str(arr[0])
            arr.remove(arr[0])

        elif i == "j":
            m = max(wSeq)
            str_seq = str_seq + str(m)
            wSeq.remove(m)
            jill += int(m)

    print(str_seq)
    print("Jack will work for", jack, "hours")
    print("Jill will work for", jill, "hours")


n = file.readline()
text = file.readline().split()

count = 0
while count < len(text):
    text[count] = int(text[count])
    count += 1
seq = file.readline()


Work(text, int(n), seq)