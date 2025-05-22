import sys
input = sys.stdin.readline

string = input().rstrip()
count1 = string.count("1")//2
count0 = string.count("0")//2

string = string.replace("1","",count1)
string = string[::-1]
string = string.replace("0","",count0)
string = string[::-1]
print(string)
        


    
