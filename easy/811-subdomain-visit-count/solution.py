class Solution(object):
    def __init__(self):
        self.hashTable = dict()


    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        for cpdomain in cpdomains:
            # init var
            cpdomainArray = cpdomain.split()
            currentNumber = int(cpdomainArray[0])

            self.addToHash(cpdomainArray[1], currentNumber)

            # building cpdomains
            splitedDomains = cpdomainArray[1].split('.')
            splitedDomains.pop(0)

            while len(splitedDomains) != 0:
                self.addToHash('.'.join(splitedDomains), currentNumber)
                splitedDomains.pop(0)


        return self.buildSubdomainVisitCount()


    def addToHash(self, key, number):
        if key in self.hashTable:
            self.hashTable[key] += number
        else:
            self.hashTable[key] = number


    def buildSubdomainVisitCount(self):
        finalArray = []
 
        for sub_domain_key in self.hashTable.keys():
            finalArray.append(str(self.hashTable[sub_domain_key]) + ' ' + sub_domain_key)

        return finalArray


print(Solution().subdomainVisits(["9001 discuss.leetcode.com"]))