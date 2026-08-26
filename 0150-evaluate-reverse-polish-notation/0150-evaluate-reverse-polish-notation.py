class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if tokens[i] not in "+-/*":
                stack.append(int(tokens[i]))
            elif tokens[i] == "*" or tokens[i] == "/" or tokens[i] == "+" or tokens[i]=="-":
                b= stack[-1]
                stack.pop()
                a=stack[-1]
                stack.pop()
                if tokens[i]=="*":
                    stack.append(a*b)
                elif tokens[i]=="/":
                    stack.append(int(a/b))
                elif tokens[i]=="+":
                    stack.append(a+b)
                elif tokens[i]=="-":
                    stack.append(a-b)
                

        return (stack[-1])


        

        