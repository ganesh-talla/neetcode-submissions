class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if target-nums[i] in d:
                return [min(i,d[target-nums[i]]),max(i,d[target-nums[i]])]
            d[nums[i]] = i
        
    