import sys
input = sys.stdin.readline

h, w, n, m = map(int, input().split())

height=(h+n)//(n+1)
width=(w+m)//(m+1)
print(height*width)