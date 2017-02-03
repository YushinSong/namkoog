#include <iostream>
using namespace std;

class Point
{
private:
	int xpos, ypos;
public:
	Point(int x = 0, int y = 0) : xpos(x), ypos(y) { }
	void ShowPosition() const
	{
		cout << "[" << xpos << ", " << ypos << "]" << endl;
	}
	friend Point& operator+=(Point &pos1, const Point &pos2);
	friend Point& operator-=(Point &pos1, const Point &pos2);
};

Point& operator+=(Point &pos1, const Point &pos2)
{
	pos1.xpos += pos2.xpos;
	pos1.ypos += pos2.ypos;
	return pos1;
}
Point& operator-=(Point &pos1, const Point &pos2)
{
	pos1.xpos -= pos2.xpos;
	pos1.ypos -= pos2.ypos;
	return pos1;
}

int main()
{
	Point pos1(3, 4);
	Point pos2(10, 20);
	pos1 += pos2;
	pos1.ShowPosition();
	pos1 -= pos2;
	pos1.ShowPosition();
}