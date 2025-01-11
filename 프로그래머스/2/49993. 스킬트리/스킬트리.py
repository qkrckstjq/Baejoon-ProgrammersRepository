def solution(skill, skill_trees):
    answer = 0
    set_skill = set(list(skill))
    
    for cur_skill in skill_trees:
        i = 0
        possible_word = skill[i]
        is_possible = True
        for c in cur_skill:
            if c not in set_skill:
                continue
            elif c == possible_word:
                i += 1
                if i < len(skill):
                    possible_word = skill[i]
                else:
                    break
            else:
                is_possible = False
                break
        if is_possible:
            answer += 1
           
    return answer