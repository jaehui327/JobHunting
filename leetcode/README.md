# leetcode

## 22.01.26
### 1582. Special Positions in a Binary Matrix
https://leetcode.com/problems/special-positions-in-a-binary-matrix
m x n 배열 mat에서 mat[i][j]가 1일 때, i행과 j행의 다른 값이 모두 0인 값의 개수를 찾아라.


```python
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
```

#### 풀이법
mat[i][j]의 값이 1일 때 i행과 j열에서 유일한 1의 값이려면,
같은 리스트(i행)에 속한 값들의 합과 같은 열(j열)에 속한 값들의 합이 항상 2이다.

