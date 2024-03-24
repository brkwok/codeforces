#include <bits/stdc++.h>

using namespace std;

int main()
{
  ios::sync_with_stdio(0);

  int N;
  cin >> N;
  string prev;

  int count = 0;

  while (N--)
  {
    string temp;
    cin >> temp;
    
    if (temp != prev)
    {
      count++;
      prev = temp;
    }
  }

  cout << count << endl;
}