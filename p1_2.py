class MyNum:
    def __init__(self,num,id):
        self.num=num
        self.id=id

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        numtosort=[]
        for i in range(n):
            numtosort.append(MyNum(num=nums[i],id=i))
        numtosort=sorted(numtosort,key=lambda  x:(x.num))
        solutions=[]
        sum=0
        i=0
        j=n-1
        while i<j:
            sum=numtosort[i].num+numtosort[j].num
            if (sum==target):
                idx1=numtosort[i].id
                idx2=numtosort[j].id
                if (idx1>idx2):
                    t=idx1
                    idx1=idx2
                    idx2=t
                return (idx1,idx2)
            elif (sum<target):
                i+=1
            else:
                j-=1
        return 0

a=Solution()
print(a.twoSum([2,7,11,15],9))