# Last updated: 2/5/2026, 7:39:57 AM
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i,word in enumerate(words) if x in word]