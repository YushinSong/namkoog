#include <iostream>
#include "account.h"
using namespace std;


enum { MAKE = 1, DEPOSIT, WITHDRAW, INQUIRE, EXIT };
int main()
{
	AccountHandler manager;
	int choice;

	while(1)
	{
		manager.PrintMenu();
		cout << "¼±ÅÃ : ";
		cin >> choice;
		cout << endl;

		switch (choice)
		{
		case MAKE:
			manager.MakeAccount();
			break;
		case DEPOSIT:
			manager.Deposit();
			break;
		case WITHDRAW:
			manager.Withdraw();
			break;
		case INQUIRE:
			manager.PrintAll();
			break;
		case EXIT:
			return 0;
		}
	}
}
