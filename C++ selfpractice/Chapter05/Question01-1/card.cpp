#include <iostream>
#include <cstring>
#include "card.h"
using namespace std;



void COMP_POS::ShowPositionInfo(int pos)
{
	switch (pos)
	{
	case COMMANDER:
		cout << "사령관" << endl;
		break;
	case BOSS:
		cout << "대장" << endl;
		break;
	case TROOPS:
		cout << "부대원" << endl;
		break;
	case HEAD:
		cout << "수장" << endl;
		break;
	}
}

NameCard::NameCard(char *_name, char *_company, char *_num, int pos)
	: position(pos)
{
	name = new char[strlen(_name) + 1];
	company = new char[strlen(_company) + 1];
	num = new char[strlen(_num) + 1];
	strcpy(name, _name);
	strcpy(company, _company);
	strcpy(num, _num);
}
NameCard::NameCard(const NameCard& copy) : position(copy.position)
{
	name = new char[strlen(copy.name) + 1];
	company = new char[strlen(copy.company) + 1];
	num = new char[strlen(copy.num) + 1];
	strcpy(name, copy.name);
	strcpy(company, copy.company);
	strcpy(num, copy.num);
}
void NameCard::ShowNameCardInfo()
{
	cout << "이름 : " << name << endl;
	cout << "회사 : " << company << endl;
	cout << "전화전호 : " << num << endl;
	cout << "직급 : ";
	COMP_POS::ShowPositionInfo(position);
	cout << endl << endl;
}
NameCard::~NameCard()
{
	delete[]name;
	delete[]company;
	delete[]num;
}