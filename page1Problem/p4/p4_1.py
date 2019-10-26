class Solution(object):
    def m_findKth(self,nums1,low1,high1,nums2,low2,high2,k):
        m1=(low1+high1)//2
        m2=(low2+high2)//2
        pass
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1=len(nums1)
        n2=len(nums2)
        t=[]
        if (n1>=n2):
            t=nums1
            nums1=nums2
            nums2=t
        if (n1==0):
            if (n2%2==0):
                return (nums2[n2//2]+nums2[n2//2-1])/2
            else:
                return nums2[n2//2]
        else:
            sumlen=n1+n2
            ans=self.m_findKth(self,nums1,1,n1,nums2,1,n2,sumlen//2+1)
            if (sumlen%2==0):
                ans=(ans+self.m_findKth(self,nums1,1,n1,nums2,1,n2,sumlen//2))/2
            return ans
