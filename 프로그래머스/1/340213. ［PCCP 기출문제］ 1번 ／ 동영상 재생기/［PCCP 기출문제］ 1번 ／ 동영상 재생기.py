def solution(video_len, pos, op_start, op_end, commands):
    video_len = list(map(int, video_len.split(":"))) 
    pos = list(map(int, pos.split(":")))
    op_start = list(map(int, op_start.split(":"))) 
    op_end = list(map(int, op_end.split(":"))) 
    
    video_len = video_len[0]*60 + video_len[1]
    pos = pos[0]*60 + pos[1]
    op_start = op_start[0]*60 + op_start[1]
    op_end = op_end[0]*60 + op_end[1]
    
    # print(video_len, pos, op_start, op_end)
    if op_start <= pos <= op_end:
            pos = op_end
            
    for command in commands:
        
        
        if command == "next":
            if pos + 10 <= video_len:
                pos += 10
            else:
                pos = video_len
        elif command == "prev":
            if pos - 10 >= 0:
                pos -= 10
            else:
                pos = 0
        if op_start <= pos <= op_end:
            pos = op_end
            
    result = list(map(str, [pos // 60, pos % 60]))
    for i in range(len(result)):
        if len(result[i]) < 2:
            result[i] = f"0{result[i]}"    
    return ":".join(result)