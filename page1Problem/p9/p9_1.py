class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        my_str=str(x)
        n=len(my_str)
        mid=0
        if n%2==1:
            mid=(n+1)//2
        else:
            mid=n//2
        for i in range(mid):
            if not (my_str[i]==my_str[n-1-i]):
                return False
        return True
