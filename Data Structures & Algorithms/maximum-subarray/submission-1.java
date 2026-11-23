class Solution {
    public int maxSubArray(int[] nums) {

        int result = nums[0];

        for (int i=0; i < nums.length ;i++){
            int sum = nums[i];
            result = Math.max(result,sum);

            for (int j= i + 1; j < nums.length;j++){
                sum += nums[j];
                result = Math.max(result,sum);

            }
        }

        return result;
        
    }
}
