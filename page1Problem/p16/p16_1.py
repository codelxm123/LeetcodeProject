class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums=sorted(nums)
        n=len(nums)
        ans=nums[0]+nums[1]+nums[2]
        delta=abs(nums[0]+nums[1]+nums[2]-target)
        for head in range(n-2):
            mid=head+1
            tail=n-1
            while (mid<tail):
                sum=nums[head]+nums[mid]
                while (tail>mid and sum+nums[tail]>target):
                    tail-=1
                if (tail>mid):
                    x=abs(sum+nums[tail]-target)
                    if x<delta:
                        delta=x
                        ans=sum+nums[tail]
                if (tail+1<n):
                    x = abs(sum + nums[tail+1] - target)
                    if x < delta:
                        delta = x
                        ans = sum + nums[tail+1]
                mid+=1
        return ans
