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



## 22.02.07
### [66. Plus One](https://leetcode.com/problems/plus-one/)
정수 배열 digit(단, digit[i]는 i번째 정수 자릿수)을 1 증가시킨 어레이를 반환하라.

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plusOne = 0
        for (i, num) in enumerate(reversed(digits)):
            plusOne += 10 ** i * num
        plusOne += 1
        result = list(map(int, str(plusOne)))
        return result
```

#### 풀이법
digit을 reversed로 역순으로 만들어 10의 i(인덱스) 제곱을 한 수를 각 자릿수에 곱해준다.
1을 더한 후 map으로 어레이를 만들어 반환



## 22.02.09
### [884. Uncommon Words from Two Sentences](https://leetcode.com/problems/uncommon-words-from-two-sentences/)
주어진 두 문장에서 중복되지 않고 한번 나타나는 단어의 리스트를 반환하라.

- dictionary
```python
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        list = s1.split() + s2.split()
        dict = {}
        result = []
        for word in list:
            if dict.get(word):
                dict[word] += 1
            else:
                dict[word] = 1
        for key, value in dict.items():
            if value == 1:
                result.append(key)
        return result
```

- counter
```python
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        result = []
        counter = Counter(s1.split() + s2.split())
        for key in counter:
            if counter[key] == 1:
                result.append(key)
        return result 
```

#### 풀이법
dictionary 또는 counter로 만들어서 단어를 key 값으로 하고 단어의 빈도수를 value로 할 때, value가 1인 단어만 리스트에 넣어 반환한다.



## 22.02.15.화
### [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal)
트리 전위순회 -> 후위순회

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                result.insert(0, node.val) # append(node.val)
                stack.append((node.left))
                stack.append(node.right)
        return result
        # return result[::-1]
    
        # if root == None:
        #     return []
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

```
