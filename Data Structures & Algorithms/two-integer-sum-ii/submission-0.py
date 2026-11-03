class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans=[]
        d = {}
        for i in range(len(numbers)):
            if numbers[i] in d:
                ans = [d[numbers[i]]+1,i+1]
                break
            d[target - numbers[i]] = i
        return ans

