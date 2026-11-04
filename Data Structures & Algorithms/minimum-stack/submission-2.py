class MinStack:

    def __init__(self):
        self.stack = []
        self.minElemstack = []

        

    def push(self, val: int) -> None:
        if len(self.minElemstack)==0:
            self.minElemstack.append(val)
        else:
            self.minElemstack.append(min(val,self.minElemstack[-1]))
        self.stack.append(val)
        # print(self.stack)
        # print(self.minElemstack)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minElemstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minElemstack[-1]
        
