import sys

h, w, n, m = map(int, sys.stdin.readline().split()) 

x = (h + n) // (n + 1)
y = (w + m) // (m + 1)

print(x * y)
