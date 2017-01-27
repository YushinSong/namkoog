#include <iostream>
#include <cstring>
#include "account.h"
using namespace std;

Account *accArr[100];
int accNum = 0;

Account::Account(int id, char *_name, int _money) : accID(id), money(_money)
{
	name = new char[strlen(_name) + 1];
	strcpy(name, _name);
}
Account::Account(const Account& copy) : accID(copy.accID), money(copy.money)
{
	name = new char[strlen(copy.name) + 1];
	strcpy(name, copy.name);
}
int Account::GetID() const
{
	return accID;
}
void Account::Deposit(int _money)
{
	money += _money;
}
int Account::Withdraw(int _money)
{
	if (money < _money)
		return 0;

	money -= _money;
	return money;
}
void Account::ShowAccInfo() const
{
	cout << "����id : " << accID << endl;
	cout << "��  �� : " << name << endl;
	cout << "��  �� : " << money << endl;
}
Account::~Account()
{
	delete[]name;
}



int PrintMenuMoney()
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
void MakeAccountMoney(int customer)
{
	int id, money;
	char name[20];

	cout << "[���°���]" << endl;
	cout << "����ID : ";
	cin >> id;
	cout << "�̸� : ";
	cin >> name;
	cout << "�Աݾ� : ";
	cin >> money;
	cout << endl << endl;

	accArr[accNum] = new Account(id, name, money);
	++accNum;
}

void DepositMoney()
{
	int id, money;

	cout << "[��   ��]" << endl;
	cout << "����ID : ";
	cin >> id;
	cout << "�Աݾ� : ";
	cin >> money;
	cout << endl << endl;

	for (int i = 0; i < accNum; ++i)
	{
		if (accArr[i]->GetID() == id)
		{
			accArr[i]->Deposit(money);
			cout << "�Ա� �Ϸ�" << endl << endl;
			return;
		}
	}
	cout << "��ȿ���� �ʴ� id�Դϴ�." << endl << endl;
}

void WithdrawMoney()
{
	int id, money;

	cout << "[��   ��]" << endl;
	cout << "����ID : ";
	cin >> id;
	cout << "��ݾ� : ";
	cin >> money;
	cout << endl << endl;

	for (int i = 0; i < accNum; ++i)
	{
		if (accArr[i]->GetID() == id)
		{
			if (accArr[i]->Withdraw(money) == 0)
			{
				cout << "�ܾ� ����" << endl;
				return;
			}
			cout << "��� �Ϸ�" << endl << endl;
			return;
		}
	}
	cout << "��ȿ���� �ʴ� id�Դϴ�." << endl << endl;
}

void PrintAllMoney()
{
	for (int i = 0; i < accNum; ++i)
	{
		accArr[i]->ShowAccInfo();
		cout << endl;
	}
}