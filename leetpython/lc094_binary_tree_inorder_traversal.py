from lib.tree import TreeNode
from lib.core import solution, TestCase
from typing import List


class LC094(TestCase):
    @solution
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


if __name__ == '__main__':
    print(123)
    t = LC094()
    t.add_cases(TreeNode, [1, None, 2, 3])
    t.run()
