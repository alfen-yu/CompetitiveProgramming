# class Solution:
#     def makeGood(self, s: str) -> str:
#         check = len(s) - 2
#         while (len(s) != check):
#             for i in range(0, len(s) - 1):
#                 j = ord(s[i])
#                 j1 = ord(s[i + 1])
#                 if (j == j1 - 32) or (j - 32 == j1):
#                     s.replace(s[i], '')
#                     s.replace(s[i], '')
#             check = len(s) - 2
                

# s = "leEeetcode"
# u = Solution()
# u = u.makeGood(s)
# print(u)

# a = 'E'
# b = 'e'
# c = ord(a)
# d = ord(b) - 32

# if c == d:
#     print("YES")

class Solution:
    self.check = 0
    def makeGood(self, s: str) -> str:
        if self.check == len(s):
            return s
        else:
            for i in range(0, len(s) - 1):
                j = ord(s[i])
                j1 = ord(s[i + 1])
                if (j == j1 - 32) or (j - 32 == j1):
                    s.replace(s[i], '')
                    s.replace(s[i], '')
                    break
            check = len(s)
            return self.makeGood(s)
        

s = "leEeetcode"
u = Solution()
u = u.makeGood(s)
print(u)