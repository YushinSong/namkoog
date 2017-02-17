#ifndef HIGH_H
#define HIGH_H
#include "normalaccount.h"
#include "string.h"


class HighCreditAccount : public NormalAccount
{
private:
	int level;
public:
	HighCreditAccount(int id, String name, int _money, int _rate, int _level)
		: NormalAccount(id, name, _money, _rate), level(_level) { }
	virtual void Deposit(int money)
	{
		if (money < 0)
			throw MinusException(money);

		NormalAccount::Deposit(money);
		Account::Deposit(money*(level / 100));
	}
};


#endif // !HIGH_H
