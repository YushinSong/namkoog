#include <iostream>
using namespace std;

int main()
{
	int sell = 0;

	while (1)
	{
		cout << "�Ǹűݾ��� ���� ������ �Է�(-1 to end) : ";
		cin >> sell;

		if (sell == -1)
		{
			cout << "���α׷��� �����մϴ�." << endl;
			break;  
		}
		cout << "�̹� �� �޿� : " << 50 + (sell * 0.12) << endl << endl;
	}
}