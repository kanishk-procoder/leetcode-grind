class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> answer;
        vector<int> sol;

        func(nums,0,sol,answer);
        return answer;

    }

    void func(vector<int>& nums, int start, vector<int>& sol, vector<vector<int>>& answer) {
        answer.push_back(sol);
        for (int i = start; i < nums.size(); i++) {
            sol.push_back(nums[i]);
            func(nums, i + 1, sol, answer);
            sol.pop_back();
        }
    }
};