#include <iostream>
#include "car.h"
using namespace std;

int main()
{
	HybridCar car1(100, 200);
	HybridWaterCar car2(400, 500, 300);

	cout << car1.GetGasGauge() << " " << car1.GetElecGauge() << endl;
	car2.ShowCurrentGauge();
}