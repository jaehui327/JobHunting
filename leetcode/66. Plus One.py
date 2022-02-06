from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plusOne = 0
        for (i, num) in enumerate(reversed(digits)):
            plusOne += 10 ** i * num
        plusOne += 1
        result = list(map(int, str(plusOne)))
        return result

sol = Solution()
print(sol.plusOne([1,2,3]))
print(sol.plusOne([9]))