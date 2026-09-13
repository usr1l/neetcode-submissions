class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = dict()
        for i in range(len(nums)):
            if target - nums[i] not in tracker:
                tracker[nums[i]] = i

            else:
                return [min(i, tracker[target-nums[i]]),max(i, tracker[target-nums[i]])]
                    