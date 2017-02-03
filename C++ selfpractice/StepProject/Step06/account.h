#ifndef ACCOUNT_H
#define ACCOUNT_H


enum { MAKE = 1, DEPOSIT, WITHDRAW, INQUIRE, EXIT };
enum { LEVEL_A = 7, LEVEL_B = 4, LEVEL_C = 2 };
enum { NORMAL = 1, CREDIT = 2 };

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
	virtual void Deposit(int _money);
	int Withdraw(int _money);
	void ShowAccInfo() const;
	~Account();
};

class NormalAccount : public Account
{
private:
	int rate;
public:
	NormalAccount(int id, char *name, int _money, int _rate);
	virtual void Deposit(int money);
};

class HighCreditAccount : public NormalAccount
{
private:
	int level;
public:
	HighCreditAccount(int id, char *name, int _money, int _rate, int _level);
	virtual void Deposit(int money);
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
	void MakeNormalAccount();
	void MakeCreditAccount();
	void Deposit();
	void Withdraw();
	void PrintAll();
	~AccountHandler();
};

#endif // !ACCOUNT_H
