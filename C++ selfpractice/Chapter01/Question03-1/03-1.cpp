#include <iostream>
using namespace std;

int BoxVolume(int lentgth, int width, int height);
int BoxVolume(int lentgth, int width);
int BoxVolume(int lentgth);

int main()
{
	cout << "[3, 3, 3] : " << BoxVolume(3, 3, 3) << endl;
	cout << "[5, 5, D] : " << BoxVolume(5, 5) << endl;
	cout << "[7, D, D] : " << BoxVolume(7) << endl;
}
int BoxVolume(int lentgth, int width, int height)
{
	return lentgth*width*height;
}
int BoxVolume(int lentgth, int width)
{
	return lentgth*width;
}
int BoxVolume(int lentgth)
{
	return lentgth;
}