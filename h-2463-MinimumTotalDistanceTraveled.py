"""First (failed) draft
class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        # factory_indices = [x[0] for x in factory]
        # full_range = (min(min(robot), min(factory_indices)), max(max(robot), max(factory_indices)))
        ans = 0
        for f in factory:
            if len(robot) == 0: break
            if f[1] == 0: continue
            distances = dict()
            for r in robot:
                dist = abs(f[0]-r)
                if not dist in distances:
                    distances[dist] = [r]
                else:
                    distances[dist] += [r]
            while f[1] > 0:
                if len(robot) == 0: break
                min_dist = min(distances.keys())
                to_remove = min(distances[min_dist])
                print('Fixing ', to_remove, ' with factory ' , f)
                print('Robots:\n', robot)
                print('Distances:\n' ,distances)
                f[1] -= 1
                ans += min_dist
                distances[min_dist].remove(to_remove)
                robot.remove(to_remove)
                if len(distances[min_dist]) == 0: del distances[min_dist]
            print(f, distances)

        return ans
"""


# Wrong, did not complete
class Solution:
    ans = 0
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        # Construct factories as a dict
        factory.sort()
        factories = dict() # {pos, limit}
        for f in factory:
            if not f[0] in factory:
                factories[f[0]] = f[1]
            else:
                factories[f[0]] += f[1]
        # Prepare Robots for fixing
        def fixRobot(r, dist):
            factories[r] -= 1
            if factories[r] == 0: del factories[r]
            self.ans += dist
        robots_and_dists = []
        for r in robot:
            left, right = r, r
            while left not in factories and right not in factories:
                left -= 1
                right += 1
            dist = abs(left - r)
            robots_and_dists.append([dist, r])
        robots_and_dists.sort()
        print(robots_and_dists)
        priority_queue = [x[1] for x in robots_and_dists]
        # Fix robots
        for r in priority_queue:
            if r in factories:
                fixRobot(r, 0)
                continue
            left, right = r, r
            while left not in factories and right not in factories:
                left -= 1
                right += 1
            fixRobot(left if left in factories else right, abs(r-(left if left in factories else right)))

        # yay
        return self.ans

robot = [9,11,99,101]
factory = [[10,1],[7,1],[14,1],[100,1],[96,1],[103,1]]
robot2 = [1,-1]
factory2 = [[-2,1],[2,1]]
print('First example: ', Solution().minimumTotalDistance(robot, factory))
print('Second example: ', Solution().minimumTotalDistance(robot2, factory2))
