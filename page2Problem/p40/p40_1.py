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
            num = candidates[nown][0]
            if candidates[nown][1]>0:
                candidates[nown][1] -= 1
                self.res.append(num)
                self.dfs(candidates, nown, remain - num)
                self.res.pop()
                candidates[nown][1]+=1
            self.dfs(candidates, nown + 1, remain)
            return 0

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(candidates)
        if n == 0:
            return []
        candidates.sort()
        m_candidates=[]
        pre=candidates[0]
        num=0
        for i in range(n):
            if (candidates[i]==pre):
                num+=1
            else:
                m_candidates.append([pre,num])
                num=1
                pre=candidates[i]
        m_candidates.append([pre, num])
        self.dfs(m_candidates, 0, target)
        return self.ans
