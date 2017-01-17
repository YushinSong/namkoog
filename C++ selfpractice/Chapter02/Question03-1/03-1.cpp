#include <iostream>
using namespace std;

typedef struct __Point
{
	int xPos;
	int yPos;
}Point;

Point& PntAdder(const Point &p1, const Point &p2)
{
	Point *ptr = new Point;
	ptr->xPos = p1.xPos + p2.xPos;
	ptr->yPos = p1.yPos + p2.yPos;

	return *ptr;
}

int main()
{
	Point *pnt1 = new Point;
	pnt1->xPos = 10;
	pnt1->yPos = 15;

	Point *pnt2 = new Point;
	pnt2->xPos = 20;
	pnt2->yPos = 10;

	Point &ptr = PntAdder(*pnt1, *pnt2);
	cout << ptr.xPos << ", " << ptr.yPos << endl;

	delete pnt1;
	delete pnt2;
	delete &ptr;
}