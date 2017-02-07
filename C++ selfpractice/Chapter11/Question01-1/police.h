#ifndef POLICE_H
#define POLICE_H

class Gun
{
private:
	int bullet;
public:
	Gun(int bnum);
	void shot();
};

class Police
{
private:
	int handcuffs;
	Gun * pistol;
public:
	Police(int bnum, int bcuff);
	Police(const Police& ref);
	Police& operator=(const Police& ref);
	void PutHandcuff();
	void shot();
	~Police();
};

#endif // !POLICE_H
