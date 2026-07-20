class Solution:
    def isValid(self, s: str) -> bool:

        stack = [] #Because I need somewhere to store opening brackets.

        pairs = {
            ')':'(',
            '}':'{',
            ']': '['
        }

        for c in s:
            if c in "([{":
                stack.append(c)

            else: #If it isn't an opening bracket...
                if not stack:  #Is stack empty?
                    return False

                if stack[-1] != pairs[c]: #Does the top match?
                    return False

                stack.pop() #Remove it. match done Correct?

        return len(stack) == 0 #If stack is empty Everything matched.

        