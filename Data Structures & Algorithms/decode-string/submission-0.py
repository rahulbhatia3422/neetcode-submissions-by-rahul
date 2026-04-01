class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        string_stack = []
        current_string = ""
        current_num = 0

        for ch in s:
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)
            elif ch == "[":
                # Push current_string and current_num to stacks
                count_stack.append(current_num)
                string_stack.append(current_string)
                # Reset
                current_string = ""
                current_num = 0
            elif ch == "]":
                # Pop count and previous string
                count = count_stack.pop()
                prev_string = string_stack.pop()
                # Repeat current_string count times and append to prev_string
                current_string = prev_string + count * current_string
            else:  # letter
                current_string += ch

        return current_string
            