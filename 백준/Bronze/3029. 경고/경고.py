time1 = input().split(":")
time2 = input().split(":")

def get_second(time):
    return int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])

def get_time(second):
    hour = str(round(second // 3600))
    last_min = second % 3600
    
    min = str(round(last_min // 60))
    last_second = last_min % 60
    
    second = str(last_second)
    
    return f"{hour if len(hour) > 1 else '0' + hour}:{min if len(min) > 1 else '0' + min}:{second if len(second) > 1 else '0' + second}"


day = 3600 * 24
time1_second = get_second(time1)
time2_second = get_second(time2)

if time1_second >= time2_second:
    print(get_time(day - time1_second + time2_second))
else:
    print(get_time(time2_second - time1_second))