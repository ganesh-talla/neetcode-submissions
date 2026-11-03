class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pospair=[[p,s] for p,s in zip(position,speed)]
        pospair.sort(reverse=True)

        stack = []
        for pos,spe in pospair:
            stack.append((target-pos)/spe)
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


        