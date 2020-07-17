class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sumNumber = 0
        hashTable = { "I": 1, "V": 5, "X": 10, "XL": 40, "L": 50, "C": 100, "D" : 500, "M": 1000 }

        while len(s):
            if len(s) >= 2 and (s[0] == "I" or s[0] == "X" or s[0] == "C"):
                if hashTable[s[0]] < hashTable[s[1]]:
                    sumNumber += hashTable[s[1]] - hashTable[s[0]]
                    s = s[2:]
                else:
                    sumNumber += hashTable[s[0]]
                    s = s[1:]
            else:
                sumNumber += hashTable[s[0]]
                s = s[1:]

        return sumNumber


print(Solution().romanToInt('III'))
print(Solution().romanToInt('IV'))
print(Solution().romanToInt('IX'))
print(Solution().romanToInt('LVIII'))
print(Solution().romanToInt('MCMXCIV'))
print(Solution().romanToInt('MDLXX'))
