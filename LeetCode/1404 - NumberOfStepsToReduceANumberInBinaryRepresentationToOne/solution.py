class Solution:
    def numSteps(self, s: str) -> int:
        num_of_steps = 0
        s = int(s, 2)

        while s != 1:
            if s % 2 == 0:
                s //= 2
                num_of_steps += 1
            else:
                s += 1
                num_of_steps += 1
        return num_of_steps
    
u = Solution()
print(u.numSteps("1101"))