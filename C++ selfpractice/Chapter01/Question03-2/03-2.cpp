// 다음과 같은 형태의 함수오버로딩은 문제가 있다. 어떠한 문제가 있는가

int SimpleFunc(int a = 10)
{
	return a + 1;
}

int SimpleFunc(void)
{
	return 10;
}

// 컴파일은 된다.
// 그러나 SimpleFunc();의 경우 두가지 호출조건 모두 만족해서 문제가 발생한다.