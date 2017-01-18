#ifndef CAL_H
#define CAL_H

class Calculator 
{
private:
	int add, div, min, mul;
public:
	void Init();
	double Add(double num1, double num2);
	double Div(double num1, double num2);
	double Min(double num1, double num2);
	double Mul(double num1, double num2);
	void ShowOpCount();
};

#endif //CAL_H