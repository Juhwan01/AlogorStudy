import sys
input = sys.stdin.readline

N,M = map(int,input().strip().split())

memo = []
for _ in range(N):
    memo.append(input().rstrip())
    
g1 = set(memo)

for _ in range(M):
    keywords = input().rstrip().split(",")
    g1.difference_update(keywords)
    print(len(g1))