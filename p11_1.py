#超时
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        s=0
        for i in range(n):
            for j in range(n):
                s=max(s,min(height[i],height[j])*(j-i))
        return s

n=int(input())
m_list=[]
for i in range(n):
    m=int(input())
    m_list.append(m)
my_solution=Solution()
print(my_solution.maxArea(m_list))