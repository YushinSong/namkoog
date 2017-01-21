#ifndef FRUIT_H
#define FRUIT_H

class FruitSeller
{
private:
	int APPLE_PRICE;
	int numofApples;
	int myMoney;
public:
	void InitMembers(int price, int num, int money);
	int SaleApples(int money);
	void ShowSaleResult() const;
};

class FruitBuyer
{
private:
	int myMoney;
	int numofApples;
public:
	void InitMembers(int money);
	bool BuyApples(FruitSeller &seller, int money);
	void ShowBuyResult() const;
};

#endif // !FRUIT_H
