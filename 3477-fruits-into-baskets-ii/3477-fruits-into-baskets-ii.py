class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count=0
        for i in fruits:
            j=0
            for j in range(len(baskets)):
                if baskets[j]-i>=0:
                    baskets[j]=0
                    break
        for i in baskets:
            if i!=0:
                count+=1

        return count
                
        