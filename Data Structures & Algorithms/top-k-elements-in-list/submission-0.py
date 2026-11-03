from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        d1 = defaultdict(list)
        for i in d:
            d1[d[i]].append(i)
        
        ans = []
        for i in range(len(nums),0,-1):
            if d1[i]!=[]:
                for j in d1[i]:
                    ans.append(j)
        return ans[:k]



        