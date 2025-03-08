class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(k):
        #     temp = nums[-1]
        #     for j in range(len(nums)-2, -1, -1):
        #         nums[j+1] = nums[j]
        #     nums[0] = temp
        k = k%len(nums)
        if k != 0:
            nums[::] = nums[len(nums)-k::] + nums[:-k:]
        
