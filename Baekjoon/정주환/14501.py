import sys
input = sys.stdin.readline

n = int(input().rstrip())

t=[]
m=[]

dp = [0]*(n+1)

for i in range(n):
    time, money = map(int,input().rstrip().split())
    t.append(time)
    m.append(money)

for i in range(n-1,-1,-1):
    if i+t[i]>n:
        dp[i]=dp[i+1]
    else:
        dp[i]=max(dp[i+1],m[i]+dp[i+t[i]])

print(max(dp))