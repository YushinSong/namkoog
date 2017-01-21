#ifndef POINT_H
#define POINT_H

class Point
{
private:
	int xpos;
	int ypos;
	int radius;
public:
	void Init(int x, int y, int r);
	void ShowPointInfo() const;
};

class Ring
{
private:
	Point Inner;
	Point outter;
public:
	void Init(int ix, int iy, int ir, int ox, int oy, int or );
	void ShowRingInfo() const;
};

#endif // !POINT_H
