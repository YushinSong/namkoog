#ifndef HANDLER_H
#define HANDLER_H
#include "account.h"

class AccountHandler
{
private:
	Account *accArr[100];
	int accNum;
public:
	AccountHandler();
	void PrintMenu();
	void MakeAccount();
	void MakeNormalAccount();
	void MakeCreditAccount();
	void Deposit();
	void Withdraw();
	void PrintAll();
	~AccountHandler();
};

#endif // !HANDLER_H
