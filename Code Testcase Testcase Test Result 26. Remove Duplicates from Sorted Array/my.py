class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        i = 1

        while i < len(nums):
            if(nums[i]!=nums[i-1]):
                nums[idx] = nums[i]
                idx+=1
            i+=1

        return idx
