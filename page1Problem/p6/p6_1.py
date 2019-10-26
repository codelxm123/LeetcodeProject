class Solution(object):
    def getCols(self,s,numRows):
        nowlen=len(s)
        x = 0
        j = 0
        while (x < nowlen):
            x += numRows
            j += 1
            if (x < nowlen):
                remain = nowlen - x
                if (remain <= numRows - 2):
                    return j+remain
                j+=numRows-2
                x+=numRows-2
            else:
                return j
        return j
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        nowlen=len(s)
        n=numRows
        if (n==1):
            return s
        m=self.getCols(s,numRows)
        ch=[['' for i in range(m)] for j in range(n)]
        nowlen = len(s)
        nowm = -1
        x = 0
        while (x < nowlen):
            nowm += 1
            remain = nowlen - x
            for i in range(min(remain, n)):
                ch[i][nowm] = s[x]
                x += 1
            if (x < nowlen):
                remain = nowlen - x
                for k in range(min(remain, n - 2)):
                    nowm += 1
                    ch[n - k - 2][nowm] = s[x]
                    x += 1
        resStr=""
        """
        for i in range(n):
            for j in range(m):
                print(ch[i][j],end=' ')
            print()
        """
        for i in range(n):
            for j in range(m):
                if (not ch[i][j]==' '):
                    resStr+=ch[i][j]
        return resStr

s=input()
numRows=int(input())
my_solution=Solution()
print(my_solution.convert(s,numRows))
