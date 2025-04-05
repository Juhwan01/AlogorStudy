import sys
input = sys.stdin.readline

vowel = ['a','e','i','o','u']

while True:
    string = input().rstrip()
    flag = True
    if string == "end":
        break
    if not any(v in string for v in vowel):
        print("<{}> is not acceptable.".format(string))
    else:
        for i in range(len(string)):
            try:
                tmp1 = string[i:i+3]
                tmp2 = string[i:i+2]
                sum_vowel=sum(tmp1.count(v)for v in vowel)
                sum_alpha=sum(tmp2.count(t)for t in tmp2)
                if sum_vowel == 3 or sum_vowel == 0:
                    print("<{}> is not acceptable.".format(string))
                    flag=False
                    break
                elif sum_alpha == 2 and tmp2 != "ee" and tmp2 != "oo":
                    print("<{}> is not acceptable.".format(string))
                    flag=False
                    break
            except:
                continue
        if flag:
            print("<{}> is acceptable.".format(string))
            
        
        

    
    
    
        
