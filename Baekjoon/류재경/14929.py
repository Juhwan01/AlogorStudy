import sys
input = sys.stdin.readline

def sum1(n, x):
    sum1 = 0
    for a in range(n):
        for b in range(a+1, n):
            sum1 += x[a] * x[b]
            
    return sum1

def sum2(n, x):
    all_sum = sum(x)
    sum2 = 0
    for i in range(n-1):
        all_sum -= x[i]
        sum2 += all_sum * x[i]
    
    return sum2
         
         
n = int(input())
x = list(map(int,input().split())) 


print(sum1(n, x))
print(sum2(n, x))


    
