#include <iostream>
#include <cstring>
#include "friend.h"
using namespace std;


MyFriendInfo::MyFriendInfo(char *_name, int _age) : age(_age)
{
	name = new char[strlen(_name) + 1];
	strcpy(name, _name);
}
void MyFriendInfo::ShowMyFriendInfo()
{
	cout << "이름 : " << name << endl;
	cout << "나이 : " << age << endl;
}


MyFriendDetailInfo::MyFriendDetailInfo(char *name, int age, char *_addr, char *_phone) : MyFriendInfo(name, age)
{
	addr = new char[strlen(_addr) + 1];
	strcpy(addr, _addr);
	phone = new char[strlen(_phone) + 1];
	strcpy(phone, _phone);
}
void MyFriendDetailInfo::ShowMyFriendDetailInfo()
{
	ShowMyFriendInfo();
	cout << "주소 : " << addr << endl;
	cout << "번호 : " << phone << endl << endl;
}