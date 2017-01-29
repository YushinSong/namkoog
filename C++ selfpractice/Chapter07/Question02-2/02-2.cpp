#include "book.h"

int main()
{
	Book book("전지적 알바생 시점", "010-5757-6514", 0);
	book.ShowBookInfo();

	EBook ebook("전지적 알바생 시점 ebook", "010-5757-6514", 0, "s1323klmd");
	ebook.ShowEBookInfo();
}