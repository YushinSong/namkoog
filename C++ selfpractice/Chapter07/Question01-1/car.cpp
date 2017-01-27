#include <iostream>
#include "car.h"
using namespace std;



Car::Car(int gas) : gasolineGauge(gas){ }

int Car::GetGasGauge()
{
	return gasolineGauge;
}


HybridCar::HybridCar(int gas, int elec) : Car(gas), electricGauge(elec) { }

int HybridCar::GetElecGauge()
{
	return electricGauge;
}


HybridWaterCar::HybridWaterCar(int gas, int elec, int water) : HybridCar(gas, elec), waterGauge(water) { }

void HybridWaterCar::ShowCurrentGauge()
{
	cout << "ÀÜ¿© °¡¼Ö¸° : " << GetGasGauge() << endl;
	cout << "ÀÜ¿© Àü±â·® : " << GetElecGauge() << endl;
	cout << "ÀÜ¿© ¿öÅÍ·® : " << waterGauge << endl;
}
