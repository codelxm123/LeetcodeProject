class Solution(object):
    def __init__(self):
        self.m_dict={"2":['a','b','c'],"3":['d','e','f'],"4":['g','h','i'],"5":['j','k','l'],"6":['m','n','o'],"7":['p','q','r','s'],"8":['t','u','v'],"9":['w','x','y','z']}
        self.m_str=""
        self.ans_list=[]
    def dfs(self,m,n,digits):
        if (m==n):
            self.ans_list.append(self.m_str)
        else:
            prev=self.m_str
            for ch in self.m_dict[digits[m]]:
                self.m_str+=ch
                self.dfs(m+1,n,digits)
                self.m_str=prev
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        n=len(digits)
        if n==0:
            return []
        self.dfs(0,n,digits)
        return self.ans_list
m_solution=Solution()
print(m_solution.letterCombinations("24554"))