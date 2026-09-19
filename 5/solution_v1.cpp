class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty()) return "";
        
        int start = 0, max_len = 0;
        
        for (int i = 0; i < s.length(); i++) {
            int l = i, r = i;
            while (l >= 0 && r < s.length() && s[l] == s[r]) {
                if (r - l + 1 > max_len) {
                    start = l;
                    max_len = r - l + 1;
                }
                l--;
                r++;
            }

            l = i, r = i + 1;
            while (l >= 0 && r < s.length() && s[l] == s[r]) {
                if (r - l + 1 > max_len) {
                    start = l;
                    max_len = r - l + 1;
                }
                l--;
                r++;
            }
        }
        
        return s.substr(start, max_len);
    }
};