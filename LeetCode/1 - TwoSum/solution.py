# remove the line below for leetcode 
from typing import List 

# Time Complexity is n^2

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i] + nums[j]) == target and (i != j):
                    return [i, j]

# test cases - remove for leetcode 

arr = [3, 3]
target = 6

u = Solution()
print(u.twoSum(arr, target))