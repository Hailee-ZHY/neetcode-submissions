class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            ")":"(", 
            "}":"{", 
            "]":"["
        }

        stack = [] # this is a stack

        for i in s:
            if i in pair:
                if stack and stack[-1] == pair[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return len(stack) == 0 