class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if (n==0):
            return 0
        newn=1
        pre=nums[0]
        for i in range(1,n):
            if not (nums[i]==pre):
                pre=nums[i]
                nums[newn]=pre
                newn+=1
        return newn
