class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        for char in s:
            if char.isalnum():
                string.append(char.lower())
        

        for i in range(len(string)):
            if string[i].lower() != string[len(string)-1- i].lower():
                return False
        return True