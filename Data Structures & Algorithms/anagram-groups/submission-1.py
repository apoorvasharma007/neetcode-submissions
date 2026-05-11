class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_index_dict = {}
        for string in strs:
            character_count_array = [0] * 26
            for char in string:
                ascii = ord(char) - ord('a')
                character_count_array[ascii] += 1
            key = tuple(character_count_array)
            if key not in freq_index_dict:
                freq_index_dict[key] = [string]
            else:
                freq_index_dict[key].append(string)
        result = freq_index_dict.values()
        return list(result)