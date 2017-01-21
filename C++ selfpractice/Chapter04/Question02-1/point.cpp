#include <iostream>
#include "point.h"
using namespace std;

void Point::Init(int x, int y, int r)
{
	xpos = x;
	ypos = y;
	radius = r;
}
void Point::ShowPointInfo() const
{
	cout << "radius : " << radius << endl;
	cout << "[" << xpos << ", " << ypos << "]" << endl;
}


void Ring::Init(int ix, int iy, int ir, int ox, int oy, int or)
{
	Inner.Init(ix, iy, ir);
	outter.Init(ox, oy, or );
}
void Ring::ShowRingInfo() const
{
	cout << "Inner Circle Info..." << endl;
	Inner.ShowPointInfo();
	cout << "outter Circle Info..." << endl;
	outter.ShowPointInfo();
}