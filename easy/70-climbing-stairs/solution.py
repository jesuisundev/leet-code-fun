class Solution(object):
    def climbStairs(self, n):
        return self.try_climb(0, n)

    def try_climb(self, current_step, sum_of_step):
        if current_step > sum_of_step:
            return 0

        if current_step == sum_of_step:
            return 1
  
        return self.try_climb(current_step + 1, sum_of_step) + self.try_climb(current_step + 2, sum_of_step)

print(Solution().climbStairs(2))
print(Solution().climbStairs(3))