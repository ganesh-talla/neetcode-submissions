class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append((temperatures[i], i))
                continue
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                ans[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temperatures[i], i))
        return ans



        