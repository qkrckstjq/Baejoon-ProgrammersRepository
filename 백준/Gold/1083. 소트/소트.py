N = int(input())
array = list(map(int, input().split()))
S = int(input())

for i in range(N):
    # 현재 위치에서 S번 이내로 이동할 수 있는 가장 큰 수를 찾음
    max_index = i
    for j in range(i + 1, min(N, i + S + 1)):
        if array[j] > array[max_index]:
            max_index = j

    # 이동할 수 있는 만큼 S에서 차감하고, 최대 값과 현재 위치 값을 스왑하여 앞으로 이동
    if max_index != i:
        S -= (max_index - i)
        # 최대 값과 현재 위치 사이의 값을 차례로 교환하여 이동
        for j in range(max_index, i, -1):
            array[j], array[j - 1] = array[j - 1], array[j]
    
    # 더 이상 교환할 수 없으면 종료
    if S <= 0:
        break

print(" ".join(map(str, array)))
