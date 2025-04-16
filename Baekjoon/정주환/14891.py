import sys
input = sys.stdin.readline

cogwheel_list = []

cogwheel_list.append(input().rstrip())
cogwheel_list.append(input().rstrip())
cogwheel_list.append(input().rstrip())
cogwheel_list.append(input().rstrip())

t = int(input())

for _ in range(t):
    num, direct = map(int, input().rstrip().split())
    num = num - 1  # 0-인덱스로 변환
    
    # 회전 방향 결정
    rotate_direction = [0] * len(cogwheel_list)
    rotate_direction[num] = direct
    
    # 오른쪽 톱니바퀴들의 회전 방향 결정
    for i in range(num, len(cogwheel_list)-1):
        if cogwheel_list[i][2] != cogwheel_list[i+1][6]:
            rotate_direction[i+1] = -rotate_direction[i]
        else:
            break
    
    # 왼쪽 톱니바퀴들의 회전 방향 결정
    for i in range(num, 0, -1):
        if cogwheel_list[i][6] != cogwheel_list[i-1][2]:
            rotate_direction[i-1] = -rotate_direction[i]
        else:
            break
    
    # 회전 수행
    for i in range(len(cogwheel_list)):
        if rotate_direction[i] == 1:  # 시계 방향
            cogwheel_list[i] = cogwheel_list[i][-1] + cogwheel_list[i][:-1]
        elif rotate_direction[i] == -1:  # 반시계 방향
            cogwheel_list[i] = cogwheel_list[i][1:] + cogwheel_list[i][0]

sum_wheel = 0
for i in range(len(cogwheel_list)):
    sum_wheel += int(cogwheel_list[i][0]) * (2**i)

print(sum_wheel)