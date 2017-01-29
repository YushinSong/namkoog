#ifndef BOOK_H
#define BOOK_H

class Book
{
private:
	char *title;
	char *isbn;
	int price;
public:
	Book(char *_title, char *_isbn, int _price);
	void ShowBookInfo();
};

class EBook : public Book
{
private:
	char *DRMKey;
public:
	EBook(char *_title, char *_isbn, int _price, char *_DRMKey);
	void ShowEBookInfo();
};

#endif // !BOOK_H
