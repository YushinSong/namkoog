#include <iostream>
#include "fruit.h"
using namespace std;

int main()
{
	int *num;
	num = new int(100);
	FruitSeller seller;
	seller.InitMembers(1000, 20, 0);
	FruitBuyer buyer;
	buyer.InitMembers(5000);
	if (!buyer.BuyApples(seller, 2000))
		cout << "�ʱ�ȭ ����" << endl;

	cout << *num;
	cout << "���� �Ǹ����� ��Ȳ" << endl;
	seller.ShowSaleResult();
	cout << "���� �������� ��Ȳ" << endl;
	buyer.ShowBuyResult();
}
