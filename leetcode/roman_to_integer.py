class Solution:
    def roman_to_int(self, s: str) -> int:
        roman_table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        num = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for i in s:
            num += roman_table[i]
        return num


obj = Solution()
print(obj.roman_to_int("III"))
