class Solution(object):
    def longestPalindrome(self,s):
        n=len(s)
        maxs=""
        maxlen=0
        #奇
        for i in range(n):
            head=i
            tail=i
            nowlen=-1
            while (head>=0 and tail<n and s[head]==s[tail]):
                nowlen+=2
                head-=1
                tail+=1
            if (nowlen>maxlen):
                maxlen=nowlen
                maxs=s[head+1:tail]
        #偶
        for i in range(1,n):
            head=i-1
            tail=i
            nowlen=0
            while (head>=0 and tail<n and s[head]==s[tail]):
                nowlen+=2
                head-=1
                tail+=1
            if (nowlen>maxlen):
                maxlen=nowlen
                maxs=s[head+1:tail]
        return maxs
