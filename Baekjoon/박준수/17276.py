import sys
input = sys.stdin.readline

N = int(input())

angle_list = []
arr_list = []

for _ in range(N):
    size, angle = map(int, input().split())
    angle_list.append(angle)
    arr = []
    for i in range(size):
        col = list(map(int,input().split()))
        arr.append(col)
    arr_list.append(arr)

for i in range(len(arr_list)):
    arr = arr_list[i]
    size = len(arr)
    epoch = len(arr)//2
    steps = (angle_list[i] // 45) % 8
    for _ in range(steps):
        for j in range(epoch):
            temp1=arr[j][-(j+1)]
            arr[j][-(j+1)] = arr[j][size//2]
            arr[j][size//2] = arr[j][j]
                
            temp2=arr[-(j+1)][-(j+1)]
            arr[-(j+1)][-(j+1)] = arr[size//2][-(j+1)]
            arr[size//2][-(j+1)] = temp1
    
            temp1 = arr[-(j+1)][j]
            arr[-(j+1)][j] = arr[-(j+1)][size//2]
            arr[-(j+1)][size//2] = temp2
    
            arr[j][j] = arr[size//2][j]
            arr[size//2][j] = temp1

for arr in arr_list:
    for row in arr:
        print(" ".join(map(str,row)))