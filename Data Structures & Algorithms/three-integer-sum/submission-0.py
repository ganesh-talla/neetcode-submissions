class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for i in range(len(nums)):
            target = -nums[i]
            d=defaultdict(int)
            for j in range(i+1,len(nums)):
                if target-nums[j] in d and d[target-nums[j]]>0:
                    ans.add(tuple(sorted([nums[i], target-nums[j], nums[j]])))
                else:
                    d[nums[j]] += 1
        return [list(t) for t in ans]