class Solution(object):
    def fizzBuzz(self, n):
        """[summary]
        straightforward
        there is a better solution with hashmap
        """
        result = []

        for number in range(1, n + 1):
            if number % 3 == 0 and number % 5 == 0:
                result.append('FizzBuzz')
            elif number % 3 == 0:
                result.append('Fizz')
            elif number % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(number))
        
        return result

print(Solution().fizzBuzz(15))