N = int(input())
input_list = list(map(int, input().split()))
input_list.sort()  # 투 포인터를 사용하기 위해 정렬

result = 0

for k in range(N):
    target = input_list[k]
    left, right = 0, N - 1

    while left < right:
        if left == k:  # target과 같은 인덱스를 건너뜀
            left += 1
            continue
        if right == k:  # target과 같은 인덱스를 건너뜀
            right -= 1
            continue

        two_sum = input_list[left] + input_list[right]

        if two_sum == target:
            result += 1
            break  # 하나만 찾으면 되므로 종료
        elif two_sum < target:
            left += 1
        else:
            right -= 1

print(result)
