class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        else if (x == 0) {
            return true;
        }
        else {
            int a[10];
            int length = 0;
            while (x > 0) {
                a[length] = x % 10;
                x /= 10;
                length++;
            }
            for (int i = 0; i < length / 2; i++) {
                if (a[i] != a[length - 1 - i]) {
                    return false;
                }
            }
            return true;
        }
    }
};