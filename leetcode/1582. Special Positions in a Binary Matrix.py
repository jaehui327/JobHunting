from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        result = 0
        for n in mat:
            for j, m in enumerate(n):
                if m == 1:
                    x = 0
                    for a in n:
                        x += a
                    for b in range(0, len(mat)):
                        x += mat[b][j]
                    if x == 2:
                        result += 1
        return result

sol = Solution()
print(sol.numSpecial([[1, 0, 0], [0, 0, 1], [1, 0, 0]]))
print(sol.numSpecial([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))


