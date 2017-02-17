#include <iostream>
#include <cstring>
#include "BankingCommonDecl.h"
#include "accountexception.h"
#include "account.h"
using namespace std;


Account::Account(int id, String _name, int _money) : accID(id), money(_money)
{
	name = _name;
}
int Account::GetID() const
{
	return accID;
}
void Account::Deposit(int _money)
{
	if (_money < 0)
		throw MinusException(_money);

	money += _money;
}
int Account::Withdraw(int _money)
{
	if (_money < 0)
		throw MinusException(_money);
	if (money < _money)
		throw InsuffException(money, _money);

	money -= _money;
	return money;
}
void Account::ShowAccInfo() const
{
	cout << "°èÁÂid : " << accID << endl;
	cout << "ÀÌ  ¸§ : " << name << endl;
	cout << "ÀÜ  ¾× : " << money << endl;
}