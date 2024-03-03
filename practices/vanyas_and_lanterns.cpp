#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
  int n, l, r, i;

  cin >> n >> l;

  int p[n];

  for (i = 0; i < n; i++)
  {
    cin >> p[i];
  }

  sort(p, p + n);

  r = max(p[0], l - p[n - 1]) * 2;

  for (i = 1; i < n; i++)
  {
    r = max(r, p[i] - p[i - 1]);
  }

  cout.precision(20);

  cout << fixed << r / 2.0 << endl;
  return 0;
}