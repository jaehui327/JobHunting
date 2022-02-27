from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        result = image
        oldColor = result[sr][sc]
        m = len(result)
        n = len(result[0])

        def dfs(i, j):
            result[i][j] = newColor
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and result[x][y] == oldColor:
                    dfs(x, y)

        if oldColor != newColor:
            dfs(sr, sc)

        return result

sol = Solution()
print(sol.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))