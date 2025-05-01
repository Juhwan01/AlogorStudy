n = int(input())
budget_list = list(map(int, input().split()))
total_budget = int(input())

start = 0
end = max(budget_list)
answer = 0

while start <= end:
    mid = (start + end) // 2
    allocated = sum(min(mid,b)for b in budget_list)
    if allocated<=total_budget:
        answer=mid
        start=mid+1
    else:
        end = mid-1
print(answer)