class Solution:
    def largestGoodInteger(self, num: str) -> str:

        max_num = ""
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:

                if num[i] > max_num:
                    max_num = num[i]
        
        return max_num * 3
        