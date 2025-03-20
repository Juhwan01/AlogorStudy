import sys
input = sys.stdin.readline

result = {}
max_key = None

n_list = list(input().strip())
check_du =False

for n in n_list:
    tmp=n.upper()
    if result.get(tmp):
        result[tmp] += 1
    else:
        result[tmp] = 1

max_value = max(result.values())

for key, value in result.items():
    if value == max_value:
        if max_key:
            print("?")
            check_du = True
            break
        max_key = key
        
if not check_du:
    print(max_key)
        
