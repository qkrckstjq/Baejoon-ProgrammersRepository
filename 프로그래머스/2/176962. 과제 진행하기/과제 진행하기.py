def trans_time(time):
    hour, minute = time.split(":")
    return int(hour)*60 + int(minute)

def solution(plans):
    plans.sort(key = lambda x : trans_time(x[1]))
    # print(plans)
    stack = []
    answer = []
    for i in range(len(plans) - 1):
        plan = plans[i]
        sub = plan[0]
        start_time = trans_time(plan[1])
        delay = int(plan[2])
        
        next_plan = plans[i + 1]
        next_sub = next_plan[0]
        next_start_time = trans_time(next_plan[1])
        next_delay = int(next_plan[2])
        
        rest_time = next_start_time - (start_time + delay)
        # print(rest_time)
        if rest_time >= 0:
            answer.append(sub)
            # print(stack)
            while stack and rest_time > 0:
                last_plan_sub, last_plan_time = stack[-1][0], stack[-1][1]
                if rest_time >= last_plan_time:
                    stack.pop()
                    answer.append(last_plan_sub)
                    rest_time -= last_plan_time
                else:
                    stack[-1][1] -= rest_time
                    rest_time = 0
        else:
            stack.append([sub, -rest_time])
            
        if i == (len(plans) - 2):
            answer.append(plans[i + 1][0])
    while stack:
        answer.append(stack.pop()[0])
        
    # print(answer)
    # print(stack)
        
    
    # while stack:
    #     answer.append(stack.pop()[1])
    
    
    return answer