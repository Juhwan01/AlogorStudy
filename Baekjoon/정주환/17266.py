import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

x = list(map(int,input().split()))

max_val=max(x[0],n-x[-1])

for i in range(1,len(x)):
    light=(x[i]-x[i-1]+1)//2
    max_val = max(max_val,light)
print(max_val)
