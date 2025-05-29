import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]

sum = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        sum[i][j] = (a[i-1][j-1] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1])
K = int(input())

for _ in range(K):
    i, j, x, y = map(int, input().split())
    total = (sum[x][y] - sum[i-1][y] - sum[x][j-1] + sum[i-1][j-1])
    print(total)
