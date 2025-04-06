arr = input()
size = arr.count('a')  # 'a'의 개수만큼의 윈도우 크기
n = len(arr)

# 첫 번째 윈도우에서 'b' 개수 계산
current_b = sum(1 for i in range(size) if arr[i] == 'b')
min_b = current_b  # 최소 'b' 개수 기록

# 슬라이딩 윈도우 이동
for i in range(1, n):
    # 왼쪽 끝 문자 제거
    if arr[i - 1] == 'b':
        current_b -= 1
    # 오른쪽 끝 문자 추가 (원형 구조)
    if arr[(i + size - 1) % n] == 'b':
        current_b += 1
    # 최소값 갱신
    min_b = min(min_b, current_b)

print(min_b)
