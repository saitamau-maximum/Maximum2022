#include <bits/stdc++.h>
using namespace std;

int main() {
  // 入力
  int a, b;
  cin >> a >> b;

  // 出力
  if (a + b >= 15 && b >= 8) {
    cout << 1 << endl;
  }
  else if (a + b >= 10 && b >= 3) {
    cout << 2 << endl;
  }
  else if (a + b >= 3) {
    cout << 3 << endl;
  }
  else {
    cout << 4 << endl;
  }
}