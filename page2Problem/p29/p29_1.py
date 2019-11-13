#参考评论区高赞
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign=(dividend>0)^(divisor>0) #同号为0异号为1
        dividend=abs(dividend)
        divisor=abs(divisor)
        count=0 #下面考虑二进制除法处理
        while dividend>=divisor:
            count+=1
            divisor<<=1
        result=0
        while count>0:
            count-=1
            divisor>>=1
            if divisor<=dividend:  #相当于二进制上这个结果是1
                result+=1<<count
                dividend-=divisor
        if sign:
            result=-result   #sign=1，最后应当是负号
        return result if -(1<<31)<=result<=(1<<31)-1 else (1<<31)-1
