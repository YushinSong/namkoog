#include "friend.h"

int main()
{
	MyFriendDetailInfo jack("jack", 32, "Indiana", "7676");
	MyFriendDetailInfo gabe("gabe", 33, "Spain", "763535");

	jack.ShowMyFriendDetailInfo();
	gabe.ShowMyFriendDetailInfo();
}