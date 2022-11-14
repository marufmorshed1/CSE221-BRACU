import sys

sys.stdin = open("input.txt", "r")

evenC = 0
oddC = 0
noC = 0
palinC = 0
nonpalnC = 0


def ifPalidrome(a):
    if a is None:
        return False
    n = len(a)
    for i in range(n//2):
        if a[i] != a[n-1-i]:
            return False

    return True


def parity(n):
    checker = ""
    n = float(n)
    if n - int(n) == 0:
        if int(n) % 2 == 0:
            checker = "Even"
        elif int(n) % 2 != 0:
            checker = "Odd"
    else:
        checker = "None"

    return checker


file1 = open("input.txt", "r")
file2 = open("output.txt", "w")
file3 = open("record.txt", "w")
list = file1.read().split("\n")


for i in list:
    inner = i.split(" ")
    r1 = parity(inner[0])
    r2 = ifPalidrome(inner[1])
    if r1 == "Even" and r2 is True:
        j = inner[0] + " has even parity and " + inner[1] + " is a palindrome\n"
        evenC += 1
        palinC += 1
        file2.write(j)
    elif r1 == "Odd" and r2 is True:
        j = inner[0] + " has odd parity and " + inner[1] + " is a palindrome\n"
        oddC += 1
        palinC += 1
        file2.write(j)
    elif r1 == "None" and r2 is True:
        j = inner[0] + " cannot have parity and " + inner[1] + " is a palindrome\n"
        noC += 1
        palinC += 1
        file2.write(j)
    elif r1 == "Even" and r2 is False:
        j = inner[0] + " has even parity and " + inner[1] + " is not a palindrome\n"
        evenC += 1
        nonpalnC += 1
        file2.write(j)
    elif r1 == "Odd" and r2 is False:
        j = inner[0] + " has odd parity and " + inner[1] + " is not a palindrome\n"
        oddC += 1
        nonpalnC += 1
        file2.write(j)
    elif r1 == "None" and r2 is False:
        j = inner[0] + " cannot have parity and " + inner[1] + " is not a palindrome\n"
        noC += 1
        nonpalnC += 1
        file2.write(j)


totalNum = evenC + oddC + noC
evenC = (evenC * 100) / totalNum
oddC = (oddC * 100) / totalNum
noC = (noC * 100) / totalNum

totalPalin = palinC + nonpalnC
palinC = (palinC * 100) / totalPalin
nonpalnC = (nonpalnC * 100) / totalPalin

line1 = "Percentage of odd parity: " + str(oddC) + "%\n"
line2 = 'Percentage of even parity: ' + str(evenC) + "%\n"
line3 = "Percentage of no parity: " + str(noC) + "%\n"
line4 = "Percentage of palindrome: " + str(palinC) + "%\n"
line5 = "Percentage of non-palindrome: " + str(nonpalnC) + "%\n"

file3.write(line1)
file3.write(line2)
file3.write(line3)
file3.write(line4)
file3.write(line5)