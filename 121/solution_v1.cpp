class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minimum = INT_MAX;
        int profit = 0;
        int max_profit=0;
        for(int i = 0; i < prices.size(); i++)
        {
            minimum = min(minimum, prices[i]);
            profit = prices[i]-minimum;
            max_profit = max(profit, max_profit);
        }
        
        return max_profit;
    }
};