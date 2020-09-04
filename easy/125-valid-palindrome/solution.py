class Solution(object):
    def isPalindrome(self, s):
        """
        acceptable
        """
        value_to_check = "".join(filter(str.isalnum, str(s).lower()))
  
        if value_to_check == "" or len(value_to_check) <= 1:
            return True

        pointer_begin = 0
        pointer_end = len(value_to_check) - 1

        while pointer_begin != pointer_end and pointer_begin < pointer_end:
            if value_to_check[pointer_begin] != value_to_check[pointer_end]:
                return False

            pointer_begin += 1
            pointer_end -= 1

        return True


print(Solution().isPalindrome("aa"))
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome(""))
print(Solution().isPalindrome(" "))
print(Solution().isPalindrome(".,"))
