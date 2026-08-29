class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights=[0]+heights+[0]
        stack=[]
        maxarea=0
        for i,h in enumerate(heights):
            while stack and h<heights[stack[-1]]:
                length=heights[stack[-1]]
                stack.pop()
                area=length*(i-stack[-1]-1)
                maxarea=max(area,maxarea)


            stack.append(i)

        return maxarea


            

                     

                

        

        