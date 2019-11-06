class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)==0:
            return 0
        n=len(nums)
        k=0
        tail=n-1
        while (tail>0 and nums[tail]<=nums[tail-1]):
            tail-=1
        if (tail==0):
            head=0
            tail=n-1
            while (head<tail):
                t=nums[head]
                nums[head]=nums[tail]
                nums[tail]=t
                head+=1
                tail-=1
            return 0
        l1=tail-1
        l2=tail
        m_num=nums[l1]
        while (l2<n and nums[l2]>m_num):
            l2+=1
        l2-=1
        t=nums[l1]
        nums[l1]=nums[l2]
        nums[l2]=t
        head=l1+1
        tail=n-1
        while (head<tail):
            t = nums[head]
            nums[head] = nums[tail]
            nums[tail] = t
            head += 1
            tail -= 1
        return 0
