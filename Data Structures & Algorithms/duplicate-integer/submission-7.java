class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> seenThisNumber = new HashSet<Integer>();
        for (int i = 0; i < nums.length; i++){
            if (seenThisNumber.contains(nums[i])){
                return true;
            }
            else{
                seenThisNumber.add(nums[i]);
            }
        }
        return false;
    }
}