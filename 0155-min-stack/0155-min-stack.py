class MinStack:

    def __init__(self):
        self.arr=[]
        self.minarr=[]
        

    def push(self, value: int) -> None:
        self.arr.append(value)
        if not self.minarr:
            self.minarr.append(value)
        else:
            self.minarr.append(min(value,self.minarr[-1]))
        

    def pop(self) -> None:
        self.arr.pop()
        self.minarr.pop()
        

    def top(self) -> int:
       
        return self.arr[len(self.arr)-1]
        

    def getMin(self) -> int:

        return self.minarr[len(self.minarr)-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()