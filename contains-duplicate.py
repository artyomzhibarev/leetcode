# https://leetcode.com/problems/contains-duplicate/
from random import randint
from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if seen.get(num) is None:
                seen[num] = 1
            else:
                seen[num] += 1
                if seen[num] == 2:
                    return True
        return False


if __name__ == '__main__':
    nums = [[1, 1, 1, 3, 3, 4, 3, 2, 4, 2], [randint(0, 99) for _ in range(10)]]
    solution = Solution()
    for nums_list in nums:
        print(solution.contains_duplicate(nums=nums_list))
