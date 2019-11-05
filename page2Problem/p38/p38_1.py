class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if (n==1):
            return "1"
        else:
            res=""
            str=self.countAndSay(n-1)
            n=len(str)
            pre=str[0]
            num=1
            for i in range(1,n):
                if str[i]==pre:
                    num+=1
                else:
                    res+="%d"%num+pre
                    pre=str[i]
                    num=1
            res+="%d"%num+pre
            return res
