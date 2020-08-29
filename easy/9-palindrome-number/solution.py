class Solution(object):
    def isPalindrome(self, x):
        """
        EZ while using str.
        Try without ?
        """
        value_to_test = str(x)
        pointer_left = 0
        pointer_right = len(value_to_test) - 1

        while pointer_left != pointer_right and pointer_right > pointer_left:
            if value_to_test[pointer_left] != value_to_test[pointer_right]:
                return False
            else:
                pointer_left += 1
                pointer_right -= 1

        return True

print(Solution().isPalindrome(11))
print(Solution().isPalindrome(121))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(10))