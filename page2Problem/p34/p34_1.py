class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if (len(nums)==0):
            return [-1,-1]
        if nums[0]>target:
            return [-1,-1]
        n=len(nums)
        if nums[n-1]<target:
            return [-1,-1]

        left=0
        right=n
        while (left<right):
            mid=left+(right-left)//2
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid
        resleft=left-1
        if (resleft>=0 and not nums[resleft]==target):
            resleft=-1
        if (left<n and nums[left]==target):
            resleft=left

        left = 0
        right = n-1
        while (left < right):
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid+1
        resright = right - 1
        if (resright>=0 and not nums[resright]==target):
            resright=-1
        if (right>=0 and nums[right] == target):
            resright = right

        return [resleft,resright]
