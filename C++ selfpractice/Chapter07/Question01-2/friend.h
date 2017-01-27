#ifndef FRIEND_H
#define FRIEND_H

class MyFriendInfo
{
private:
	char *name;
	int age;
public:
	MyFriendInfo(char *_name, int _age);
	void ShowMyFriendInfo();
};

class MyFriendDetailInfo : public MyFriendInfo
{
private:
	char *addr;
	char *phone;
public:
	MyFriendDetailInfo(char *name, int age, char *_addr, char *_phone);
	void ShowMyFriendDetailInfo();
};

#endif // !FRIEND_H
