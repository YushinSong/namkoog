#ifndef CARD_H
#define CARD_H

#include <iostream>

namespace COMP_POS
{
	enum { COMMANDER, BOSS, TROOPS, HEAD };

	void ShowPositionInfo(int pos);
}

class NameCard
{
private:
	char *name, *company, *num;
	int position;
public:
	NameCard(char *_name, char *_company, char *_num, int pos);
	NameCard(const NameCard& copy);
	void ShowNameCardInfo();
	~NameCard();
};

#endif // !CARD_H
