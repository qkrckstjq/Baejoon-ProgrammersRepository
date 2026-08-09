from collections import deque

def solution(cacheSize, cities):
    answer = 0
    queue = deque()
    dup = {}
    
    for city in cities:
        city = city.upper()
        if city in dup:
            answer += 1
            idx = dup[city]
            queue.remove(city)
            # del queue[idx]
            # queue.removeIndex(idx)
            queue.append(city)
        else:
            answer += 5
            
            if len(dup) < cacheSize:
                queue.append(city)
                dup[city] = len(dup)
            else:
                if queue:
                    front = queue[0]
                    queue.popleft()
                    del dup[front]

                    queue.append(city)
                    dup[city] = len(dup)
        
    
    # print(cities)
    return answer