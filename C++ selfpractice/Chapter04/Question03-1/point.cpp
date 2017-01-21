#include <iostream>
#include "point.h"
using namespace std;

void Point::ShowPointInfo() const
{
	cout << "radius : " << radius << endl;
	cout << "[" << xpos << ", " << ypos << "]" << endl;
}


void Ring::ShowRingInfo() const
{
	cout << "Inner Circle Info..." << endl;
	Inner.ShowPointInfo();
	cout << "outter Circle Info..." << endl;
	outter.ShowPointInfo();
}