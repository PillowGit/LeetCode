class Solution:
    visited_indices = []
    def minJumps(self, arr: list[int]) -> int:
        if len(arr) == 1: return 0
        self.visited_indices = []
        # Dict of values and indices
        elements = dict()
        for i in range(len(arr)):
            if arr[i] not in elements:
                elements[arr[i]] = [i]
            else:
                elements[arr[i]] += [i]
        # Dependency Variables
        valid = range(len(arr))
        goal = len(arr)-1
        q = [[0,0]]
        self.visited_indices.append(0)

        while len(q) != 0:
            if q[0][0] == goal: return q[0][1]
            pos = q[0]
            q = q[1:]
            print(pos)
            for x in [pos[0]-1, pos[0]+1]:
                if (x in valid) and (not x in self.visited_indices):
                    self.visited_indices.append(x)
                    q.append([x, pos[1]+1])
            if arr[pos[0]] in elements:
                for ind in elements[arr[pos[0]]]:
                    if ind in valid:
                        self.visited_indices.append(ind)
                        q.append([ind, pos[1]+1])
                del elements[arr[pos[0]]]

        return -1


arr = [100,-23,-23,404,100,23,23,23,3,404]
arr2 = [7,6,9,6,9,6,9,7]
print('Example 1: ', arr, '\n', Solution().minJumps(arr))
print('Example 2: ', arr2, '\n', Solution().minJumps(arr2))
