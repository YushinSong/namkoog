#include <iostream>
using namespace std;

int main()
{
	int num;

	cout << "출력할 단 : ";
	cin >> num;

	for (int i = 0; i < 10; ++i)
	{
		cout << i << " x " << num << " = " << num*i << endl;
	}
}