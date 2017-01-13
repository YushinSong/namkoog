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
	cout << "[계좌개설]" << endl;
	cout << "계좌ID : ";
	cin >> ID[customer].accID;
	cout << "이름 : ";
	cin >> ID[customer].name;
	cout << "입금액 : ";
	cin >> ID[customer].money;
	cout << endl << endl;
}

void Deposit()
{
	int acc, money;

	cout << "[입   금]" << endl;
	cout << "계좌ID : ";
	cin >> acc;
	cout << "입금액 : ";
	cin >> money;
	cout << endl << endl;

	ID[Search(acc)].money += money;
}

void Withdraw()
{
	int acc, money;

	cout << "[출   금]" << endl;
	cout << "계좌ID : ";
	cin >> acc;
	cout << "출금액 : ";
	cin >> money;
	cout << endl << endl;

	ID[Search(acc)].money -= money;
}

void PrintAll()
{
	for (int i = 0; ID[i].money != NULL; ++i)
	{
		cout << "계좌ID : " << ID[i].accID << endl;
		cout << "이 름 : " << ID[i].name << endl;
		cout << "잔 액 : " << ID[i].money << endl;
		cout << endl << endl;
	}
}