class Solution:
    def balanced_string_split(self, s: str) -> int:
        count_balanced = 0
        r_count = 0
        for i in s:
            if i == "R":
                r_count += 1
            elif i == "L":
                r_count -= 1
            if r_count == 0:
                count_balanced += 1

        return count_balanced
