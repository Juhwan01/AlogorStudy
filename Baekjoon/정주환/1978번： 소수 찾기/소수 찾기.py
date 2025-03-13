import sys
input = sys.stdin.readline


def solution(n):
    cnt=0
    length = len(n)
    for i in range(length):
        target=n[i]
        if(target==2):
            cnt+=1
        else:
            for j in range(2, target):
                if target%j==0:
                    break
                if j==target-1:
                    cnt+=1    
    return cnt
n=int(input())
n_list = list(map(int, input().split()))
result=solution(n_list)
print(result)


        