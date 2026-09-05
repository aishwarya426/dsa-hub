class Solution:
    def summ(self, n: int) -> int:
        summ=0
        while n>0:
            num=n%10
            summ+=num*num
            n=n//10
        return summ

    def isHappy(self, n: int) -> bool:
        if self.summ(n)==1:
            return True

        slow=n
        fast=n
        while True:
            slow=self.summ(slow)
            fast=self.summ(self.summ(fast))
            if slow==fast:
                return False
            
            elif slow==1 or fast==1:
                return True

        
        
        