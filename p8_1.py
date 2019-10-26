class Solution(object):
    def greater(self,stra,strb):
        return True if (len(stra)>len(strb) or len(stra)==len(strb) and stra>strb) else False
    def nozero(self,str):
        head=0
        n=len(str)
        while (head<n and str[head]=="0"):
            head+=1
        if (head==n):
            return "0"
        else:
            return str[head:n]

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if (str==""):
            return 0
        n=len(str)
        head=-1
        flag=True
        for i in range(n):
            if not str[i]==" ":
                head=i
                break
        strnum=""
        if (head==-1):
            return 0
        if (str[head]=="-"):
            flag=False
        elif (str[head]=="+"):
            flag=True
        elif (str[head]>="0" and str[head]<="9"):
            flag=True
            head-=1
        else:
            return 0
        for j in range(head+1,n):
            if str[j]<"0" or str[j]>"9":
                break
            else:
                strnum+=str[j]
        if strnum=="":
            return 0
        strnum=self.nozero(strnum)
        if (flag):
            if self.greater(strnum,"2147483647"):
                return 2147483647
            else:
                return int(strnum)
        else:
            if self.greater(strnum,"2147483648"):
                return -2147483648
            else:
                return -int(strnum)


m_solution=Solution()
for _ in range(100):
    str=input()
    print(m_solution.myAtoi(str))