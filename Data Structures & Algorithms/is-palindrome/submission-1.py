class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        print(l,r)
        while l<r:
            if s[l]==" " or not s[l].isalnum():
                l+=1
                continue
            if s[r]==" " or not s[r].isalnum():
                r-=1
                continue
            
            if s[l].lower() == s[r].lower():
                l+=1
                r-=1
            else:
                print(l,r,s[l],s[r])
                return False
        return True


        