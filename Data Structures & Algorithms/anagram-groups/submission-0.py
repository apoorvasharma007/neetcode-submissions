class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_set = {}
        for string in strs:
            freq_index_arr = [0] * 26
            for char in string:
                lower_char = char.lower()
                ascii = ord(lower_char) - ord('a')
                freq_index_arr[ascii]+=1
            key = tuple(freq_index_arr)
            if key not in anagram_set:
                anagram_set[key] = []
            anagram_set[key].append(string)
        return list(anagram_set.values())