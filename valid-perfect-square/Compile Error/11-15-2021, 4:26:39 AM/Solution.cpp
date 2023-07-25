// https://leetcode.com/problems/valid-perfect-square

class Solution {
public:
    bool isPerfectSquare(int num) { 
        if(num==0){return false;}
        if(num==1){return true;}
        for (int i=0;i<num/2+1;i++){
            long long sq = long long (i)* long long (i);
            if(sq==num){
                return true;
            }
        }
        return false;
    }
};