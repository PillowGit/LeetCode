class Solution:
    def maximumTime(self, time: str) -> str:
        time_as_ls = list(time)
        # First digit
        if time_as_ls[0] == '?':
            time_as_ls[0] = '2' if time_as_ls[1] == '?' or int(time_as_ls[1]) < 4 else '1'

        # Second digit
        if time_as_ls[1] == '?':
            time_as_ls[1] = '3' if time_as_ls[0] == '2' else '9'

        # Third digit
        if time_as_ls[3] == '?':
            time_as_ls[3] = '5'

        # Final digit
        if time_as_ls[4] == '?':
            time_as_ls[4] = '9'

        return ''.join(time_as_ls)



print(Solution().maximumTime(input("Enter a time: ")))
