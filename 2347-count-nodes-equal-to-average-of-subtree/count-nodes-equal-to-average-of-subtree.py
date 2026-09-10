class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0
        
        def dfs(node):
            if not node:
                return 0, 0  # sum, size
            
            left_sum, left_size = dfs(node.left)
            right_sum, right_size = dfs(node.right)
            
            total_sum = left_sum + right_sum + node.val
            total_size = left_size + right_size + 1
            
            if node.val == total_sum // total_size:
                self.count += 1
            
            return total_sum, total_size
        
        dfs(root)
        return self.count