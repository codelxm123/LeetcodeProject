class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            bo=[False for _ in range(10)]
            for j in range(9):
                if not board[i][j]==".":
                    num=int(board[i][j])
                    if bo[num]:
                        return False
                    bo[num]=True
        for j in range(9):
            bo=[False for _ in range(10)]
            for i in range(9):
                if not board[i][j]==".":
                    num=int(board[i][j])
                    if bo[num]:
                        return False
                    bo[num]=True
        for k1 in range(3):
            for k2 in range(3):
                bo=[False for _ in range(10)]
                for i in range(3):
                    for j in range(3):
                        x=k1*3+i
                        y=k2*3+j
                        if not board[x][y]==".":
                            num=int(board[x][y])
                            if bo[num]:
                                return False
                            bo[num]=True
        return True
