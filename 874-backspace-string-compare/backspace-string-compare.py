class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack=[]
        stack1=[]
        for ch in s:
            if ch=='#':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        for ch1 in t:
            if ch1=="#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(ch1)
        return stack==stack1
