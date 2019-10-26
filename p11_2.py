class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        s=0
        left_list=[]
        if (n<=1):
            return 0
        left_list.append((height[0],0))
        for i in range(1,n):
            if (height[i]>left_list[-1][0]):
                left_list.append((height[i],i))
        right_list = []
        right_list.append((height[n-1], n-1))
        for i in reversed(range(n-1)):
            if (height[i] > right_list[-1][0]):
                right_list.append((height[i], i))
        n1=len(left_list)
        n2=len(right_list)
        for i in range(n1):
            h1,idx1=left_list[i]
            for j in range(n2):
                h2,idx2=right_list[j]
                if idx2<=idx1:
                    break
                s=max(s,min(h2,h1)*(idx2-idx1))
        return s
m_list=[1,8,6,2,5,4,8,3,7]
my_solution=Solution()
print(my_solution.maxArea(m_list))