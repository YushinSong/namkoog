#ifndef ACCOUNT_H
#define ACCOUNT_H

class Account
{
private:
	int accID;
	char *name;
	int money;
public:
	Account(int id, char *_name, int _money);
	Account(const Account& copy);
	int GetID() const;
	void Deposit(int _money);
	int Withdraw(int _money);
	void ShowAccInfo() const;
	~Account();
};

class AccountHandler
{
private:
	Account *accArr[100];
	int accNum;
public:
	AccountHandler();
	void PrintMenu();
	void MakeAccount();
	void Deposit();
	void Withdraw();
	void PrintAll();
	~AccountHandler();
};

#endif // !ACCOUNT_H
