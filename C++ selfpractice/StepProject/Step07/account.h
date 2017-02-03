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



#endif // !ACCOUNT_H
