#ifndef EXCEPTION_H
#define EXCEPTION_H

#include <iostream>
using namespace std;

class MinusException
{
private:
	int exval;
public:
	MinusException(int val) : exval(val) { }
	void ShowExceptionInfo() const
	{
		cout << "��(��)�ݾ� " << exval << "�� ��ȿ���� �ʽ��ϴ�!" << endl;
	}
};

class InsuffException
{
private:
	int balance;
	int reqval;
public:
	InsuffException(int val, int req) : balance(val), reqval(req) { }
	void ShowExceptionInfo() const
	{
		cout << "�ܾ׿��� " << reqval - balance << "��(��) �����մϴ�!" << endl;
	}
};


#endif // !EXCEPTION_H