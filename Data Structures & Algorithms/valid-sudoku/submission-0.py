from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check the rows in the board
        for i in range(9):
            d={}
            for j in range(9):
                tmp = board[i][j]
                if tmp == ".":
                    continue
                else:
                    if tmp in d:
                        return False
                    d[tmp] = 1
        
        #check the columns in the board
        for i in range(9):
            d={}
            for j in range(9):
                tmp = board[j][i]
                if tmp == ".":
                    continue
                else:
                    if tmp in d:
                        return False
                    d[tmp] = 1

        #check 3*3 boxes
        for i in range(0,9,3):
            for j in range(0,9,3):
                seen = set()
                for dr in range(3):
                    for dc in range(3):
                        val = board[i + dr][j + dc]
                        if val == '.':
                            continue
                        if val in seen:
                            return False
                        seen.add(val)
        return True