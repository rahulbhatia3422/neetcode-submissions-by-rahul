from typing import List
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        result = 0
        
        for word in words:
            word_count = Counter(word)
            can_form = True
            
            for ch, count in word_count.items():
                if chars_count[ch] < count:
                    can_form = False
                    break
            
            if can_form:
                result += len(word)
        
        return result