#include <iostream>
#include "shape.h"
using namespace std;


Rectangle::Rectangle(int _wid, int _hei) : wid(_wid), hei(_hei) { }

void Rectangle::ShowAreaInfo()
{
	cout << "���� : " << wid * hei << endl;
}


Square::Square(int _wid) : Rectangle(_wid, _wid) { }
