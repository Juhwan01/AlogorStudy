import sys
input = sys.stdin.readline

n, score, p = map(int,input().split())
cnt=1
isvalid=False

if n==0:
    print(1)
else:
    score_list=list(map(int,input().split()))
    for i in range(n):
        if score_list[i]<score:
            score_list.insert(i,score)
            isvalid=True
            break
        elif score_list[i]>score:
            cnt+=1
            
    if not isvalid and n<p:
        score_list.append(score)
        print(cnt)
    elif not isvalid:
        print(-1)
    else:
        print(cnt)
