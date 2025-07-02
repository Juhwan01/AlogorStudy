N = int(input())
day = list(map(int, input().split()))

def junhyun(N, day):
   stocks = 0  
   cash = N        
   for price in day:
       if cash >= price:
           cnt = cash // price           
           stocks += cnt
           cash -= cnt * price        
   total = cash + stocks * day[-1]
   return total

def seongmin(N, day):
   stocks = 0
   cash = N
   
   for i in range(3, len(day)):
       if day[i-2] > day[i-3] and day[i-1] > day[i-2] and day[i] > day[i-1]:
           cash += stocks * day[i]  
           stocks = 0
       elif day[i-2] < day[i-3] and day[i-1] < day[i-2] and day[i] < day[i-1]:
           cnt = cash // day[i]  
           stocks += cnt
           cash -= cnt * day[i]
   
   total = cash + stocks * day[-1]
   return total

j = junhyun(N, day)
s = seongmin(N, day)

if j > s:
   print("BNP")
elif s > j:
   print("TIMING")
else:
   print("SAMESAME")