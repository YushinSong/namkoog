#include <iostream>
using namespace std;

void Increase(int &num)
{
	cout << num + 1 << endl;
}
void Change(int &num)
{
	cout << num * -1 << endl;
}
int main()
{
	int num;

	cout << "���� �Է� : ";
	cin >> num;

	Increase(num);
	Change(num);
}