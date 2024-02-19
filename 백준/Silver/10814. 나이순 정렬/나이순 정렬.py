import sys

def s_input():
    return sys.stdin.readline().strip()

def merge_sort(arr, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)
    sorting(arr, start, mid, mid + 1, end)

def sorting(arr, i, i_end, j, j_end):
    sorted = []
    start = i
    end = j_end
    while i <= i_end and j <= j_end:
        if arr[i][0] <= arr[j][0]:
            sorted.append(arr[i])
            i += 1
        elif arr[i][0] > arr[j][0]:
            sorted.append(arr[j])
            j += 1

    while i <= i_end:
        sorted.append(arr[i])
        i += 1

    while j <= j_end:
        sorted.append(arr[j])
        j += 1

    sorted_idx = 0
    for i in range(start, end + 1, 1):
        arr[i] = sorted[sorted_idx]
        sorted_idx += 1

N = int(s_input())
result = [0] * N
for i in range(N):
    age, name = list(s_input().split(" "))
    result[i] = (int(age), name)

merge_sort(result, 0, len(result) - 1)

for age, name in result:
    print(age, name)