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
        for i in range(n):
            m_set=set(s[i])
            k=i
            m_max=max(m_max,1)
            while ((k<i+m_max) and (k<n-1)):
                k+=1
                m_set.add(s[k])

            while (len(m_set)==k-i+1 and (k<n-1)):
                k+=1
                m_set.add(s[k])
            if len(m_set) == k - i + 1:
                ans=k-i+1
            else:
                ans=k-i
            m_max=max(m_max,ans)
        return m_max

m=Solution()
print(m.lengthOfLongestSubstring(""))
