#include <bits/stdc++.h>

using namespace std;

int main()
{
  int t, n;
  cin >> t;
  while (t--)
  {
    cin >> n;
    set<int> s;

    for (int i = 0; i < n; i++)
    {
      int x;
      cin >> x;

      s.insert(x);
    }

    if (s.size() == n)
    {
      cout << "YES" << endl;
    }
    else
    {
      cout << "NO" << endl;
    }
  }
}