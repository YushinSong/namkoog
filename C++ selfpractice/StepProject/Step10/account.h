#ifndef ACCOUNT_H
#define ACCOUNT_H

#include "string.h"

class Account
{
private:
	int accID;
	String name;
	int money;
public:
	Account(int id, String _name, int _money);

	int GetID() const;
	virtual void Deposit(int _money);
	int Withdraw(int _money);
	void ShowAccInfo() const;
};



#endif // !ACCOUNT_H
