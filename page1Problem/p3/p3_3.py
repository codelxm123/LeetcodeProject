class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        if n==0:
            return 0
        m_max=0
        ord_max=0
        for i in range(n):
            ord_max=max(ord_max,ord(s[i]))
        for i in range(n):
            bo=[True for j in range(ord_max+1)]
            m_max=max(m_max,1)
            bo[ord(s[i])]=False
            k=i+1
            while ((k<n) and bo[ord(s[k])]):
                bo[ord(s[k])]=False
                k+=1
            m_max=max(m_max,k-i)
        return m_max
