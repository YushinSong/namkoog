#ifndef POINT_H
#define POINT_H

class Point
{
private:
	int xpos;
	int ypos;
	int radius;
public:
	Point(int x, int y, int r) : xpos(x), ypos(y), radius(r) { }
	void ShowPointInfo() const;
	~Point() { }
};

class Ring
{
private:
	Point Inner;
	Point outter;
public:
	Ring(int ix, int iy, int ir, int ox, int oy, int or )
		:Inner(ix, iy, ir), outter(ox, oy, or) { }
	void ShowRingInfo() const;
	~Ring() { }
};

#endif // !POINT_H