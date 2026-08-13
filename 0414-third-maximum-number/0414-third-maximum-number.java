import java.util.Arrays;
class Solution {
    public int thirdMax(int[] nums) {
        Arrays.sort(nums);
        int i = 0;
        for (int j=1;j<nums.length;j++){
            if (nums[j]!=nums[i]){
                i++;
                nums[i]=nums[j];
            }

        }
        int count = i+1;

        if (count < 3){
            return nums[count-1];
    }
    return nums[count-3];
    }
}