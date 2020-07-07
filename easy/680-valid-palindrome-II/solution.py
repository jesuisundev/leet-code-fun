class Solution(object):
    def validPalindrome(self, s):
        """
        looked
        - start from the edge not the middle
        - ignore not delete
        - slow
        """
        currentLeft = 0
        currentRight = len(s) - 1
        
        while currentLeft < currentRight:
            # happy scenario will always go there
            if s[currentLeft] == s[currentRight]:
                currentLeft += 1
                currentRight -= 1
            else:
                # check by ignoring one left letter
                if(self.isPalindrome(currentLeft + 1, currentRight, s)):
                    return True

                # check by ignoring one right letter
                if(self.isPalindrome(currentLeft, currentRight - 1, s)):
                    return True

                return False

        return True


    def isPalindrome(self, currentLeft, currentRight, s):
        while currentLeft < currentRight: 
            if s[currentLeft] != s[currentRight]: 
                return False
            
            currentLeft += 1
            currentRight -= 1
        
        return True



print(Solution().validPalindrome("aba"))
print(Solution().validPalindrome("abca"))
print(Solution().validPalindrome("acba"))
print(Solution().validPalindrome("deeee"))