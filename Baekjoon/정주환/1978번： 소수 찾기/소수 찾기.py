import sys
input = sys.stdin.readline


def solution(n):
    cnt = 0
    for num in n:
        # 1은 소수가 아님
        if num == 1:
            continue
        # 2는 소수
        if num == 2:
            cnt += 1
            continue
        # 짝수는 2를 제외하고 모두 소수가 아님
        if num % 2 == 0:
            continue
            
        # 홀수만 확인 (3부터 num-1까지 2씩 증가)
        check = True
        for j in range(3, num, 2):
            if num % j == 0:
                check = False
                break
                
        if check:
            cnt += 1
    
    return cnt

n=int(input())
n_list = list(map(int, input().split()))
result=solution(n_list)
print(result)


        