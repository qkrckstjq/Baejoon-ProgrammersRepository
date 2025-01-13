import heapq

def solution(book_time):
    
    def proccess_time(time):
        splited_time = time.split(":")
        return int(splited_time[0])*60 + int(splited_time[1])
        
    
    book_time.sort(key = lambda x: proccess_time(x[0]))
    book_time = [[proccess_time(book[0]), proccess_time(book[1])] for book in book_time]
    end_time = [float('inf')]
    answer = 0
    
    for i in range(len(book_time)):
        min_end_time = end_time[0]
        if book_time[i][0] >= min_end_time + 10:
            heapq.heappop(end_time)
        else:
            answer += 1
        heapq.heappush(end_time, book_time[i][1])
    
    return answer