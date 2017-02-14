#ifndef NORMAL_H
#define NORMAL_H
#include "account.h"

class NormalAccount : public Account
{
private:
	int rate;
public:
	NormalAccount::NormalAccount(int id, String name, int _money, int _rate)
		: Account(id, name, _money), rate(_rate) { }
	void NormalAccount::Deposit(int money)
	{
		Account::Deposit(money);
		Account::Deposit(money*(rate / 100));
	}
};

#endif // !NOMAL_H
