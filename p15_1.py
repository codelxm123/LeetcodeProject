#超时
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        res=[]
        n=len(nums)
        if (n<3):
            return res
        for i in range(n-1):
            m=set()
            m.add(nums[i+1])
            for j in range(i+2,n):
                remain=0-nums[i]-nums[j]
                if m.__contains__(remain):
                    x=[nums[i],remain,nums[j]]
                    if not (x in res):
                        res.append(x)
                m.add(nums[j])
        return res
n=int(input())
nums=[]
for _ in range(n):
    nums.append(int(input()))
m_solution=Solution()
print(m_solution.threeSum(nums))