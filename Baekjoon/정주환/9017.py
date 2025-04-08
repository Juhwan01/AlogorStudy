import sys
from collections import defaultdict
input = sys.stdin.readline



t = int(input())
for i in range(t):
    score_dict=defaultdict(list)
    result_list=[]
    n=int(input())
    score_list = list(map(int,input().split()))
    check = set(score_list)
    for i in check:
        if score_list.count(i)==6:
            result_list.append(i)
    
    print(score_dict)
