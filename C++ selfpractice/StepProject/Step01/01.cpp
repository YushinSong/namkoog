#include <iostream>
using namespace std;

typedef struct {
	int accID;
	char name[10];
	int money = NULL;
 }Account;

Account ID[100];

int PrintMenu();
void MakeAccount(int customer);
int Search(int acc);
void Deposit();
void Withdraw();
void PrintAll();


int main()
{
	int customer = 0;
	while(1)
	{ 
		switch (PrintMenu())
		{
		case 1:
			MakeAccount(customer);
			++customer;
			break;
		case 2:
			Deposit();
			break;
		case 3:
			Withdraw();
			break;
		case 4:
			PrintAll();
			break;
		case 5:
			return 0;
		}
	}
}

int PrintMenu()
{
	int num;

	cout << "--------Menu--------" << endl;
	cout << "1. ���°���" << endl;
	cout << "2. �� ��" << endl;
	cout << "3. �� ��" << endl;
	cout << "4. �������� ��ü ���" << endl;
	cout << "5. ���α׷� ����" << endl;
	cout << "���� : ";
	cin >> num;
	cout << endl << endl;

	return num;
}
int Search(int acc)
{
	for (int i = 0; ID[i].money != NULL; ++i)
	{
		if (acc == ID[i].accID)
			return i;
	}
}
void MakeAccount(int customer)
{
	cout << "[���°���]" << endl;
	cout << "����ID : ";
	cin >> ID[customer].accID;
	cout << "�̸� : ";
	cin >> ID[customer].name;
	cout << "�Աݾ� : ";
	cin >> ID[customer].money;
	cout << endl << endl;
}

void Deposit()
{
	int acc, money;

	cout << "[��   ��]" << endl;
	cout << "����ID : ";
	cin >> acc;
	cout << "�Աݾ� : ";
	cin >> money;
	cout << endl << endl;

	ID[Search(acc)].money += money;
}

void Withdraw()
{
	int acc, money;

	cout << "[��   ��]" << endl;
	cout << "����ID : ";
	cin >> acc;
	cout << "��ݾ� : ";
	cin >> money;
	cout << endl << endl;

	ID[Search(acc)].money -= money;
}

void PrintAll()
{
	for (int i = 0; ID[i].money != NULL; ++i)
	{
		cout << "����ID : " << ID[i].accID << endl;
		cout << "�� �� : " << ID[i].name << endl;
		cout << "�� �� : " << ID[i].money << endl;
		cout << endl << endl;
	}
}