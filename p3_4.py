class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        if n==0:
            return 0
        ord_max=0
        for i in range(n):
            ord_max=max(ord_max,ord(s[i]))
        bo=[True for j in range(ord_max+1)]
        i=0
        bo[ord(s[0])]=False
        k=1
        while ((k < n) and bo[ord(s[k])]):
            bo[ord(s[k])] = False
            k += 1
        m_max = k - i
        for i in range(1,n):
            bo[ord(s[i-1])]=True
            tail=k
            while ((tail < n) and bo[ord(s[tail])]):
                bo[ord(s[tail])] = False
                tail += 1
            m_max = max(m_max,tail - i)
            k=tail
        return m_max

m=Solution()
print(m.lengthOfLongestSubstring("a "))


