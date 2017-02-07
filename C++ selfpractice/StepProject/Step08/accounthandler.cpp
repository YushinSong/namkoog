#include "accounthandler.h"
#include "highcreditaccount.h"
#include <iostream>
using namespace std;


AccountHandler::AccountHandler() : accNum(0) { }

void AccountHandler::PrintMenu()
{
	cout << "--------Menu--------" << endl;
	cout << "1. 계좌개설" << endl;
	cout << "2. 입 금" << endl;
	cout << "3. 출 금" << endl;
	cout << "4. 계좌정보 전체 출력" << endl;
	cout << "5. 프로그램 종료" << endl;
}
void AccountHandler::MakeAccount()
{
	int sel;

	cout << "[계좌종류 선택]" << endl;
	cout << "1. 보통예금계좌 " << "2. 신용예금계좌" << endl;
	cout << "선택 : ";
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

	cout << "[계좌개설]" << endl;
	cout << "계좌ID : ";
	cin >> id;
	cout << "이름 : ";
	cin >> name;
	cout << "입금액 : ";
	cin >> money;
	cout << "이자율 : ";
	cin >> rate;
	cout << endl << endl;

	accArr[accNum++] = new NormalAccount(id, name, money, rate);
}
void AccountHandler::MakeCreditAccount()
{
	int id, money, rate, level;
	char name[20];

	cout << "[계좌개설]" << endl;
	cout << "계좌ID : ";
	cin >> id;
	cout << "이름 : ";
	cin >> name;
	cout << "입금액 : ";
	cin >> money;
	cout << "이자율 : ";
	cin >> rate;
	cout << "신용등급 (1toA  2toB  3toC) : ";
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

void AccountHandler::Withdraw()
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