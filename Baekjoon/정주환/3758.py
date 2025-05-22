import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n,k,t,m = map(int,input().rstrip().split())
    score_dict = defaultdict(dict)
    info_dict = defaultdict(dict)
    submit_cnt = [0]*(n+1)
    for index in range(m):
        i,j,s = map(int,input().rstrip().split())
        submit_cnt[i]+=1
        if j not in score_dict[i] or score_dict[i][j] < s:
            score_dict[i][j] = s
        info_dict[i]["index"] = index
        
    for i in range(1,n+1):
        info_dict[i]["cnt"] = submit_cnt[i]
    
    for i in range(1,n+1):
        sum=0
        for score in score_dict[i].values():
            sum+=score
        info_dict[i]["total"] = sum
        
    sorted_dict = sorted(
            info_dict.items(),
            key=lambda x: (-x[1]["total"], x[1]["cnt"], x[1]["index"])
        )
    grade=1
    for team in sorted_dict:
        if team[0]==t:
            print(grade)
            break
        else:
            grade+=1
    

