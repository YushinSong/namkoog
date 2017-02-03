#ifndef EMP_H
#define EMP_H

namespace RISK_LEVEL
{
	enum { RISK_A = 30, RISK_B = 20, RISK_C = 10 };
}

class Employee
{
private:
	char name[100];
public:
	Employee(char *name);
	void ShowYourName() const;
	virtual int GetPay() const;
	virtual void ShowSalaryInfo() const;
};

class PermanentWorker : public Employee
{
private:
	int salary;
public:
	PermanentWorker(char *name, int money);
	int GetPay() const;
	void ShowSalaryInfo() const;
};

class TemporaryWorker : public Employee
{
private:
	int workTime;
	int payPerHour;
public:
	TemporaryWorker(char *name, int pay);
	void AddWorkTime(int time);
	int GetPay() const;
	void ShowSalaryInfo() const;
};

class SalesWorker : public PermanentWorker
{
private:
	int salesResult;
	double bonusRatio;
public:
	SalesWorker(char *name, int money, double ratio);
	virtual void AddSalesResult(int value);
	int GetPay() const;
	void ShowSalaryInfo() const;
};

class ForeignSalesWorker : public SalesWorker
{
private: 
	int risk;
public:
	ForeignSalesWorker(char *name, int money, double ratio, int _risk);
	int GetRiskPay() const;
	int GetPay() const;
	void ShowSalaryInfo() const;
};

class EmployeeHandler
{
private:
	Employee *empList[50];
	int empNum;
public:
	EmployeeHandler();
	void AddEmployee(Employee *emp);
	void ShowAllSalaryInfo() const;
	void ShowTotalSalary() const;
	~EmployeeHandler();
};

#endif // !EMP_H
