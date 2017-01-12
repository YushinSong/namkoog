#include <iostream>
using namespace std;

int main()
{
	int num[5], sum = 0;

	for (int i = 0; i < 5; ++i)
	{
		cout << i + 1 <<"번째 정수 입력 : ";
		cin >> num[i];
		sum += num[i];
	}
	cout << "합계 : " << sum << endl;
}