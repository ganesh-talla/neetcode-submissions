class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1]*len(nums)
        suffix_prod = [1]*len(nums)
        for i in range(1,len(nums)):
            prefix_prod[i] = nums[i-1]*prefix_prod[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            suffix_prod[i] = suffix_prod[i+1]*nums[i+1]

        print(suffix_prod)
        print(prefix_prod)

        ans = []
        for i in range(len(nums)):
            ans.append(prefix_prod[i]*suffix_prod[i])
        
        return ans

        