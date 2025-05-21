import sys
from collections import Counter
input = sys.stdin.readline

dic = []
cnt=0

n = int(input())

for i in range(n):
    dic.append(input().rstrip())

target1 = Counter(dic[0])
size = len(dic[0])
dic = dic[1:]

for word in dic:
    target2=Counter(word)
    intersection1 = sum((target1-target2).values())
    intersection2 = sum((target2-target1).values())
    if intersection1<=1 and intersection2<=1:
        cnt+=1

print(cnt)