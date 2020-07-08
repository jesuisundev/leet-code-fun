class Solution(object):
    """
    not that bad
    better solution with Floyd's Cycle-Finding Algorithm
    """
    def isHappy(self, n):
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)

            slicedNumber = self.sliceNumberByDigit(n)
            n = self.sumOfSquaredigit(slicedNumber)

        return n == 1


    def sliceNumberByDigit(self, number):
        slicedNumber = []

        while number >= 10:
            slicedNumber.append(number % 10)
            number /= 10
        
        slicedNumber.append(number)

        return slicedNumber


    def sumOfSquaredigit(self, slicedNumber):
        result = 0

        for number in slicedNumber:
            result += number ** 2

        return result



print(Solution().isHappy(19))