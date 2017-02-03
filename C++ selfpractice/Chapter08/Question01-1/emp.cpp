#include <iostream>
#include <cstring>
#include "emp.h"
using namespace std;


Employee::Employee(char *name)
{
	strcpy(this->name, name);
}
void Employee::ShowYourName() const
{
	cout << "name : " << name << endl;
}
int Employee::GetPay() const
{
	return 0;
}
void Employee::ShowSalaryInfo() const { }



PermanentWorker::PermanentWorker(char *name, int money)
	: Employee(name), salary(money) { }
int PermanentWorker::GetPay() const
{
	return salary;
}
void PermanentWorker::ShowSalaryInfo() const
{
	ShowYourName();
	cout << "salary : " << GetPay() << endl << endl;
}



TemporaryWorker::TemporaryWorker(char *name, int pay)
	: Employee(name), workTime(0), payPerHour(pay) { }
void TemporaryWorker::AddWorkTime(int time)
{
	workTime += time;
}
int TemporaryWorker::GetPay() const
{
	return workTime*payPerHour;
}
void TemporaryWorker::ShowSalaryInfo() const
{
	ShowYourName();
	cout << "salary : " << GetPay() << endl << endl;	
}



SalesWorker::SalesWorker(char *name, int money, double ratio)
	: PermanentWorker(name, money), salesResult(0), bonusRatio(ratio) { }
void SalesWorker::AddSalesResult(int value)
{
	salesResult += value;
}
int SalesWorker::GetPay() const
{
	return PermanentWorker::GetPay() + (int)(salesResult*bonusRatio);
}
void SalesWorker::ShowSalaryInfo() const
{
	ShowYourName();
	cout << "salary : " << GetPay() << endl << endl;
}


ForeignSalesWorker::ForeignSalesWorker(char *name, int money, double ratio, int _risk)
	: SalesWorker(name, money, ratio), risk(_risk) { }
int ForeignSalesWorker::GetRiskPay() const
{
	return (int)(SalesWorker::GetPay() * (risk / 100.0));
}
int ForeignSalesWorker::GetPay() const
{
	return SalesWorker::GetPay() + GetRiskPay();
}
void ForeignSalesWorker::ShowSalaryInfo() const
{
	ShowYourName();
	cout << "salary : " << SalesWorker::GetPay()  << endl;
	cout << "riskpay : " << GetRiskPay()  << endl;
	cout << "sum : " << GetPay() << endl << endl;
}




EmployeeHandler::EmployeeHandler() : empNum(0) { }
void EmployeeHandler::AddEmployee(Employee *emp)
{
	empList[empNum++] = emp;
}
void EmployeeHandler::ShowAllSalaryInfo() const
{
	for (int i = 0; i < empNum; ++i)
		empList[i]->ShowSalaryInfo();
}
void EmployeeHandler::ShowTotalSalary() const
{
	int sum = 0;
	for (int i = 0; i < empNum; ++i)
		sum += empList[i]->GetPay();

	cout << "salary sum : " << sum << endl;	
}
EmployeeHandler::~EmployeeHandler()
{
	for (int i = 0; i < empNum; ++i)
		delete empList[i];
}