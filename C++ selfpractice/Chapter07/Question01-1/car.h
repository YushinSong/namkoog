#ifndef CAR_H
#define CAR_H

class Car
{
private:
	int gasolineGauge;
public:
	Car(int gas);
	int GetGasGauge();
};

class HybridCar : public Car
{
private:
	int electricGauge;
public:
	HybridCar(int gas, int elec);
	int GetElecGauge();
};

class HybridWaterCar : public HybridCar
{
private:
	int waterGauge;
public:
	HybridWaterCar(int gas, int elec, int water);
	void ShowCurrentGauge();
};


#endif // !CAR_H
