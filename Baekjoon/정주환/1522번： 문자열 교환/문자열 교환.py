import sys
input = sys.stdin.readline

s = input().rstrip()
n = len(s)
a_count = s.count('a')
s = s + s
min_swaps = float('inf')
for i in range(n):
    window = s[i:i+a_count]
    b_count = window.count('b')
    min_swaps = min(min_swaps, b_count)

print(min_swaps)