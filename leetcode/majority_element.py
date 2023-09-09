from collections import defaultdict
from typing import List


class Soloution:
    def majority_element(self, nums: List[int]) -> int:
        # Method 1
        count_hash = defaultdict(int)
        for i in nums:
            count_hash[i] += 1
        length_nums_half = len(nums) // 2
        for key, value in count_hash.items():
            if value >= length_nums_half:
                return key

        return 0

        # Method 2

        # nums.sort()
        # n = len(nums)
        # return nums[n // 2]


s = Soloution()
lsit = [2, 3, 2, 3, 4, 3, 4]
print(s.majority_element(lsit))
