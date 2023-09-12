class Solution:
    def minimumSum(self, num: int) -> int:
        # method 1
        # nums_list=list(str(num))
        # nums_list.sort()
        # num1=f"{nums_list[0]}{nums_list[2]}"
        # num2=f"{nums_list[1]}{nums_list[3]}"
        # return int(num1)+int(num2)

        # method 2
        a, b, c, d = sorted(str(num))
        return int(a + c) + int(b + d)


s = Solution()
lis = list("2932")
lis.sort()
print(lis)
num1 = f"{lis[0]}{lis[2]}"
num2 = f"{lis[1]}{lis[3]}"
print(int(num1) + int(num2))
