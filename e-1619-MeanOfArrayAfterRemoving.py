class Solution:
    def trimMean(self, arr: list[int]) -> float:
        arr.sort()
        size = len(arr)
        five_percent = (5*size)/100
        sum = 0.0
        for i in range(int(five_percent), int(size-five_percent)):
            sum += arr[i]

        return sum/(size-(2*five_percent))


question = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
print(Solution().trimMean(question))
