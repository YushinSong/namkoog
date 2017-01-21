#ifndef ACCOUNT_H
#define AACOUNT_H

class Account
{
private:
	int accID;
	char *name;
	int money;
public:
	Account(int id, char *_name, int _money);
	int GetID();
	void Deposit(int _money);
	int Withdraw(int _money);
	void ShowAccInfo();
	~Account();
};

int PrintMenuMoney();
void MakeAccountMoney(int customer);
void DepositMoney();
void WithdrawMoney();
void PrintAllMoney();


#endif // !ACCOUNT_H
