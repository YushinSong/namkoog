#include <iostream>
#include "account.h"
using namespace std;


int main()
{
	int customer = 0;
	while (1)
	{
		switch (PrintMenuMoney())
		{
		case 1:
			MakeAccountMoney(customer);
			++customer;
			break;
		case 2:
			DepositMoney();
			break;
		case 3:
			WithdrawMoney();
			break;
		case 4:
			PrintAllMoney();
			break;
		case 5:
			return 0;
		}
	}
}
