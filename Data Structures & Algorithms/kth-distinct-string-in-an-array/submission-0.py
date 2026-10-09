class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        count = {}

        for element in arr:
            count[element] = count.get(element, 0) + 1

        for element in arr:
            if count[element] == 1:
                k -= 1
                if k == 0:
                    return element
        return ""
        