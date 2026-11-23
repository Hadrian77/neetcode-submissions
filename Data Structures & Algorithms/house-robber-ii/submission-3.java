class Solution {
    public int rob(int[] nums) {

        if (nums.length <= 1){
            return nums[0];
        }

        int[] memo = new int[nums.length];
        Arrays.fill(memo,-1);
        int[] memo2 = memo.clone();

        int[] front = Arrays.copyOfRange(nums,0,nums.length -1);
        int[] end = Arrays.copyOfRange(nums,1,nums.length);

        return Math.max(best(end,0,memo),best(front,0,memo2));
        
    }

    public int best(int[] nums, int i, int[] memo){


        if (i >= nums.length){
            return 0;
        }

        if (memo[i] != -1){

            return memo[i];

        }

        int skip = best(nums,i+1,memo);
        int rob = best(nums,i+2,memo) + nums[i];

        memo[i] = Math.max(skip,rob);

        return memo[i];


    }
}
