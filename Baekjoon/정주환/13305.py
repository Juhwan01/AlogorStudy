import sys
input = sys.stdin.readline

n=int(input())
fee=0
all_bridge=0

bridge=list(map(int,input().split()))

fuel=list(map(int,input().split()))[:n-1]
low_fee=max(fuel)

for i in range(len(bridge)):
    if fuel[i]<low_fee:
        fee+=all_bridge*low_fee
        low_fee=fuel[i]
        all_bridge=bridge[i]
    else:
        all_bridge+=bridge[i]

fee+=all_bridge*low_fee
print(fee)
