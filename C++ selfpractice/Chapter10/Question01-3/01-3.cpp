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
	friend bool operator==(const Point &pos1, const Point &pos2);
	friend bool operator!=(const Point &pos1, const Point &pos2);
};

bool operator==(const Point &pos1, const Point &pos2)
{
	if (pos1.xpos == pos2.xpos)
		return true;
	else
		return false;
}
bool operator!=(const Point &pos1, const Point &pos2)
{
	if (pos1.xpos != pos2.xpos)
		return true;
	else
		return false;
}

int main()
{
	Point pos1(3, 4);
	Point pos2(10, 20);
	
	if ((pos1 == pos2) == true)
		cout << "same" << endl;
	if ((pos1 != pos2) == true)
		cout << "not same" << endl;
}