class Solution:
    def isPalindrome(self, x: int) -> bool:
        newint=str(x)
        i=0
        j=len(newint)-1
        while i<=j:
            if newint[i]==newint[j]:
                i+=1
                j-=1
            else:
                return False
        return True
        