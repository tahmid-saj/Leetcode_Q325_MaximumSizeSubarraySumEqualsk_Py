class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # put prefixSum[i]: i in hash map, keep the first seen value to ensure maximum length
        prefixSum, seen, res = [0 for _ in range(len(nums))], {0: -1}, 0
        for i in range(len(nums)): 
            prefixSum[i] = nums[i] + (prefixSum[i - 1] if i > 0 else 0)
            if prefixSum[i] not in seen: seen[prefixSum[i]] = i
        
        for i in range(len(prefixSum)):
            if (prefixSum[i] - k) in seen: res = max(res, i - seen[prefixSum[i] - k])
        return res
