class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0] *(2*n)
        left = 0
        right = n
        for i in range(0,n*2,2):
            ans[i] = nums[left]
            ans[i+1] = nums[right]
            left +=1
            right+=1
        return ans