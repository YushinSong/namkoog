#ifndef HANDLER_H
#define HANDLER_H
#include "account.h"
#include "accountarray.h"

class AccountHandler
{
private:
	BoundCheckAccountPtrArray accArr;
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
