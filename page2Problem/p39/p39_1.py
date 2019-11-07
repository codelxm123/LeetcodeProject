class Solution(object):
    def __init__(self):
        self.ans=[]
        self.res=[]

    def dfs(self, candidates, nown, remain):
        if (remain == 0):
            a=[]
            for i in range(len(self.res)):
                a.append(self.res[i])
            self.ans.append(a)
            return 0

        if (nown >= len(candidates)):
            return 0

        if (remain < 0):
            return 0
        else:
            num = candidates[nown]
            self.res.append(num)
            self.dfs(candidates, nown, remain - num)
            self.res.pop()
            self.dfs(candidates, nown + 1, remain)
            return 0

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(candidates)
        if n == 0:
            return []
        self.dfs(candidates, 0, target)
        return self.ans
