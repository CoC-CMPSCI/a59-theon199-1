
#include <iostream>
using namespace std;

int main()
{
	int prev, current;
	// TODO
	int flag = 1;

	cin >> current;
	while ((flag == 1) or (prev > current))
	{
		flag = 0;
		cout << current << "\t";
		prev = current;
		cin >> current;
	}
	// TODO
}
