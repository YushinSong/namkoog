#include "print.h"

int main()
{
	Printer pnt;
	pnt.SetString("I love you");
	pnt.ShowString();

	pnt.SetString("me too");
	pnt.ShowString();
}