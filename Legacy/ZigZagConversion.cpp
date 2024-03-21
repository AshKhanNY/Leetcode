class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) return s;
        
        vector<string> zigzags(numRows, "");
        string new_str = "";
        int counter = 0;
        int adder = -1;
        for (int i = 0; i < s.length(); ++i){
            zigzags[counter] += s[i];
            if (counter == 0 || counter == numRows - 1) 
                adder *= -1; 
            counter += adder;
        }
        for (int i = 0; i < zigzags.size(); ++i){
            // printf("String #%d in vector: %s\n", i, zigzags[i].c_str());
            // fflush(stdout);
            new_str.append(zigzags[i]);
        }
        return new_str;
    }
};
