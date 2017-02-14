#ifndef HANDLER_H
#define HANDLER_H
#include "account.h"
#include "boundcheckarray.h"
#include "boundcheckarray.cpp"

class AccountHandler
{
private:
	BoundCheckArray<Account*> accArr;
	int accNum;
public:
	AccountHandler();
	void PrintMenu();
	void MakeAccount();
	void Deposit();
	void Withdraw();
	void PrintAll();
	~AccountHandler();
protected:
	void MakeNormalAccount();
	void MakeCreditAccount();
};

#endif // !HANDLER_H
