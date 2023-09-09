from collections import defaultdict
from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        # Method 1 time: O(n) space: O(n)
        # hash_nums = defaultdict(int)

        # for i in nums:
        #     hash_nums[i] += 1
        #     if hash_nums[i] == 2:
        #         return True

        # Method 2 time:O(nlogn) space: O(1)
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                return True
            i += 1
        return False


s = Solution()

a = tuple()
