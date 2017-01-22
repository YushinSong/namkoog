#include <iostream>
#include "card.h"

int main()
{
	NameCard manBoss("Gabriel Reyes", "BLACKWATCH", "185-1111-1111", COMP_POS::BOSS);
	NameCard copy1 = manBoss;
	NameCard manComm("Jack Morrison", "OVERWATCH", "185-7676-7676", COMP_POS::COMMANDER);
	NameCard copy2 = manComm;
	copy1.ShowNameCardInfo();
	copy2.ShowNameCardInfo();
}