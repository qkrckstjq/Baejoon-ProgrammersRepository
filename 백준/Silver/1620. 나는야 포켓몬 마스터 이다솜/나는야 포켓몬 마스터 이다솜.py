N, M = map(int, input().split(" "))

number_name = {}
name_number = {}

for i in range(1, N + 1):
    name = input()
    number_name[i] = name
    name_number[name] = i

for _ in range(M):
    input_value = input()
    try:
        input_value = int(input_value)
        print(number_name[input_value])
    except:
        print(name_number[input_value])
    