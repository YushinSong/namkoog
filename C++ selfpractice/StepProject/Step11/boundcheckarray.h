#ifndef ARRAY_H
#define ARRAY_H


template <typename T>
class BoundCheckArray
{
private:
	T *arr;
	int arrlen;
	BoundCheckArray(const BoundCheckArray& arr) { }
	BoundCheckArray& operator=(const BoundCheckArray& arr) { }
public:
	BoundCheckArray(int len = 100);
	T& operator[] (int idx);
	T operator[] (int idx) const;
	int GetArrLen() const;
	~BoundCheckArray();
};

#endif // !ARRAY_H
