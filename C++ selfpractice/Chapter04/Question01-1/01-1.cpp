#include <iostream>
#include "fruit.h"
using namespace std;

int main()
{
	FruitSeller seller;
	seller.InitMembers(1000, 20, 0);
	FruitBuyer buyer;
	buyer.InitMembers(5000);
	if (!buyer.BuyApples(seller, 2000))
		cout << "초기화 실패" << endl;

	cout << "과일 판매자의 현황" << endl;
	seller.ShowSaleResult();
	cout << "과일 구매자의 현황" << endl;
	buyer.ShowBuyResult();
}
