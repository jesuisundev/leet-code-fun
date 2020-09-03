class Solution(object):
    """
    time limit exceded
    """
    def __init__(self):
        self.memo = {}

    def countPrimes(self, n):
        count_primes = 0

        for current_index in range(2, n):
            if current_index != n and self.isPrime(current_index):
                count_primes += 1

        return count_primes

    def isPrime(self, n):
        if n in self.memo:
            return self.memo[n]
        else:
            for current_index in range(2, n - 1):
                if n % current_index == 0:
                    self.memo[n] = False
                    return self.memo[n]

            self.memo[n] = True
            return self.memo[n]


#print(Solution().countPrimes(10))
print(Solution().countPrimes(499979))