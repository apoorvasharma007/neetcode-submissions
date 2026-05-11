class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1

        freq_of_n_elements = [[] for i in range(len(nums)+1)]
        for n, freq in freq_map.items():
            freq_of_n_elements[freq].append(n)

        ans_list = []
        for i in range(len(freq_of_n_elements) -1, 0, -1):
            for number in freq_of_n_elements[i]:
                ans_list.append(number)
                if len(ans_list) == k:
                    return ans_list
        