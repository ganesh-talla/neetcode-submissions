from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        maxans = 0
        ans = 0
        for i in nums:
            ans=0
            j = i
            if j-1 not in d:
                while j in d:
                    ans += 1
                    j += 1
                
                maxans = max(ans,maxans)
        return maxans

            
        