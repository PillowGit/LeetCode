class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    paths = defaultdict(int)
    duplicates = []

    def dfs(self, node):
        if not node: return ''
        leftPath, rightPath = self.dfs(node.left), self.dfs(node.right)
        path = f'l{leftPath}{node.val}{rightPath}r'
        self.paths[path] += 1
        if self.paths[path] == 2:
            self.duplicates.append(node)
        return path

    def findDuplicateSubtrees(self, root):
        self.dfs(root)
        return self.duplicates
        