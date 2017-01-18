#include <iostream>
#include "Calculator.h"
using namespace std;

void Calculator::Init()
{
	add = 0, div = 0, min = 0, mul = 0;
}
double Calculator::Add(double num1, double num2)
{
	++add;
	return num1 + num2;
}
double Calculator::Div(double num1, double num2)
{
	++div;
	return num1 / num2;
}
double Calculator::Min(double num1, double num2)
{
	++min;
	return num1 - num2;
}
double Calculator::Mul(double num1, double num2)
{
	++mul;
	return num1 * num2;
}
void Calculator::ShowOpCount()
{
	cout << "���� : " << add;
	cout << " ���� : " << min;
	cout << " ���� : " << mul;
	cout << " ������ : " << div << endl;
}