class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        if (n<=1):
            return 0
        ans=0
        head=-1
        while head<n-1:
            head+=1
            if s[head]=="(":
                tail=head
                num=1
                while (tail<n-1):
                    tail+=1
                    if s[tail]==")":
                        num-=1
                        if (num<0):
                            head=tail
                            break
                        if (num==0):
                            ans=max(ans,tail-head+1)
                    else:
                        num+=1
                if (tail==n-1):
                    break
        tail=n
        while tail>0:
            tail-=1
            if s[tail]==")":
                head=tail
                num=1
                while (head>0):
                    head-=1
                    if s[head]=="(":
                        num-=1
                        if (num<0):
                            tail=head
                            break
                        if (num==0):
                            ans=max(ans,tail-head+1)
                    else:
                        num+=1
                if (head==0):
                    break
        return ans
