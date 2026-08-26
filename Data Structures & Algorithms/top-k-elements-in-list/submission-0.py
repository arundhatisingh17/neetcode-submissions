class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = {}
        heap = []

        final_list = []

        for i in range(len(nums)):
            freq_map[nums[i]] = freq_map.get(nums[i], 0) + 1

        for key, val in freq_map.items():
            heapq.heappush(heap, (-val, key))

        for i in range(k):
            freq, num = heapq.heappop(heap)
            final_list.append(num)

        return final_list