# C, N = list(map(int, input().split(" ")))
# max_people = 0
# pay_people = []
# for _ in range(N):
#     pay, people = list(map(int, input().split(" ")))
#     pay_people.append([pay, people])
#     max_people = max(max_people, people)
#     # if peoples[people] == 0:
#     #     peoples[people] = pay
#     # else:
#     #     people[people] = min(peoples[people], pay)

# peoples = []
# if max_people >= C:
#     peoples = [0] * (max_people + 1)
# elif C % max_people == 0:
#     peoples = [0] * (max_people * (C // max_people) + 1)
# else:
#     peoples = [0] * (max_people * (C // max_people + 1) + 1)

# result = []
# for pay, people in pay_people:
#     if peoples[people] == 0:
#         peoples[people] = pay
#     else:
#         peoples[people] = min(peoples[people], pay) 
#     for next_people in range(people, len(peoples), people):
#         if peoples[next_people] == 0:
#             peoples[next_people] += peoples[next_people - people] + pay
#         else:
#             peoples[next_people] = min(peoples[next_people], peoples[next_people - people] + pay)
#         if next_people >= C:
#             result.append(peoples[next_people]) 

# print(min(result))

# C, N = list(map(int, input().split(" ")))
# pay_people = []
# for _ in range(N):
#     pay, people = list(map(int, input().split(" ")))
#     pay_people.append([pay, people])


C, N = list(map(int, input().split(" ")))
pay_people = []
for _ in range(N):
    pay, people = list(map(int, input().split(" ")))
    pay_people.append([pay, people])

dp = [float('inf')] * (C + 101)
dp[0] = 0
for pay, people in pay_people:
    for i in range(people, len(dp)):
        dp[i] = min(dp[i], dp[i - people] + pay)

print(min(dp[C:]))
