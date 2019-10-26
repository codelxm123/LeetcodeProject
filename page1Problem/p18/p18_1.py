class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        n=len(nums)
        res_list=[]
        if (n<4):
            return []
        for i in range(n-3):
            if (i==0 or nums[i]>nums[i-1]):
                for j in reversed(range(i+3,n)):
                    if (j==n-1 or nums[j]<nums[j+1]):
                        sum=nums[i]+nums[j]
                        head=i+1
                        tail=j-1
                        while (head<tail):
                            if (head==i+1 or nums[head]>nums[head-1]):
                                if (tail==j-1 or nums[tail]<nums[tail+1]):
                                    sum2=sum+nums[head]+nums[tail]
                                    if (sum2>target):
                                        tail-=1
                                    elif (sum2<target):
                                        head+=1
                                    else:
                                        res_list.append([nums[i],nums[head],nums[tail],nums[j]])
                                        head+=1
                                        tail-=1
                                else:
                                    tail-=1
                            else:
                                head+=1
        return res_list
