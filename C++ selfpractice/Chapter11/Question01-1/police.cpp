#include <iostream>
#include "police.h"
using namespace std;


Gun::Gun(int bnum) : bullet(bnum) { }
void Gun::shot()
{
	cout << "bang!!" << endl;
	bullet--;
}


Police::Police(int bnum, int bcuff) : handcuffs(bcuff)
{
	if (bnum > 0)
		pistol = new Gun(bnum);
	else
		pistol = NULL;
}
Police::Police(const Police& ref) : handcuffs(ref.handcuffs)
{
	if (ref.pistol != NULL)
		pistol = new Gun(*(ref.pistol));
	else
		pistol = NULL;
}
Police& Police::operator=(const Police& ref)
{
	if (pistol != NULL)
		delete pistol;

	if (ref.pistol != NULL)
		pistol = new Gun(*(ref.pistol));
	else
		pistol = NULL;

	handcuffs = ref.handcuffs;
	return *this;
}
void Police::PutHandcuff()
{
	cout << "snap!!" << endl;
	handcuffs--;
}
void Police::shot()
{
	if (pistol == NULL)
		cout << "Hut bang!!" << endl;
	else
		pistol->shot();
}
Police::~Police()
{
	if (pistol != NULL)
		delete pistol;
}
