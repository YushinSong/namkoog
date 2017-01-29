#ifndef SHAPE_H
#define SHAPE_H


class Rectangle
{
private:
	int wid, hei;
public:
	Rectangle(int _wid, int _hei);
	void ShowAreaInfo();
};

class Square : public Rectangle
{
private:
	int wid;
public:
	Square(int _wid);
};


#endif // !SHAPE_H
