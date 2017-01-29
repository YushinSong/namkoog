#include <iostream>
#include <cstring>
#include "book.h"
using namespace std;


Book::Book(char *_title, char *_isbn, int _price)
	: price(_price)
{ 
	title = new char[strlen(_title) + 1];
	isbn = new char[strlen(_isbn) + 1];
	strcpy(title, _title);
	strcpy(isbn, _isbn);
}
void Book::ShowBookInfo()
{
	cout << "제목 : " << title << endl;
	cout << "ISBN : " << isbn << endl;
	cout << "가격 : " << price << endl;
}


EBook::EBook(char *_title, char *_isbn, int _price, char *_DRMKey)
	: Book(_title, _isbn, _price)
{ 
	DRMKey = new char[strlen(_DRMKey) + 1];
	strcpy(DRMKey, _DRMKey);
}
void EBook::ShowEBookInfo()
{
	ShowBookInfo();
	cout << "인증키 : " << DRMKey << endl;
}
