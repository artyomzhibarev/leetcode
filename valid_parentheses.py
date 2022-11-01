# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
                continue
            if not stack:
                return False
            popped_char = stack.pop()
            if popped_char == "(" and char != ")"\
                    or popped_char == "[" and char != "]"\
                    or popped_char == "{" and char != "}":
                return False
        return not stack


if __name__ == '__main__':
    print(Solution().is_valid("]"))
