class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        newn=0
        n=len(nums)
        for i in range(n):
            if not (nums[i]==val):
                nums[newn]=nums[i]
                newn+=1
        return newn
