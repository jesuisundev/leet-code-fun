import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        hashTable = dict()
        temp = re.sub('[\!\?\'\.,.\;\.]', ' ', paragraph).replace('  ', ' ')
        splitted_paragraph = temp.split(" ")
        
        biggest_seen = 0
        result = ''

        for word in splitted_paragraph:
            lowercase_word = word.lower()

            if lowercase_word not in banned:
                if lowercase_word in hashTable:
                    hashTable[lowercase_word] += 1
                else:
                    hashTable[lowercase_word] = 1
                
                if biggest_seen < hashTable[lowercase_word]:
                    biggest_seen = hashTable[lowercase_word]
                    result = lowercase_word

        return result

print(Solution().mostCommonWord(
    "Bob hit a ball, the hit BALL flew far after it was hit.",
    ["hit"]
))

print(Solution().mostCommonWord(
    "a, a, a, a, b,b,b,c, c",
    ["a"]
))