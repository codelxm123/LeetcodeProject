#评论区参考
class Solution(object):
    def findKth(self,nums1,st1,nums2,st2,k):
        if (st1>len(nums1)-1):
            return nums2[st2+k-1]
        if (st2>len(nums2)-1):
            return nums1[st1+k-1]
        if (k==1):
            return min(nums1[st1],nums2[st2])
        mid1=2147483647
        mid2=2147483647
        if (st1+k//2-1<len(nums1)):
            mid1=nums1[st1+k//2-1]
        if (st2+k//2-1<len(nums2)):
            mid2=nums2[st2+k//2-1]
        if (mid1<mid2):
            return self.findKth(nums1,st1+k//2,nums2,st2,k-k//2)
        else:
            return self.findKth(nums1,st1,nums2,st2+k//2,k-k//2)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if (len(nums1)==0 and len(nums2)==0):
            return 0.0
        m=len(nums1)
        n=len(nums2)
        l=(m+n+1)//2
        r=(m+n+2)//2
        if (l==r):
            return self.findKth(nums1,0,nums2,0,l)
        else:
            return (self.findKth(nums1,0,nums2,0,l)+self.findKth(nums1,0,nums2,0,r))/2.0
