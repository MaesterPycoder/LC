class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        lst = [1] * n

        for i in range(1, n):
            lst[i] = lst[i-1]*nums[i-1]
        
        right = nums[-1]
        for j in range(n-2, -1, -1):
            lst[j] = lst[j]*right
            right *= nums[j]
    

           
        return lst
