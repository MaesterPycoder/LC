class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0
        j = 0
        while(i < len(nums)-j):
            if(nums[i]==val):
                j+=1
                nums[i], nums[len(nums)-j] = nums[len(nums)-j], nums[i]
            if(nums[i]!=val):
                i+=1 
        return len(nums)-j

