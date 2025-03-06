from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = m-1
        j = n-1
        k = m+n-1
        
        while i>=0 and j>=0:
            if(nums1[i]>=nums2[j]):
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1
        
        if j>=0:
            nums1[i+1:k+1] = nums2[0:j+1]
        
        return nums1
        
if __name__ == "__main__":
    s = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    print(s.merge(nums1,m,nums2,n))
    print("\n================\n")
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    print(s.merge(nums1,m,nums2,n))
    print("\n================\n")
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    print(s.merge(nums1,m,nums2,n))
    print("\n================\n")
    nums1 = [2,0]
    m = 1
    nums2 = [1]
    n = 1
    print(s.merge(nums1,m,nums2,n))
    print("\n================\n")
    nums1 = [4,5,6,0,0,0]
    m = 3
    nums2 = [1,2,3]
    n = 3
    print(s.merge(nums1,m,nums2,n))
    
