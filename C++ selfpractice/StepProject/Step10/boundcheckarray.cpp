#include "account.h"
#include <iostream>
#include "boundcheckarray.h"
using namespace std;

template <typename T>
BoundCheckArray<T>::BoundCheckArray(int len) : arrlen(len)
{
	arr = new T[len];
}

template <typename T>
T& BoundCheckArray<T>::operator[] (int idx)
{
	if (idx < 0 || idx >= arrlen)
	{
		cout << "Array index out of bound exception" << endl;
		exit(1);
	}
	return arr[idx];
}

template <typename T>
T BoundCheckArray<T>::operator[] (int idx) const
{
	if (idx < 0 || idx >= arrlen)
	{
		cout << "Array index out of bound exception" << endl;
		exit(1);
	}
	return arr[idx];
}

template <typename T>
int BoundCheckArray<T>::GetArrLen() const
{
	return arrlen;
}

template <typename T>
BoundCheckArray<T>::~BoundCheckArray()
{
	delete[]arr;
}
