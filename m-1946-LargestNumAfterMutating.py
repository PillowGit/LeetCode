class Solution:
    def maximumNumber(self, num: str, change: list[int]):
        mappings = {x:change[x] for x in range(10)}
        number = [int(x) for x in num]
        changed = False
        for i in range(len(number)):
            if changed and mappings[number[i]] < number[i]:
                break
            if mappings[number[i]] > number[i]:
                changed = True
                number[i] = mappings[number[i]]
        return ''.join([str(x) for x in number])


num = "132"
change = [9,8,5,0,3,6,4,2,6,8]
print(Solution().maximumNumber(num, change))
