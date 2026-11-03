import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]','',s)
        st,e=0,len(s)-1

        while(st<e): 
            if(s[st]!=s[e]):
                return False
            st+=1
            e-=1

        return True

        