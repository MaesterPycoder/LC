class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        prev = nums[0]
        i = 1
        k = 1
        for i in range(1,len(nums)):
            if(nums[i]!=prev):
                prev = nums[i]
                nums[idx] = nums[i]
                idx+=1
                k=1
            else:
                if(k>0):
                    nums[idx] = nums[i]
                    idx+=1
                k-=1

        return idx
