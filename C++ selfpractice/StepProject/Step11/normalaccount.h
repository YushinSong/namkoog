#ifndef NORMAL_H
#define NORMAL_H
#include "account.h"
#include "string.h"
#include "accountexception.h"

class NormalAccount : public Account
{
private:
	int rate;
public:
	NormalAccount::NormalAccount(int id, String name, int _money, int _rate)
		: Account(id, name, _money), rate(_rate) { }
	virtual void Deposit(int money)
	{
		if (money < 0)
			throw MinusException(money);

		Account::Deposit(money);
		Account::Deposit(money*(rate / 100));
	}
};

#endif // !NOMAL_H
