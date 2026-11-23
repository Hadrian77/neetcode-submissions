class Solution {
    public boolean hasDuplicate(int[] nums) {

        HashSet<Integer> cache = new HashSet<Integer>();

        boolean result = true;

        for(int num: nums){

            result = cache.add(num);

            if (result == false){
                return true;
            }



        }

        return false;
        
    }
}