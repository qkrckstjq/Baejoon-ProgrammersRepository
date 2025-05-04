#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b;
    cin >> a >> b;

    long long sumA = 0, sumB = 0;

    for (char ch : a) sumA += (ch - '0');
    for (char ch : b) sumB += (ch - '0');

    cout << sumA * sumB << '\n';
	return 0;
}