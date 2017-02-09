#include <iostream>
#include <cstring>
#include "account.h"
using namespace std;


Account::Account(int id, char *_name, int _money) : accID(id), money(_money)
{
	name = new char[strlen(_name) + 1];
	strcpy(name, _name);
}
Account::Account(const Account& copy) : accID(copy.accID), money(copy.money)
{
	name = new char[strlen(copy.name) + 1];
	strcpy(name, copy.name);
}
Account& Account::operator=(const Account& ref)
{
	accID = ref.accID;
	money = ref.money;

	delete[]name;
	name = new char[strlen(ref.name) + 1];
	strcpy(name, ref.name);
	return *this;
}
int Account::GetID() const
{
	return accID;
}
void Account::Deposit(int _money)
{
	money += _money;
}
int Account::Withdraw(int _money)
{
	if (money < _money)
		return 0;

	money -= _money;
	return money;
}
void Account::ShowAccInfo() const
{
	cout << "°èÁÂid : " << accID << endl;
	cout << "ÀÌ  ¸§ : " << name << endl;
	cout << "ÀÜ  ¾× : " << money << endl;
}
Account::~Account()
{
	delete[]name;
}

