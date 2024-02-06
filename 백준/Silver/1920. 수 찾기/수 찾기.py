base_len = int(input())
base_dict = set(input().split(" "))
comp_len = int(input())
comp_str = input().split(" ")


for s in comp_str:
    if s in base_dict:
        print('1')
    else:
        print('0')