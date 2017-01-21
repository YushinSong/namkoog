#include <iostream>
#include "fruit.h"
using namespace std;

void FruitSeller::InitMembers(int price, int num, int money)
{
	APPLE_PRICE = price;
	numofApples = num;
	myMoney = money;
}
int FruitSeller::SaleApples(int money)
{
	int num = money / APPLE_PRICE;
	numofApples -= num;
	myMoney += money;
	return num;
}
void FruitSeller::ShowSaleResult() const
{
	cout << "남은 사과 : " << numofApples << endl;
	cout << "판매 수익 : " << myMoney << endl << endl;
}



void FruitBuyer::InitMembers(int money)
{
	myMoney = money;
	numofApples = 0;
}
bool FruitBuyer::BuyApples(FruitSeller &seller, int money)
{
	if (money < 0)
	{
		cout << "0보다 큰 돈을 지불해야 합니다." << endl;
		return false;
	}
	numofApples += seller.SaleApples(money);
	myMoney -= money;
	return true;
}
void FruitBuyer::ShowBuyResult() const
{
	cout << "현재 잔액 : " << myMoney << endl;
	cout << "사과 개수 : " << numofApples << endl << endl;
}