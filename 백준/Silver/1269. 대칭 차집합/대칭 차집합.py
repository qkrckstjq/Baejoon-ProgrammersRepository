A, B = map(int, input().split(" "))
A_list = set(list(map(int, input().split(" "))))
B_list = set(list(map(int, input().split(" "))))
A_len = len(A_list)
B_len = len(B_list)
# print(A_list, B_list, A_len, B_len)
for num in A_list:
    if num in B_list:
        A_len -= 1
        
for num in B_list:
    if num in A_list:
        B_len -= 1

print(A_len + B_len)