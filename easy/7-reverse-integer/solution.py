class Solution(object):
    def reverse(self, x):
        """
        using math to get the remainder from the modulo and reverse the number

        - not good approach at first
        - partial
        """
        # make constant for overflow rule
        INT_MAX = 2 ** 31 - 1
        # get the sign of th number to avoid dealing with minus number
        sign = 1 if x >= 0 else -1
        # init temp and make sure minus -> plus
        temp, x = 0, abs(x)

        while x != 0:
            # take the last digit
            last_digit = x % 10
            # delete the last digit from x
            x /= 10

            # checking for overflow before adding the digit
            if temp > INT_MAX // 10 or (temp == INT_MAX // 10 and last_digit > 7): 
                return 0

            # we dont have overflow, we can safely push the digit
            temp = temp * 10 + last_digit
        
        # returning with the right sign
        return temp * sign


print(Solution().reverse(123))
print(Solution().reverse(-123))
print(Solution().reverse(1534236469))

