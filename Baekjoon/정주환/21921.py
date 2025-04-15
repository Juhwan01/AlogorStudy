import sys
input = sys.stdin.readline

n, size = map(int, input().split())
visitor_list = list(map(int, input().split()))

window_sum = sum(visitor_list[:size])
max_sum = window_sum
cnt = 1

for i in range(size, n):
    window_sum = window_sum - visitor_list[i - size] + visitor_list[i]
    if window_sum > max_sum:
        max_sum = window_sum
        cnt = 1
    elif window_sum == max_sum:
        cnt += 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(cnt)
