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
	cout << "���� ��� : " << numofApples << endl;
	cout << "�Ǹ� ���� : " << myMoney << endl << endl;
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
		cout << "0���� ū ���� �����ؾ� �մϴ�." << endl;
		return false;
	}
	numofApples += seller.SaleApples(money);
	myMoney -= money;
	return true;
}
void FruitBuyer::ShowBuyResult() const
{
	cout << "���� �ܾ� : " << myMoney << endl;
	cout << "��� ���� : " << numofApples << endl << endl;
}