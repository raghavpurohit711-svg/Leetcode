class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] ans= new int [2*n];
        int left = 0;
        int right = n;
        for (int i=0;i<n*2;i+=2){
            ans[i] = nums[left];
            ans[i+1] = nums[right];
            left++;
            right++;
        }
        return ans;
    }
}