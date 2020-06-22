class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        result = currentValue = start

        if n > 1:
            for index in range(n - 1):
                if index == 0:
                    result = currentValue ^ currentValue + 2
                else:
                    result = result ^ currentValue + 2

                currentValue = currentValue + 2

        return result

        
print(Solution().xorOperation(5,0))
print(Solution().xorOperation(4,3))
print(Solution().xorOperation(1,7))
print(Solution().xorOperation(10,5))