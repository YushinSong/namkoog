#include "book.h"

int main()
{
	Book book("������ �˹ٻ� ����", "010-5757-6514", 0);
	book.ShowBookInfo();

	EBook ebook("������ �˹ٻ� ���� ebook", "010-5757-6514", 0, "s1323klmd");
	ebook.ShowEBookInfo();
}