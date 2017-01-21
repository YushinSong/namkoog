#include <iostream>
#include "card.h"

int main()
{
	NameCard manBoss("Gabriel Reyes", "BLACKWATCH", "185-1111-1111", COMP_POS::BOSS);
	NameCard manComm("Jack Morrison", "OVERWATCH", "185-7676-7676", COMP_POS::COMMANDER);
	NameCard manTroo("Jesses Mccree", "BLACKWATCH", "185-2222-2222", COMP_POS::TROOPS);
	NameCard manHead("Simada Hanzo", "SIMADA", "173-0000-0000", COMP_POS::HEAD);
	manBoss.ShowNameCardInfo();
	manComm.ShowNameCardInfo();
	manTroo.ShowNameCardInfo();
	manHead.ShowNameCardInfo();
}