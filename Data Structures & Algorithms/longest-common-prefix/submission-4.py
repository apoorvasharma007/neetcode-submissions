class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        first_string = strs[0]
        curr_common_prefix = ""
        for i in range(len(first_string)):
            for string in strs:
                if i >= len(string):
                    return curr_common_prefix
                elif first_string[i] == string[i]:
                    continue
                else:
                    return curr_common_prefix
            curr_common_prefix += first_string[i]
        return curr_common_prefix