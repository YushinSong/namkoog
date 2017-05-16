#include <iostream>
using namespace std;

void change(int &x, int &y)
{
	int &temp = &x;
	x = y;
	y = &temp;
}

int main()
{
	int x = 5, y = 10;
	change(x, y);
	cout << x << " " << y;
	return 0;
}