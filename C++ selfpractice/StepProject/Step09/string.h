#ifndef STRING_H
#define STRING_H

#include <iostream>
#include <cstring>
#include "BankingCommonDecl.h"

class String
{
private:
	int len;
	char *str;
public:
	String();
	String(const char *s);
	String(const String& s);
	~String();
	String& operator=(const String& s);
	String& operator+=(const String& s);
	bool operator==(const String& s);
	String operator+ (const String& s);

	friend ostream& operator<< (ostream& os, const String& s);
	friend istream& operator>> (istream& is, String& s);
};

#endif // !STRING_H