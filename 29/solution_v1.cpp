class Solution {
public:
    int divide(int dividend, int divisor) {

        if(dividend == INT_MIN && divisor == -1)
            return INT_MAX;

        long long dvd = dividend;
        long long dvs = divisor;

        int sign = ((dvd < 0) ^ (dvs < 0)) ? -1 : 1;

        dvd = abs(dvd);
        dvs = abs(dvs);

        long long ans = dvd / dvs;

        return sign * ans;
    }
};