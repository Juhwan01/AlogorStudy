import sys
input = sys.stdin.readline

board = []
command_list = []
for i in range(5):
    board.append(list(map(int,input().rstrip().split())))

for i in range(5):
    command = list(map(int,input().rstrip().split()))
    command_list.extend(command)
    
for k in range(len(command_list)):
    line=0
    for i in range(5):
        for j in range(5):
            if board[i][j] == command_list[k]:
                board[i][j] = 0
    for i in range(5):
        if sum(board[i])==0:
            line+=1
            
    for i in range(5):
        sum_board=0
        for j in range(5):
            sum_board+=board[j][i]
        if sum_board == 0:
            line+=1
    
    if sum(1 for i in range(5) if board[i][i]==0)==5:
        line+=1
    if sum(1 for i in range(5) if board[i][4-i]==0)==5:
        line+=1   
    
    if line>=3:
        print(k+1)
        break
    
    
    