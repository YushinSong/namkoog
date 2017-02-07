#include "police.h"

int main()
{
	Police pman1(5, 3);
	Police pman2 = pman1;
	pman2.PutHandcuff();
	pman2.shot();

	Police pman3(2, 4);
	pman3 = pman1;
	pman3.PutHandcuff(); 
	pman3.shot();
}