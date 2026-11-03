class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def encode(word):
            l=[0]*26
            for i in word:
                l[ord(i)-ord('a')] += 1
            return '-'.join(str(i) for i in l)
        d={}
        for i in strs:
            enc = encode(i)
            if enc in d:
                d[enc].append(i)
            else:
                d[enc] = [i]
        ans=[]
        for i in d:
            ans.append(d[i])
        return ans

