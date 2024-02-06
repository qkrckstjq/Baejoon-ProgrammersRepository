base_len = int(input())
base_dict = set(input().split(" "))
comp_len = int(input())
comp_str = input().split(" ")


result = ""
for s in comp_str:
    if s in base_dict:
        print('1')
    if not s in base_dict:
        print('0')

# print(result)