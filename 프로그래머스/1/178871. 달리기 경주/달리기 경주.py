def solution(players, callings):
    def swap(arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    
    rank_by_players = {}
    players_by_rank = {player : 0 for player in players}
    for i in range(len(players)):
        rank_by_players[i + 1] = players[i]
        players_by_rank[players[i]] = i + 1
    
    # print(rank_by_players)
    # print(players_by_rank)
    for name in callings:
        cur_rank = players_by_rank[name]
        prev_rank = cur_rank - 1
        prev_name = rank_by_players[prev_rank]
        swap(rank_by_players, cur_rank, prev_rank)
        swap(players_by_rank, name, prev_name)
    
    answer = [rank_by_players[i] for i in range(1, len(players) + 1)]
    return answer