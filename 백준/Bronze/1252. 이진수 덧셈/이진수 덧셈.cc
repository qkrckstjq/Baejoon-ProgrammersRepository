#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    string a, b;
    cin >> a >> b;

    string ans;
    int i = a.size() - 1, j = b.size() - 1, carry = 0;
    while (i >= 0 || j >= 0 || carry) {
        int av = (i >= 0 ? a[i] - '0' : 0);
        int bv = (j >= 0 ? b[j] - '0' : 0);
        int sum = av + bv + carry;
        carry = sum / 2;
        ans.push_back(char('0' + (sum % 2)));
        i--;  
        j--;
    }

    reverse(ans.begin(), ans.end());

    size_t pos = ans.find_first_not_of('0');
    if (pos != string::npos) {
        cout << ans.substr(pos);
    } else {
        cout << "0";
    }

    return 0;
}
