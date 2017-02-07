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
	Book(const Book& ref);
	Book& operator=(const Book& ref);
	void ShowBookInfo();
};

class EBook : public Book
{
private:
	char *DRMKey;
public:
	EBook(char *_title, char *_isbn, int _price, char *_DRMKey);
	EBook(const EBook& ref);
	EBook& operator=(const EBook& ref);
	void ShowEBookInfo();
};

#endif // !BOOK_H
