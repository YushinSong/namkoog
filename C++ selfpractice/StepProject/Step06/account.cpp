#include <iostream>
#include <cstring>
#include "account.h"
using namespace std;


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





NormalAccount::NormalAccount(int id, char *name, int _money, int _rate)
	: Account(id, name, _money), rate(_rate) { }
void NormalAccount::Deposit(int money)
{
	Account::Deposit(money);
	Account::Deposit(money*(rate / 100));
}



HighCreditAccount::HighCreditAccount(int id, char *name, int _money, int _rate, int _level)
	: NormalAccount(id, name, _money, _rate), level(_level) { }
void HighCreditAccount::Deposit(int money)
{
	NormalAccount::Deposit(money);
	Account::Deposit(money*(level / 100));
}







AccountHandler::AccountHandler() : accNum(0) { }

void AccountHandler::PrintMenu()
{
	cout << "--------Menu--------" << endl;
	cout << "1. ���°���" << endl;
	cout << "2. �� ��" << endl;
	cout << "3. �� ��" << endl;
	cout << "4. �������� ��ü ���" << endl;
	cout << "5. ���α׷� ����" << endl;
}
void AccountHandler::MakeAccount()
{
	int sel;

	cout << "[�������� ����]" << endl;
	cout << "1. ���뿹�ݰ��� " << "2. �ſ뿹�ݰ���" << endl;
	cout << "���� : ";
	cin >> sel;

	if (sel == 1)
		MakeNormalAccount();
	else
		MakeCreditAccount();
}

void AccountHandler::MakeNormalAccount()
{
	int id, money, rate;
	char name[20];

	cout << "[���°���]" << endl;
	cout << "����ID : ";
	cin >> id;
	cout << "�̸� : ";
	cin >> name;
	cout << "�Աݾ� : ";
	cin >> money;
	cout << "������ : ";
	cin >> rate;
	cout << endl << endl;

	accArr[accNum++] = new NormalAccount(id, name, money, rate);
}
void AccountHandler::MakeCreditAccount()
{
	int id, money, rate, level;
	char name[20];

	cout << "[���°���]" << endl;
	cout << "����ID : ";
	cin >> id;
	cout << "�̸� : ";
	cin >> name;
	cout << "�Աݾ� : ";
	cin >> money;
	cout << "������ : ";
	cin >> rate;
	cout << "�ſ��� (1toA  2toB  3toC) : ";
	cin >> level;
	cout << endl << endl;

	switch (level)
	{
	case LEVEL_A:
		accArr[accNum++] = new HighCreditAccount(id, name, money, rate, LEVEL_A);
	case LEVEL_B:
		accArr[accNum++] = new HighCreditAccount(id, name, money, rate, LEVEL_B);
	case LEVEL_C:
		accArr[accNum++] = new HighCreditAccount(id, name, money, rate, LEVEL_C);
	}
}



void AccountHandler::Deposit()
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

void AccountHandler::Withdraw()
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

void AccountHandler::PrintAll()
{
	for (int i = 0; i < accNum; ++i)
	{
		accArr[i]->ShowAccInfo();
		cout << endl;
	}
}

AccountHandler::~AccountHandler()
{
	for (int i = 0; i > accNum; ++i)
		delete accArr[i];
}