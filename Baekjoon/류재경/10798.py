a = []
for i in range(5) : 
    b = []
    s = input()
    for j in s:
        b.append(j)
    a.append(b) 
    
max = 0
for i in a:
    if len(i) > max:
        max = len(i)
           
for i in range(max):
    for j in range(5):
        if i < len(a[j]):
           print(a[j][i], end="")
        
                
    
