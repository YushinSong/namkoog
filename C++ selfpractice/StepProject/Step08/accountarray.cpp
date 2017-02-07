#include "account.h"
#include <iostream>
#include "accountarray.h"
using namespace std;

BoundCheckAccountPtrArray::BoundCheckAccountPtrArray(int len) : arrlen(len){ }
ACCOUNT_PTR& BoundCheckAccountPtrArray::operator[] (int idx)
{
	if (idx < 0 || idx >= arrlen)
	{
		cout << "Array index out of bound exception" << endl;
		exit(1);
	}
	return arr[idx];
}
ACCOUNT_PTR BoundCheckAccountPtrArray::operator[] (int idx) const
{
	if (idx < 0 || idx >= arrlen)
	{
		cout << "Array index out of bound exception" << endl;
		exit(1);
	}
	return arr[idx];
}
int BoundCheckAccountPtrArray::GetArrLen() const
{
	return arrlen;
}
BoundCheckAccountPtrArray::~BoundCheckAccountPtrArray()
{
	delete[]arr;
}
