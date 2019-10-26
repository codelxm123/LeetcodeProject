class Solution(object):
    def __init__(self):
        self.m_list=[('I',1),("IV",4),('V',5),("IX",9),('X',10),("XL",40),('L',50),("XC",90),('C',100),("CD",400),('D',500),("CM",900),('M',1000)]
    def is_start(self,s,str,start_num):
        if len(s)-start_num<len(str):
            return False
        for i in range(len(str)):
            if not (str[i]==s[start_num+i]):
                return False
        return True
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        m_list=self.m_list
        ans=0
        head=0
        while (head<len(s)):
            for i in reversed(range(len(m_list))):
                str,num=m_list[i]
                if (self.is_start(s,str,head)):
                    head+=len(str)
                    ans+=num
                    break
        return ans
