import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
for i in range(t):
    score_dict=defaultdict(list)
    n=int(input())
    score_list = list(map(int,input().split()))
    checker=set(score_list)
    for i in checker:
        if score_list.count(i)!=6:
            score_list=list(filter(lambda x:x!=i,score_list))

    for i in range(len(score_list)):
        score_dict[score_list[i]].append(i)
    
    for score in score_dict:
        tmp=score_dict.get(score)
        score_dict[score]=[sum(tmp[:4]),tmp[4]]
    sorted_result = sorted(score_dict.items(), key = lambda x: (x[1][0], x[1][1]))
    print(sorted_result[0][0])