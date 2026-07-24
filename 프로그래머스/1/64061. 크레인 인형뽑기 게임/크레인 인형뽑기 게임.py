# class link:
#     def __init__(self, value):
#         self.down = None
#         self.up = None
#         self.value = value
        
        
#     def setDown(self, down):
#         self.down = down
    
#     def setUp(self, up):
#         self.up = up
    
#     def remove(self):
#         down = self.down
#         if self.value == down.value:
            
    

def solution(board, moves):
    answer = 0
    bucket = []
    real_board = [[] for _ in range(len(board[0]))]
    
    for i in range(len(board[0])):
        for j in range(len(board) - 1, -1, -1):
            if board[j][i] != 0:
                real_board[i].append(board[j][i])
    
    # print(real_board)
    
    for target in moves:        
        col = real_board[target - 1]
        if len(col) != 0:
            if len(bucket) == 0 or bucket[-1] != col[-1]:
                bucket.append(col[-1])
            elif bucket[-1] == col[-1]:
                bucket.pop()
                answer += 2
            col.pop()
        # print(real_board)
        # print(bucket)

    return answer