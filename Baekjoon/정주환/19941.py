import sys
from collections import defaultdict
input = sys.stdin.readline

n,k = map(int,input().strip().split())

string = input()

p_index = []
h_index = []

for i in range(n):
    if string[i] == "H":
        h_index.append(i)
    else:
        p_index.append(i)
        
cnt=0
index=0
cnt_h=len(h_index)
for p in p_index:
    while index<cnt_h:
        h=h_index[index]
        if abs(p-h)<=k:
            cnt+=1
            index+=1
            break
        elif p<h:
            break
        else:
            index+=1
        
        
print(cnt)