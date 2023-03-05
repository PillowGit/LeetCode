class Solution:
    def cycleLengthQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        # Generates a set representing a nodes path up the tree
        def generatePath(n):
            if n == 1: return set([1])
            path = set()
            while n != 1:
                path.add(n)
                n = n//2
            return path
        
        cycle_lengths = []
        for query in queries:
            cycle_lengths += [len( generatePath(query[0]).symmetric_difference(generatePath(query[1])) ) + 2]
        return cycle_lengths
