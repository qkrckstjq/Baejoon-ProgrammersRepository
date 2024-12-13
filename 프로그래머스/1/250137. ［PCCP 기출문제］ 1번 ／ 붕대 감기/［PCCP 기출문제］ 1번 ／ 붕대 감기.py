def solution(bandage, health, attacks):
    max_health = health
    def add_health(health, num):
        return health + num if health + num <= max_health else max_health
    
    def healing(health, time_dif):
        raps = (time_diff - 1) // bandage[0]
        per_heal = (time_diff - 1) % bandage[0]
        health = add_health(health, (bandage[0] * bandage[1] + bandage[2]) * raps)
        health = add_health(health, per_heal * bandage[1])
        return health
                            
    for i in range(len(attacks) - 1):
        time = attacks[i][0]
        damage = attacks[i][1]
        
        next_time = attacks[i + 1][0]
        # next_damage = attacks[i + 1][1]
        
        time_diff = next_time - time
        health -= damage
        # print("뎀지 받음", health)
        if health < 1:
            break
        health = healing(health, time_diff)
        # print("힐 받음", health)
        
    health -= attacks[-1][1]
    if health < 1:
        return -1
    else:
        return health
