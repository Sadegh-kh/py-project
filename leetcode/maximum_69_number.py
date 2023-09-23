class Solution:
    def maximum_69_number(self, num: int) -> int:
        # method 1
        # checked = 0
        # new_num = ""
        # for i in str(num):
        #     if i == "6" and checked == 0:
        #         new_num += "9"
        #         checked = 1
        #         continue
        #     new_num += i
        # return int(new_num)

        # method 2
        return int(str(num).replace("6", "9", 1))


s = Solution()
print(s.maximum_69_number(9669))
