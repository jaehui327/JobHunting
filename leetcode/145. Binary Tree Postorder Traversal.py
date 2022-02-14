from typing import Optional
from typing import List

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

sol = Solution()
print(sol.postorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))))
