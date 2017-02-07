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
Book::Book(const Book& ref) :price(ref.price)
{
	title = new char[strlen(ref.title) + 1];
	isbn = new char[strlen(ref.isbn) + 1];
	strcpy(title, ref.title);
	strcpy(isbn, ref.isbn);
}
Book& Book::operator=(const Book& ref)
{
	delete[]title;
	delete[]isbn;

	title = new char[strlen(ref.title) + 1];
	isbn = new char[strlen(ref.isbn) + 1];
	strcpy(title, ref.title);
	strcpy(isbn, ref.isbn);
	price = ref.price;
	return *this;
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
EBook::EBook(const EBook& ref) : Book(ref)
{
	DRMKey = new char[strlen(ref.DRMKey) + 1];
	strcpy(DRMKey, ref.DRMKey);
}
EBook& EBook::operator=(const EBook& ref)
{
	Book::operator=(ref);
	delete[]DRMKey;
	DRMKey = new char[strlen(ref.DRMKey) + 1];
	strcpy(DRMKey, ref.DRMKey);
	return *this;
}
void EBook::ShowEBookInfo()
{
	ShowBookInfo();
	cout << "인증키 : " << DRMKey << endl;
}
