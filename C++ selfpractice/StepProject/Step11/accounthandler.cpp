#include "BankingCommonDecl.h"
#include "accounthandler.h"
#include "highcreditaccount.h"
#include "string.h"
#include <iostream>
using namespace std;


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
	String name;

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
	String name;

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

	while (true)
	{
		cout << "[��   ��]" << endl;
		cout << "����ID : ";
		cin >> id;
		cout << "�Աݾ� : ";
		cin >> money;
		cout << endl << endl;

		try
		{
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
			return;
		}
		catch (MinusException& expt)
		{
			expt.ShowExceptionInfo();
			cout << "�Աݾ׸� ���Է��ϼ���." << endl;
		}
	}
}

void AccountHandler::Withdraw()
{
	int id, money;

	while (true)
	{
		cout << "[��   ��]" << endl;
		cout << "����ID : ";
		cin >> id;
		cout << "��ݾ� : ";
		cin >> money;
		cout << endl << endl;

		try {
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
			return;
		}
		catch (MinusException& expt)
		{
			expt.ShowExceptionInfo();
			cout << "�Աݾ׸� ���Է��ϼ���." << endl;
		}
	}
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