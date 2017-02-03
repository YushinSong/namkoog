#include <iostream>
#include <cstring>
#include "emp.h"
using namespace std;


int main()
{
	EmployeeHandler handler;

	ForeignSalesWorker *fseller1 = new ForeignSalesWorker("jack", 1000, 0.1, RISK_LEVEL::RISK_A);
	fseller1->AddSalesResult(7000);
	handler.AddEmployee(fseller1);

	ForeignSalesWorker *fseller2 = new ForeignSalesWorker("gabe", 1000, 0.1, RISK_LEVEL::RISK_A);
	fseller2->AddSalesResult(7000);
	handler.AddEmployee(fseller2);

	ForeignSalesWorker *fseller3 = new ForeignSalesWorker("jess", 1000, 0.1, RISK_LEVEL::RISK_B);
	fseller3->AddSalesResult(7000);
	handler.AddEmployee(fseller3);

	handler.ShowAllSalaryInfo();
}