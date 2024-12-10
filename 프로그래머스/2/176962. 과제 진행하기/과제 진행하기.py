def solution(plans):
    def trans_time(time):
        hour, minute = time.split(":")
        return int(hour) * 60 + int(minute)

    # 플랜을 시작 시간 기준으로 정렬
    plans.sort(key=lambda x: trans_time(x[1]))

    stack = []
    answer = []

    for i in range(len(plans) - 1):
        current_plan = plans[i]
        next_plan = plans[i + 1]

        current_subject, current_start, current_duration = current_plan
        next_subject, next_start, _ = next_plan

        current_start_time = trans_time(current_start)
        next_start_time = trans_time(next_start)
        duration = int(current_duration)

        rest_time = next_start_time - (current_start_time + duration)

        if rest_time >= 0:
            # 현재 작업 완료 후 다음 작업 시작
            answer.append(current_subject)
            # 스택에 쌓여 있는 작업 처리
            while stack and rest_time > 0:
                last_subject, remaining_time = stack.pop()
                if rest_time >= remaining_time:
                    answer.append(last_subject)
                    rest_time -= remaining_time
                else:
                    stack.append((last_subject, remaining_time - rest_time))
                    rest_time = 0
        else:
            # 다음 작업 시작 전 현재 작업 미완료
            stack.append((current_subject, -rest_time))

    # 마지막 작업 추가
    answer.append(plans[-1][0])

    # 스택에 남아 있는 작업 추가
    while stack:
        answer.append(stack.pop()[0])

    return answer
