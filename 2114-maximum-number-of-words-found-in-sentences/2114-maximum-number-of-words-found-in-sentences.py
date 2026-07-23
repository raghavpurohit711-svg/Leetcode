class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0
        for i in sentences:
            count = max(count,i.count(" ") + 1)
        return count