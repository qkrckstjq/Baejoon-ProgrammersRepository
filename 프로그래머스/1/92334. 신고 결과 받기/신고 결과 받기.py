def solution(id_list, report, k):
    answer = []
    post_report = {}
    get_report = {}
    
    for arr in report:
        user_report = arr.split(" ")
        user = user_report[0]
        reported = user_report[1]
        dup = False
        
        if user in post_report:
            if reported in post_report[user]:
                dup = True
            post_report[user].add(reported)
        else:
            post_report[user] = set([reported])
        
        if dup:
            continue
        if reported in get_report:
            get_report[reported] += 1
        else:
            get_report[reported] = 1
    
    for user in id_list:
        num = 0
        if not user in post_report:
            answer.append(0)
            continue
        report_list = post_report[user]
        for report in report_list:
            if get_report[report] >= k:
                num += 1
                
        answer.append(num)
            
    
    # print(post_report, get_report)
    
    return answer