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
	friend Point& operator-(const Point &pos);
};

Point& operator-(const Point &pos)
{
	Point ref(pos.xpos * -1, pos.ypos * -1);
	return ref;
}

int main()
{
	Point pos1(3, 4);
	Point pos2 = -pos1;
	pos2.ShowPosition();
}