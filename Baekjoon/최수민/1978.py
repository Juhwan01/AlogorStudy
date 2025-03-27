N = int(input()) 

count = 0 

number = map(int, input().split())

for num in number:         
    if num > 1 :          
        for j in range(2, num):
            if num % j == 0:   
                break
        else:
            count += 1 

print(count)