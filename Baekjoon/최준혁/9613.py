def GDB(a, b):
    while(b>0):
        a, b = b, a%b
    return a
    

num = int(input())

while(num):
    num -= 1
    list_num = list(map(int, input().split()))
    count = 0
    for i in range(1, list_num[0]):
        for j in range(i+1, list_num[0]+1):
            count += GDB(list_num[i], list_num[j])
    print(count)