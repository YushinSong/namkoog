#include <iostream>
using namespace std;

template <typename T>
class Point 
{
private:
	T xpos, ypos, temp;
public:
	Point(T x, T y) : xpos(x), ypos(y) { }
	void ShowPosition() const
	{
		cout << "[" << xpos << ", " << ypos << "]" << endl;
	}
	void SwapData()
	{
		temp = xpos;
		xpos = ypos;
		ypos = temp;
	}
};

int main()
{
	Point<int> pos1(3, 4);
	pos1.ShowPosition();
	pos1.SwapData();
	pos1.ShowPosition();

	Point<char> pos2('T', 'E');
	pos2.ShowPosition();
	pos2.SwapData();
	pos2.ShowPosition();
}