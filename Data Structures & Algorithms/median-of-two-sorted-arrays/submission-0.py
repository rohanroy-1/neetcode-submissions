class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        merge=nums1+nums2
        merge.sort()
        total_len = len(nums1)+len(nums2)
        if total_len % 2 == 0:

            return(merge[(total_len//2)-1]+merge[(total_len//2)])/2.0
        else: 
            return merge[total_len//2]

        
        

            

