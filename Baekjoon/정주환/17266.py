import sys
input = sys.stdin.readline

index_list=[]
n = int(input())
m = int(input())

x = list(map(int,input().split()))

index_list.append(0)
index_list.append(x)
index_list.append(m)

print(index_list)