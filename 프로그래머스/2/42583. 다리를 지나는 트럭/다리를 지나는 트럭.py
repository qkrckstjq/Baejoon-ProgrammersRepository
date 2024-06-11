from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque()
    total_weight = 0
    truck_weights = deque(truck_weights)
    
    while truck_weights:
        answer += 1
        
        if len(bridge) == bridge_length:
            total_weight -= bridge.popleft()
            
        if total_weight + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            bridge.append(truck)
            total_weight += truck
        else:
            bridge.append(0)
    
    return answer + bridge_length
