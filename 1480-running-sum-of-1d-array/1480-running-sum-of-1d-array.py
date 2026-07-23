class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        for i  in range(len(nums)):
            runningSum.append(sum(nums[0:i+1]))

        return runningSum