class Solution {
public:
    int mySqrt(int x) {
        long long square_num=0;
        int num = 0;
        while(square_num<=x){
            num+=1;
            square_num = (long long)num * num;
        }

        return num-1;
    }
};