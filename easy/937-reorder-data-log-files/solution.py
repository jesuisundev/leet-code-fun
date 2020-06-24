class Solution(object):
    def reorderLogFiles(self, logs):
        """
        using special sorted functions 
        https://www.programiz.com/python-programming/methods/built-in/sorted
        order in the sort !
        #4
        """

        return sorted(logs, key = self.preSortedLogs)


    def preSortedLogs(self, log):
        index, secondArgument = log.split(" ", 1)
        return (0, secondArgument, index) if secondArgument[0].isalpha() else (1,)


print(Solution().reorderLogFiles(
    ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
))
