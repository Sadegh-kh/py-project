from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # method 1
        # count = 0
        # g.sort(reverse=True)
        # for i in g:
        #     for j in s:
        #         if i <= j:
        #             count += 1
        #             s.remove(j)
        #             break

        # return count

        # method 2
        g.sort()
        s.sort()
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i


s = Solution()
print(s.findContentChildren([10, 9, 8, 7, 10, 9, 8, 7], [10, 9, 8, 7]))
