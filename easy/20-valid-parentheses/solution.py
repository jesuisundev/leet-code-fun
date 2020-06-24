class Solution(object):
    def isValid(self, s):
        """
        Using a stack for temp and poping
        """

        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for letter in s:
            if self.isOpenChar(letter):
                stack.append(letter)
            else:
                if stack:
                    if stack[-1] != mapping[letter]:
                        return False
                    else:
                        stack.pop()
                else:
                    return False

        return not stack


    def isOpenChar(self, char):
        if char == '{' or char == '[' or char == '(':
            return True
        
        return False


print(Solution().isValid(
    "{}"
))

print(Solution().isValid(
    "{[]}"
))

print(Solution().isValid(
    "()[]{}"
))

print(Solution().isValid(
    "(]"
))

print(Solution().isValid(
    "([)]"
))

print(Solution().isValid(
    "]"
))
