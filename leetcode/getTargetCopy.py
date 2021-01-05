import unittest
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = deque()
        queue.append(cloned)
        while queue:
            node = queue.popleft()
            if node.val == target.val:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


class Test(unittest.TestCase):
    def test_canFormArray(self):
        solution = Solution()
        tree = TreeNode([7, 4, 3, None, None, 6, 19])
        self.assertEqual(solution.getTargetCopy(tree, tree, 3), 3)


if __name__ == '__main__':
    unittest.main()
