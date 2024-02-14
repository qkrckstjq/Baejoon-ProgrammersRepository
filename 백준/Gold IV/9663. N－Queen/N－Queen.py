n = int(input())
row_check = [False] * n
left = [False] * (2*n-1)
right = [False] * (2*n-1)
cnt = 0


def queen(qn):
    global n, cnt
    if qn == n:
        cnt += 1
        return
    else:
        for j in range(n):
            if not row_check[j] and not left[j + qn] and not right[n-1 + qn - j]:
                row_check[j] = left[j + qn] = right[n-1 + qn - j] = True
                queen(qn + 1)
                row_check[j] = left[j + qn] = right[n-1 + qn - j] = False


queen(0)
print(cnt)