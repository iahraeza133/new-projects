from typing import List

class Solution:
    def twoSum(self, numbers: List[int], goal: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == goal:
                    return [i, j]


solution = Solution()
numbers = [2, 7, 11, 15]
goal = 9
print(solution.twoSum(numbers, goal))  
