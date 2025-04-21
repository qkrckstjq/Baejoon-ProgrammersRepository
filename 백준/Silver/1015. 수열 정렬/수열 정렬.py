N = int(input())
A = list(map(int, input().split()))

indexed_A = list(enumerate(A))
indexed_A.sort(key=lambda x: (x[1], x[0]))

P = [0] * N
for b_index, (a_index, _) in enumerate(indexed_A):
    P[a_index] = b_index

print(' '.join(map(str, P)))
