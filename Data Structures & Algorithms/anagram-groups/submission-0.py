from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #frequency hash technique
        d = defaultdict(list)
        for stri in strs:
            l = [0]*26
            # l = tuple(l)
            for i in stri:
                l[ord(i)-ord('a')] += 1
            d[tuple(l)].append(stri)
        ans = []
        for s in d:
            ans.append(d[s])
        return ans

            
                
        