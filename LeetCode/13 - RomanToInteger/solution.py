class Solution:
    def __init__(self):
        self.letters = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    def romanToInt(self, s: str) -> int:
        convert = []
        for i in range(len(s)):
            convert.append(self.letters[s[i]])
        sum = convert[0]
        for i in range(1, len(convert)):
            if convert[i - 1] < convert[i]:
                sum += convert[i] - 2*(convert[i - 1])
            else:
                sum += convert[i]
        return sum 


# run individually 
# u = Solution()
# print(u.romanToInt("MCMXCIV"))