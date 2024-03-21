class Solution {
public:
    string intToRoman(int num) {
        string roman = "";
        map<int, string> roman_letters({
            {1000, "M"},
            {900, "CM"},
            {500, "D"},
            {400, "CD"},
            {100, "C"},
            {90, "XC"},
            {50, "L"},
            {40, "XL"},
            {10, "X"},
            {9, "IX"},
            {5, "V"},
            {4, "IV"},
            {1, "I"},
        });
        map<int, string>::reverse_iterator it;
        int index;
        it = roman_letters.rbegin();
        while (num != 0 && it != roman_letters.rend()){
            if (num == 1){
                roman.append("I");
                break;
            }
            for (index = num / it->first; index > 0; --index){
                roman.append(it->second);
            }
            num -= (num / it->first) * (it->first);
            ++it;
            
        }
        return roman;
    }
};
