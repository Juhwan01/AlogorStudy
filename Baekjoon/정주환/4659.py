import sys
input = sys.stdin.readline

vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    string = input().rstrip()
    
    if string == "end":
        break
    
    flag = True
    
    if not any(v in string for v in vowels):
        flag = False
    
    if flag:
        for i in range(len(string) - 2):
            if all(string[i+j] in vowels for j in range(3)):
                flag = False
            elif all(string[i+j] not in vowels for j in range(3)):
                flag = False
    
    if flag:
        for i in range(len(string) - 1):
            if string[i] == string[i+1] and string[i] not in ['e', 'o']:
                flag = False
                break
    if flag:
        print("<{}> is acceptable.".format(string))
    else:
        print("<{}> is not acceptable.".format(string))