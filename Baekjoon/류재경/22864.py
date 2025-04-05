import sys
input = sys.stdin.readline

x = list(map(int, input().split()))
M = 0
B = 0
H = 0

while H < 24:
    if M + x[0] > x[3]:
        M -= x[2]
        if M < 0:
            M = 0
    else:
        B += x[1]
        M += x[0]
    if M > x[3]:
        break
    H += 1

print(B)