class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ['+','-','*','/']:
                b = stack.pop()
                a = stack.pop()
                # print(a,b,i)
                if i == '+':
                    stack.append(a+b)
                elif i == '-':
                    stack.append(a-b)
                elif i == '*':
                    stack.append(a*b)
                elif i == '/':
                    if (a<0 and b<0) or (a>0 and b>0):
                        stack.append(a//b)
                    else:
                        stack.append(math.ceil(a/b))
            else:
                stack.append(int(i))
        return stack[0]



        