# https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        res = ''
        if not strs:
            return res

        elif len(strs) == 1:
            return strs[0]
        else:
            shortest_str = strs[0]
            for i in range(1, len(strs)):
                if len(strs[i]) < len(shortest_str):
                    shortest_str = strs[i]

            for j in range(len(shortest_str)):
                for str_ in strs:
                    if str_[j] != shortest_str[j]:
                        return res
                res += shortest_str[j]
        return res


if __name__ == '__main__':
    print(Solution().longest_common_prefix(["cir", "car"]))
