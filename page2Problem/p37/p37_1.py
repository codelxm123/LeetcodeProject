class Solution(object):
    def __init__(self):
        self.bo1=[[]]
        self.bo2=[[]]
        self.bo3=[[]]
        self.ans=[["" for _ in range(9)] for _ in range(9)]

    def dfs(self,board,x,y):
        if (x==9):
            for i in range(9):
                for j in range(9):
                    self.ans[i][j]=board[i][j]
            return 1
        num_block=(x//3)*3+y//3
        next_x=x
        next_y=y
        if (y==8):
            next_x+=1
            next_y=0
        else:
            next_y+=1
        if board[x][y]==".":
            for num in range(9):
                if self.bo1[x][num] and self.bo2[y][num] and self.bo3[num_block][num]:
                    board[x][y]="%d"%(num+1)
                    self.bo1[x][num]=False
                    self.bo2[y][num]=False
                    self.bo3[num_block][num]=False
                    if self.dfs(board,next_x,next_y):
                        return 1
                    board[x][y]="."
                    self.bo1[x][num] = True
                    self.bo2[y][num] = True
                    self.bo3[num_block][num] = True
        else:
            return self.dfs(board,next_x,next_y)
        return 0

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.bo1=[[True for _ in range(9)] for _ in range(9)]
        self.bo2 = [[True for _ in range(9)] for _ in range(9)]
        self.bo3 = [[True for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    num_block = (i // 3) * 3 + j // 3
                    num=int(board[i][j])
                    self.bo1[i][num-1]=False
                    self.bo2[j][num-1]=False
                    self.bo3[num_block][num-1]=False
        self.dfs(board,0,0)
        return self.ans
