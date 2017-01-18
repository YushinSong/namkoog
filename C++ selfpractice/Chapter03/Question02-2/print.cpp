#include <iostream>
#include <cstring>
#include "print.h"
using namespace std;

void Printer::SetString(char *str)
{
	strcpy(word, str);
}
void Printer::ShowString()
{
	cout << word << endl;
}