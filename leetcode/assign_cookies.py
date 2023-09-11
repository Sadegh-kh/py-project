from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort(reverse=True)
        for i in g:
            for j in s:
                if i <= j:
                    count += 1
                    s.remove(j)
                    break

        return count


s = Solution()
print(s.findContentChildren([10, 9, 8, 7, 10, 9, 8, 7], [10, 9, 8, 7]))
