class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['{','[','(']:
                stack.append(i)
            else:
                if len(stack)>0:
                    elem = stack.pop()
                else:
                    return False
                if (i == '}' and elem == '{') or (i == ')' and elem == '(') or (i == ']' and elem == '['):
                    continue
                else:
                    return False
        if len(stack)==0:
            return True
        return False

        