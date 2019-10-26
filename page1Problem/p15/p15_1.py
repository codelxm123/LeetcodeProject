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
        head=0
        while (head<n-2):
            mid=head+1
            tails=n-1
            while (mid<n-1):
                remain=0-nums[head]-nums[mid]
                while (tails>mid and nums[tails]>remain):
                    tails-=1
                if (tails<=mid):
                    break
                elif (nums[tails]==remain):
                    res.append([nums[head],nums[mid],remain])
                pre_midnum=nums[mid]
                while (mid<=n-1 and nums[mid]==pre_midnum):
                    mid+=1

            pre_headnum=nums[head]
            while (head<=n-2 and nums[head]==pre_headnum):
                head+=1

        return res
