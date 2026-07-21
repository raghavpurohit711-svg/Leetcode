class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        digits_sum = sum(digits)
        product = 1
        for x in digits: 
            product *= x
        ans = product - digits_sum
        return ans