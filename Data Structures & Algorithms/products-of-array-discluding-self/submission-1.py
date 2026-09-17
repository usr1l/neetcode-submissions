class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multiplier = 1
        res = [1 for _ in nums]
        for i in range(len(nums[:-1])):
            multiplier *= nums[i]
            res[i+1] *= multiplier

        multiplier = 1
        for i in range(len(nums)-1, 0, -1):
            multiplier *= nums[i] 
            res[i-1] *= multiplier

        return res
        ''