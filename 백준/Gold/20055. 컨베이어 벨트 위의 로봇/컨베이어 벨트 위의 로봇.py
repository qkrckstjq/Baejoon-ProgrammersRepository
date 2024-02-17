import sys

def s_input():
    return sys.stdin.readline().strip()
def split_belt(belt, flat_belt, N):
    upper_belt = []
    lower_belt = []
    belt_len = len(flat_belt) - 1
    for i in range(N):
        temp_upper = [flat_belt[i], False]
        upper_belt.append(temp_upper)

        temp_lower = [flat_belt[belt_len - i], False]
        lower_belt.append(temp_lower)
    belt.append(upper_belt)
    belt.append(lower_belt)

def rotate_belt(belt):
    temp_up_right = belt[0][-1]
    temp_down_left = belt[1][0]
    belt_len = len(belt[0]) - 1
    for i in range(belt_len):
        belt[1][i] = belt[1][i + 1]
        belt[0][belt_len - i] = belt[0][belt_len - i - 1]
    belt[0][0] = temp_down_left
    belt[1][-1] = temp_up_right
    belt[0][-1][1] = False
    belt[1][0][1] = False
def move_box_robot(belt, belt_state, target):
    for i in range(len(belt[0]) - 1, 0, -1):
        if belt[0][i - 1][1]:
            if not belt[0][i][1] and belt[0][i][0] > 0:
                belt[0][i][1] = True
                belt[0][i - 1][1] = False
                belt[0][i][0] -= 1
                if check_zero(belt[0][i][0], belt_state, target):
                    return True
        else:
            continue
    belt[0][-1][1] = False
    return False
def lift_box_robot(belt, belt_state, target):
    if belt[0][0][0] > 0:
        belt[0][0][1] = True
        belt[0][0][0] -= 1
        return check_zero(belt[0][0][0], belt_state, target)
    return False
def check_zero(remain, belt_state, target):
    if remain == 0:
        belt_state['zero'] += 1
        if belt_state['zero'] == target:
            return True
    return False
belt = []
N, K = list(map(int, s_input().split(" ")))
flat_belt = list(map(int, s_input().split(" ")))
split_belt(belt, flat_belt, N)
belt_state = {'zero': 0}
result = 0

while True:
    result += 1
    rotate_belt(belt)
    if move_box_robot(belt, belt_state, K):
        break
    if lift_box_robot(belt, belt_state, K):
        break

print(result)