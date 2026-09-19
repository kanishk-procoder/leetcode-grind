class Solution {
public:
    int majorityElement(vector<int>& nums) {
        for (int val : nums) {
            int count = 0;
            for (int el : nums) {
                if (val == el) {
                    count++;
                }
            }

            if (count > (nums.size() / 2)) {
                return val;
            }
        }
        return -1;
    }
};