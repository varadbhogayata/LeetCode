# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = [root]
        depth = 0
        while queue:
            node = queue.pop(0)
            depth += 1
            for _ in range(len(queue)):
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return depth