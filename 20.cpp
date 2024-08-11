class Solution {
public:
    bool isValid(string s) {
        int leng = s.length();
        vector<char> stack;
        int position = 0;
        while (position < leng) {
            switch(s[position]) {
                case '(':
                stack.push_back('(');
                break;
                case ')':
                if (stack.empty() == true || stack.back() != '(') {
                    return false;
                }
                else {
                    stack.pop_back();
                }
                break;
                case '{':
                stack.push_back('{');
                break;
                case '}':
                if (stack.empty() == true || stack.back() != '{') {
                    return false;
                }
                else {
                    stack.pop_back();
                }
                break;
                case '[':
                stack.push_back('[');
                break;
                case ']':
                if (stack.empty() == true || stack.back() != '[') {
                    return false;
                }
                else {
                    stack.pop_back();
                }
                break;
                default:
                return false;
            }
            position++;
        }
        if (stack.empty() == true) {
            return true;
        }
        else {
            return false;
        }
    }
};