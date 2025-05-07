#include <stdio.h>
#include <math.h>
#include <inttypes.h>
#include <stdint.h>

#define INT uint64_t
#define PINT PRIu64
#define SINT SCNu64

typedef struct {
	INT a;
	INT b;
} sp_t;

INT llp(INT a, int pow);
sp_t split_num(INT num, int sndlen);
INT unsplit_num(sp_t sp);
int numlen(INT num);

int main() {
	INT bnum = 4;
	sp_t sp;
	INT num = 16;
	INT maxnum = llp(10,16);
	INT ret = 0;
	int nl;
	int f;
	while (num < maxnum) {
		nl = numlen(num);
		f = 1;
			sp = split_num(num, nl>>1);
		if ((sp.a+sp.b == bnum) && (unsplit_num(sp) == num) && (llp(sp.a+sp.b, 2) == num)) {
				ret += num;
				f = 0;
				printf("%"PINT"\n",num);
		}
		if ((nl & 1) && f){
			sp = split_num(num, nl/2 + 1);
			if ((sp.a+sp.b == bnum) && (unsplit_num(sp) == num) && (llp(sp.a+sp.b, 2) == num)) {
				ret += num;
				printf("->>%"PINT"\n",num);
			}
		}
		++bnum;
		num = llp(bnum,2);
	}
	printf( "%"PINT"\n", ret);
}

int numlen(INT num){
	int ret = 0;
	while (num) { ++ret; num /=10; }
	return ret;
}
INT llp(INT a, int pow){
	INT ret = 1;
	while (pow) {
		ret *= a;
		--pow;
	}
	return ret;
}

sp_t split_num(INT num, int sndlen) {
	sp_t ret;
	ret.a = num;
	for ( int i = 0; i != sndlen; ++i ) {ret.a /= 10;}
	ret.b = num % (ret.a*llp(10,sndlen));
	return ret;
}

INT unsplit_num(sp_t sp) {
	return sp.a * llp(10, numlen(sp.b)) + sp.b;
}
