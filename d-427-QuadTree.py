class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

# Helper
def makeMatrixString(grid):
    in_string = ''
    for a in range(len(grid)):
        for b in range(len(grid)):
            in_string += (str(grid[a][b]) + ' ')
        in_string += '\n'
    return in_string

# Helper
def bfsPrint(head):
    if not head: print("empty tree")
    q = [head]
    level = 1
    res = ''
    while len(q) != 0:
        res += f"val={q[0].val}, isLeaf={q[0].isLeaf} | "
        for child in [q[0].topLeft, q[0].topRight, q[0].bottomLeft, q[0].bottomRight]:
            if not child is None:
                q.append(child)
        level -= 1
        if level == 0:
            res += '\n'
            level = len(q) - 1
        q.pop(0)
    print(res)
        

class Solution(object):
    def construct(self, grid):
        # Empty Grid
        if len(grid) == 0: return None
        # Grid size 1
        if len(grid) == 1: return Node(grid[0][0] == 1, True, None, None, None, None)

        # Necessary Variable
        headNode = Node(grid[0][0] == 1, True, None, None, None, None)
        
        # Matrix is leaf
        nums = set()
        for i in range(len(grid)):
            nums = nums | set(grid[i])
        if len(nums) == 1: return headNode

        # Matrix is branch
        mid = len(grid) // 2
        headNode.isLeaf = False
        headNode.topLeft = self.construct([grid[a][0:mid] for a in range(mid)])
        headNode.topRight = self.construct([grid[a][mid:] for a in range(mid)])
        headNode.bottomLeft = self.construct([grid[a][0:mid] for a in range(mid, len(grid))])
        headNode.bottomRight = self.construct([grid[a][mid:] for a in range(mid, len(grid))])
        return headNode



sln = Solution()
question = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
print(makeMatrixString(question))
ans = sln.construct(question)
bfsPrint(ans)