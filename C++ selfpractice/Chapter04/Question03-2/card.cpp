#include <iostream>
#include <cstring>
#include "card.h"
using namespace std;



void COMP_POS::ShowPositionInfo(int pos)
{
	switch (pos)
	{
	case COMMANDER:
		cout << "��ɰ�" << endl;
		break;
	case BOSS:
		cout << "����" << endl;
		break;
	case TROOPS:
		cout << "�δ��" << endl;
		break;
	case HEAD:
		cout << "����" << endl;
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
void NameCard::ShowNameCardInfo()
{
	cout << "�̸� : " << name << endl;
	cout << "ȸ�� : " << company << endl;
	cout << "��ȭ��ȣ : " << num << endl;
	cout << "���� : ";
	COMP_POS::ShowPositionInfo(position);
	cout << endl <<  endl;
}
NameCard::~NameCard()
{
	delete[]name;
	delete[]company;
	delete[]num;
}