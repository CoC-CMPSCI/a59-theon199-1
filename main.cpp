
#include <iostream>
using namespace std;

int main()
{
	int prev, current;
	bool first = true;

	cin >> current;
	while (first || current <= prev)
	{
		first = false;
		cout << current;
		prev = current;
		cin >> current;
		if (current <= prev)
		{
			cout << '\t';
		}
	}

	cout << endl;
}
