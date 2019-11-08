class Solution(object):
    def findnum(self,nums,l,r,target):
        if (l>r):
            return -1
        head=l
        tail=r
        while (head<=tail):
            mid=head+(tail-head)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                head=mid+1
            else:
                tail=mid-1
        return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        head=0
        tail=n-1
        if (n==0):
            return -1
        num=nums[tail]
        while (head<tail):
            mid=head+(tail-head)//2
            if nums[mid]<=num:
                tail=mid
            else:
                head=mid+1
        res1=self.findnum(nums,0,head-1,target)
        if (res1==-1):
            res2=self.findnum(nums,head,n-1,target)
            return res2
        else:
            return res1
