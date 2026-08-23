class Solution:
    def checkDivisibility(self, n: int) -> bool:
        if n ==0 :
            return False
        og_n = n
        digits = []
        while n>0:
            digits.append(n%10)
            n//=10
        digits = digits[::-1]
        sum1 = sum(digits)
        fact = 1
        for i in digits:
            fact*=i
        div = sum1 + fact
        if div ==0:
            return False
        return og_n%div==0