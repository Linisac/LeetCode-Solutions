class Solution {
public:
    int romanToInt(string s) {
        int len = s.length();
        int num = 0;
        for (int i = len - 1; i >= 0; i--) {
            switch(s[i]) {
                case 'I':
                num += ((i < len - 1 && (s[i + 1] == 'V' || s[i + 1] == 'X')) ? -1 : 1);
                break;
                case 'V':
                num += 5;
                break;
                case 'X':
                num += ((i < len - 1 && (s[i + 1] == 'L' || s[i + 1] == 'C')) ? -10 : 10);
                break;
                case 'L':
                num += 50;
                break;
                case 'C':
                num += ((i < len - 1 && (s[i + 1] == 'D' || s[i + 1] == 'M')) ? -100 : 100);
                break;
                case 'D':
                num += 500;
                break;
                case 'M':
                num += 1000;
                break;
                default:
                num = 0;
            }
        }
        return num;
    }
};