class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s=""
        if len(strs) == 0:
            return s
        str_first=strs[0]
        x=len(str_first)
        for str in strs:
            x=min(x,len(str))
        for i in range(x):
            ch=str_first[i]
            for str in strs:
                if not (str[i]==ch):
                    return s
            s=s+ch
        return s
m_solution=Solution()
n=int(input())
str_list=[]
for i in range(n):
    str_list.append(input())
print(m_solution.longestCommonPrefix(str_list))