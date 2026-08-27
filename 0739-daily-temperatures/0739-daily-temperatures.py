class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        ans=[0]*len(temp)
        stack=[]
        # for i in range(len(temp)):
        #     stack.append(temp[i])
        #     j=i+1
        #     while stack and j<len(temp):
        #         if temp[j]>stack[-1]:
        #             a=j
        #             break 
        #         a=i
        #         j+=1
        #     ans[i]=(a-i)
        #     stack.pop()
        # ans[-1]=0
        # return ans   

        for i in range(len(temp)):
            while stack and temp[i]>temp[stack[-1]]:
                ans[stack[-1]]=i-stack[-1]
                stack.pop()
            stack.append(i)
        return ans
        