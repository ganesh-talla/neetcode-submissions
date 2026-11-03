class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums)-1
        ans = -1
        while l<=h:
            mid = (l+h)//2
            if nums[mid]==target:
                return mid

            #left sorted    
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    h = mid - 1
            #right sorted
            else:
                if target < nums[mid] or target > nums[h]:
                    h = mid - 1
                else:
                    l = mid + 1
        return -1 
