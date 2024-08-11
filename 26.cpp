class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int leng = nums.size();
        int explore = 0, end = 0;
        while (explore < leng) {
            if (explore == leng - 1) {
                break;
            }
            else {
                //explore < leng - 1
                if (nums[explore] == nums[explore + 1]) {
                    explore++;
                }
                else {
                    //nums[explore] != nums[explore + 1]
                    explore++;
                    end++;
                    nums[end] = nums[explore];
                }
            }
        }
        return end + 1;
    }
};