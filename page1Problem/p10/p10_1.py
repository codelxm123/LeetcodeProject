class Solution(object):
    def __init__(self):
        self.result=[]
    def dfs(self,s,st1,m_p,st2):
        if (st2>=len(m_p)):
            return False
        if (st1==len(s)):
            k=st2
            if (not self.result[st1][k]==-1):
                return True if self.result[st1][k]==1 else False
            while (k<len(m_p) and m_p[k][1]==-1):
                k+=1
            if (k==len(m_p)):
                self.result[st1][st2]=1
                return True
            else:
                self.result[st1][st2] = 0
                return False
        if (not self.result[st1][st2]==-1):
            return True if self.result[st1][st2] == 1 else False
        if (m_p[st2][0]==s[st1] or m_p[st2][0]=="."):
            flag=self.dfs(s,st1+1,m_p,st2+1)
            if (m_p[st2][1]==-1):
                flag=flag or self.dfs(s,st1+1,m_p,st2) or self.dfs(s,st1,m_p,st2+1)
            self.result[st1][st2]=1 if flag else 0
            return flag
        else:
            if (m_p[st2][1]==-1):
                self.result[st1][st2]=self.dfs(s,st1,m_p,st2+1)
                return self.result[st1][st2]
            else:
                self.result[st1][st2] = False
                return False
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        x=len(p)
        m_s=[]
        for i in range(x):
            if (p[i]=="*"):
                m_s[-1][1]=-1
            else:
                m_s.append([p[i],1])
        if (len(m_s)==0):
            if (len(s)==0):
                return True
            else:
                return False
        m_s.append(["*",-1])
        self.result=[[-1 for _ in range(len(m_s))] for _ in range(len(s)+1)]
        return self.dfs(s,0,m_s,0)
