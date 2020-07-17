class Solution(object):
    def addBinary(self, a, b):
        """
        - Convert a and b into integers x and y, x will be used to keep an answer, and y for the carry.
        - Carry non -zero
        - While carry is nonzero: y != 0:
        - Current answer without carry is XOR of x and y: answer = x^y.
        - Current carry is left-shifted AND of x and y: carry = (x & y) << 1.
        - Job is done, prepare the next loop: x = answer, y = carry.
        """
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]


print(Solution().addBinary('11', '1011'))