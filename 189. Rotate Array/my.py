class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k%len(nums)

        ##Method0
        # rotated = [0]*len(nums)
        # for i in range(len(nums)):
        #     rotated[(i+k)%len(nums)] = nums[i] 

        # for i in range(len(nums)):
        #     nums[i] = rotated[i]

        ##Method1
        # for i in range(k):
        #     temp = nums[-1]
        #     for j in range(len(nums)-2, -1, -1):
        #         nums[j+1] = nums[j]
        #     nums[0] = temp


        ##Method 2
        # if k != 0:
        #     nums[::] = nums[len(nums)-k::] + nums[:-k:]


        ##Method3
        def reverse(l,r):
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
        reverse(0, len(nums)-1)
        reverse(0, k-1)
        reverse(k, len(nums)-1)
        
