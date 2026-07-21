class Solution:
    def addDigits(self, num: int) -> int:
        while num//10 !=0:
            dig = [int(d) for d in str(num)]
            num = sum(dig)
        return num