class Solution(object):
    def dfs(self,ans, m_str, nstk, leftn, n):
        if (leftn == n):
            while nstk > 0:
                nstk -= 1
                m_str += ")"
            ans.append(m_str)
            return 0
        m2_str = m_str + "("
        self.dfs(ans, m2_str, nstk + 1, leftn + 1, n)
        if (nstk > 0):
            m2_str = m_str + ")"
            self.dfs(ans, m2_str, nstk - 1, leftn, n)
        return 0

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if (n == 0):
            return []
        ans = []
        self.dfs(ans, "", 0, 0, n)
        return ans
