import sys
input = sys.stdin.readline

N,M = map(int,input().rstrip().split())
mark_list=[]
for _ in range(N):
    mark,require = input().rstrip().split()
    require = int(require)
    mark_list.append([mark,require])
sorted_list = sorted(mark_list,key = lambda x:x[1])
for _ in range(M):
    target = int(input())
    left,right = 0,N-1
    answer=""
    while left<=right:
        mid = (left+right)//2
        if target<=mark_list[mid][1]:
            right = mid-1
            answer = mark_list[mid][0]
        else:
            left = mid+1
    print(answer)