from typing import List


class Solution:
    def letter_combinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hash_phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        list_result = [""]
        for digit in digits:
            new_list = []
            for result in list_result:
                for letter in hash_phone[digit]:
                    new_list.append(result + letter)
            list_result = new_list

        return list_result


obj = Solution()
print(obj.letter_combinations("244"))
