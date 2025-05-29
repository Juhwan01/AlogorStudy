import sys
input = sys.stdin.readline

N = int(input())

cow = [-1 for _ in range(11)]
cnt = 0
for _ in range(N):
    c, r = map(int, input().split())
    if cow[c] == -1:
        cow[c] = r
    elif cow[c] != r:
        cow[c] = r
        cnt += 1
print(cnt)