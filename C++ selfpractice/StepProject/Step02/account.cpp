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
int Account::GetID()
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
void Account::ShowAccInfo()
{
	cout << "계좌id : " << accID << endl;
	cout << "이  름 : " << name << endl;
	cout << "잔  액 : " << money << endl;
}
Account::~Account()
{
	delete[]name;
}



int PrintMenuMoney()
{
	int num;

	cout << "--------Menu--------" << endl;
	cout << "1. 계좌개설" << endl;
	cout << "2. 입 금" << endl;
	cout << "3. 출 금" << endl;
	cout << "4. 계좌정보 전체 출력" << endl;
	cout << "5. 프로그램 종료" << endl;
	cout << "선택 : ";
	cin >> num;
	cout << endl << endl;

	return num;
}
void MakeAccountMoney(int customer)
{
	int id, money;
	char name[20];

	cout << "[계좌개설]" << endl;
	cout << "계좌ID : ";
	cin >> id;
	cout << "이름 : ";
	cin >> name;
	cout << "입금액 : ";
	cin >> money;
	cout << endl << endl;

	accArr[accNum] = new Account(id, name, money);
	++accNum;
}

void DepositMoney()
{
	int id, money;

	cout << "[입   금]" << endl;
	cout << "계좌ID : ";
	cin >> id;
	cout << "입금액 : ";
	cin >> money;
	cout << endl << endl;
	
	for (int i = 0; i < accNum; ++i)
	{
		if (accArr[i]->GetID() == id)
		{
			accArr[i]->Deposit(money);
			cout << "입금 완료" << endl << endl;
			return;
		}
	}
	cout << "유효하지 않는 id입니다." << endl << endl;
}

void WithdrawMoney()
{
	int id, money;

	cout << "[출   금]" << endl;
	cout << "계좌ID : ";
	cin >> id;
	cout << "출금액 : ";
	cin >> money;
	cout << endl << endl;

	for (int i = 0; i < accNum; ++i)
	{
		if (accArr[i]->GetID() == id)
		{
			if (accArr[i]->Withdraw(money) == 0)
			{
				cout << "잔액 부족" << endl;
				return;
			}
			cout << "출금 완료" << endl << endl;
			return;
		}
	}
	cout << "유효하지 않는 id입니다." << endl << endl;
}

void PrintAllMoney()
{
	for (int i = 0; i < accNum; ++i)
	{
		accArr[i]->ShowAccInfo();
		cout << endl;
	}
}