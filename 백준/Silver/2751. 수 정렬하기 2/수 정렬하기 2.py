import sys

def s_input():
    return sys.stdin.readline().strip()

N = int(s_input())
result = [0] * N
for i in range(N):
    result[i] = int(s_input())

def merge_sort(arr, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)
    sorting(arr, start, mid, mid + 1, end)


def sorting(arr, i, i_end, j, j_end):
    start = i
    end = j_end
    sorted = []
    while i <= i_end and j <= j_end:
        if arr[i] < arr[j]:
            sorted.append(arr[i])
            i += 1
        elif arr[i] > arr[j]:
            sorted.append(arr[j])
            j += 1
        else:
            sorted.append(arr[i])
            sorted.append(arr[j])
            i += 1
            j += 1

    while i <= i_end:
        sorted.append(arr[i])
        i += 1

    while j <= j_end:
        sorted.append(arr[j])
        j += 1
    sorted_idx = 0
    for idx in range(start, end + 1):
        arr[idx] = sorted[sorted_idx]
        sorted_idx += 1



# test = [4, 7, 5, 31, 8, 2,1,1245,25634,6423,643,36475357,434,2,423,243,2,6,246,426,47623,47]
# merge_sort(test, 0, len(test) - 1)
merge_sort(result, 0, len(result) - 1)
for v in result:
    print(v)
