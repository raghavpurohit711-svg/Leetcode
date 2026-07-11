class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = "".join(map(str,digits))
        digits = int(digits) + 1
        digits = [int(i) for i in str(digits)]
        return digits