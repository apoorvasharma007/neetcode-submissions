# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         contents = {}
#         if len(s) != len(t):
#             return False
#         for i in range(len(s)):
#             contents[s[i]] = contents.get(s[i], 0) + 1
#             contents[t[i]] = contents.get(t[i], 0) - 1
#         for char, net_count in contents.items():
#             if net_count != 0:
#                 return False
#         return True
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT