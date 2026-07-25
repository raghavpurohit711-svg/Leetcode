class Solution:
    def reverse(self, x: int) -> int:
        
        x = str(x)
        if x[0] == '-':
            x = x.replace('-','')
            y = x[::-1]
            y=int(y)
            if y> 2**31-1 or y< -2**31:
                return 0
            else:
                return 0-y
        else :
            y = x[::-1]
            y=int(y)
            if y> 2**31-1 or y< -2**31:
                return 0
            else:
                return int(y)