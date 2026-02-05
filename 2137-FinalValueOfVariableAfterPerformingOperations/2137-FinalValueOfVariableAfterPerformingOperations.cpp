// Last updated: 2/5/2026, 7:40:32 AM
class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int result = 0 ; 
        for ( string opr : operations) result+=(opr[1] == '+' ? 1 : -1);
        return result;
    }
};