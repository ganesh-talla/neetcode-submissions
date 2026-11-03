from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i]+=1
        
        dList = defaultdict(list)
        for i in d:
            dList[d[i]].append(i)
        
        ans = []
        for i in range(len(nums),0,-1):
            if dList[i]!=[]:
                for j in dList[i]:
                    ans.append(j)
        return ans[:k]
