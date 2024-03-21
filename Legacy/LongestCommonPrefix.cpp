class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        // Find the longest common prefix string amongst an array of string
        int i, j;
        // With respect to first str, we initialize its place values with 1 to
        // show that we are going to find prefixes relative to the first str
        vector<int> p(strs[0].length(), 1);
        for (i = 1; i < strs.size(); ++i){
            for (j = 0; j < strs[0].length(); ++j){
                if (strs[i][j] == strs[0][j]) p[j]++;
            }
        }
        j = 0;
        for (i = 0; i < p.size(); ++i){
            cout << p[i] << endl;
            if (p[i] == strs.size()) ++j;
            else break;
        }
        return strs[0].substr(0,j);
    }
};
