class Solution {
    public int findNumbers(int[] nums) {
        int Count = 0;
        for(int i=0;i<nums.length;i++){
            int digitCount = 0;
            int num = nums[i];
            while (num>0){
                num = num/10;
                digitCount++;
            }
            if (digitCount%2==0){
                Count++;
            }
        }
        return Count;  
    }
}