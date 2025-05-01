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
    num = num - 1
    
    rotate = [0]*len(cogwheel_list)
    rotate[num] = direct
    
    for i in range(num,len(cogwheel_list)-1):
        if cogwheel_list[i][2] != cogwheel_list[i+1][6]:
            rotate[i+1] = -rotate[i]
        else:
            break
        
    for i in range(num,0,-1):
        if cogwheel_list[i][6] != cogwheel_list[i-1][2]:
            rotate[i-1] = -rotate[i]
        else:
            break
    
    for i in range(len(cogwheel_list)):
        if rotate[i] == 1:
            cogwheel_list[i] = cogwheel_list[i][-1] + cogwheel_list[i][:-1]
        elif rotate[i] == -1:
            cogwheel_list[i] = cogwheel_list[i][1:] + cogwheel_list[i][0]
            
sum_wheel = 0
for i in range(len(cogwheel_list)):
    sum_wheel += int(cogwheel_list[i][0]) * (2**i)

print(sum_wheel)