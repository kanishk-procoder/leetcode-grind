class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        double ans;
        for(int i = 0; i< nums2.size(); i++){
            nums1.push_back(nums2[i]);
        }

        sort(nums1.begin(), nums1.end());
        int n = nums1.size();
        if(nums1.size()%2 == 0){
            n = n/2;
            ans = (double)(nums1[n]+nums1[n-1])/2;
        }
        else{
            ans = (nums1[n/2]);
        }

        return ans;
    }
};