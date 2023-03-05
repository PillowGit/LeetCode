"""wrong
class Solution:
    def possibleSubarrays(self, amnt):
        return (amnt*(amnt+1))//2
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        l = 0
        r = 1
        answer = 0
        def isValid(left, right) -> bool:
            slice = nums[left:right]
            return right < len(nums) and min(nums[left:right]) == minK and max(nums[left:right]) == maxK

        while r < len(nums):
            while isValid(l,r):
                r += 1
            answer += self.possibleSubarrays(l-r-1)
            l = r
            r += 1
            

        return answer
    """
class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:

        return -1

nums = [1,3,5,2,7,5]
minK = 1
maxK = 5
print(Solution().countSubarrays(nums, minK, maxK))
nums2 = [1,1,1,1]
minK2 = 1
maxK2 = 1
print(Solution().countSubarrays(nums2, minK2, maxK2))
