class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<int> x = {1};
        vector<vector<int>> result;
        result.push_back(x);
        for (int i = 2; i<=numRows; i++)
        {
            x = creating_array(i,x);
            result.push_back(x);
        }
        return result;
    }

    vector<int> creating_array(int i, vector<int> last)
    {
        vector<int> x;
        for(int k=0; k<i-1;k++)
        {
            if(x.empty()) 
            {
                x.push_back(1);
                continue;
            }
            int res = last[k-1] + last[k];
            x.push_back(res);
        }
        x.push_back(1);

        return x;
    }
};