class Solution:
    def compress(self, chars: list[str]) -> int:
        # Helper to compress repeats
        def stitchList(index, amount):
            number = list(str(amount))
            chars[:] = chars[:index - amount + 1] + list(str(amount)) + chars[i:]
            return amount - (1 + len(number))
        # Iterating helper variables
        i = 0
        last_char = ''
        repeats = 0
        # While loop for dynamic sizing
        while i < len(chars):
            if chars[i] != last_char:
                if repeats > 1:
                    i -= stitchList(i, repeats)
                repeats = 1
                last_char = chars[i]
            else:
                repeats += 1
            i += 1
        # Stitch last occurence if necessary
        if repeats > 1: stitchList(i, repeats)
        
        return len(chars)

# Should become ["a","2","b","2","c","3"]
chars = ["a","a","b","b","c","c","c"]
print("First example: ", Solution().compress(chars))
print(chars)

# Should become ["a","b","1","2"]
chars2 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"] 
print("Second example: ", Solution().compress(chars2))
print(chars2)

