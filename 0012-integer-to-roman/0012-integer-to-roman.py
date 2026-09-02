class Solution:
    def intToRoman(self, num: int) -> str:
        value=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        ans=''
        i =0 
        while i<len(value):
            count = num // value[i]
            if count > 0:
                ans+=symbols[i]*count
                num-=value[i]*count
            i+=1
        return ans