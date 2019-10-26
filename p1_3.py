class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m_map=dict()
        n=len(nums)
        m_map[nums[0]]=0
        for i in range(1,n):
            remain=target-nums[i]
            if m_map.__contains__(remain):
                return (m_map[remain],i)
            m_map[nums[i]]=i

a=Solution()
print(a.twoSum([3,2,4],6))