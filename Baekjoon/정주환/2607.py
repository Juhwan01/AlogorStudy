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
    intersection = target2-target1
    result = sum(intersection.values())
    if result<=1:
        cnt+=1

print(cnt)