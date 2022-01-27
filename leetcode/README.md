# leetcode

## 22.01.26
### [1582. Special Positions in a Binary Matrix](https://leetcode.com/problems/special-positions-in-a-binary-matrix)
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



## 22.01.28
### [1656. Design an Ordered Stream](https://leetcode.com/problems/design-an-ordered-stream/)
There is a stream of n (idKey, value) pairs arriving in an arbitrary order, where idKey is an integer between 1 and n and value is a string. No two pairs have the same id.

Design a stream that returns the values in increasing order of their IDs by returning a chunk (list) of values after each insertion. The concatenation of all the chunks should result in a list of the sorted values.

Implement the OrderedStream class:

- OrderedStream(int n) Constructs the stream to take n values.
- String[] insert(int idKey, String value) Inserts the pair (idKey, value) into the stream, then returns the largest possible chunk of currently inserted values that appear next in the order.

```python
class OrderedStream:

    def __init__(self, n: int):
        self.pre = 1
        self.ptr = 1
        self.last = n + 2
        self.result = [[] for i in range(n + 1)]

    def insert(self, idKey: int, value: str) -> List[str]:
        self.result[idKey] = value
        if idKey > self.ptr:
            self.pre = idKey
            return []
        elif idKey == self.ptr:
            try:
                self.ptr = self.result[idKey:].index([]) + idKey
            except:
                self.ptr = self.last
            return self.result[idKey:self.ptr]
        else:
            self.ptr = idKey
            return self.result[self.pre:idKey]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
```