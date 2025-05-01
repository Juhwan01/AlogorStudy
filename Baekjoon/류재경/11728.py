import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

X = A + B
X.sort()

print(*X)

# numbers = [1, 2, 3, 4, 5]
# print(*numbers)  # 1 2 3 4 5
# 위 코드는 print(1, 2, 3, 4, 5)와 동일한 효과