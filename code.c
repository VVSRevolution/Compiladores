#include<stdio.h>
typedef char literal[256];
void main(void){
	literal	A;
	int 	G, F, E, D, B;
	double 	C;


	printf("Digite B:");
	scanf("%d",&B);
	printf("Digite A:");
	scanf("%s",A);
	if( B > 2 ) {
	if( B <= 4 ) {
	printf("B esta entre 2 e 4");
	}
	}
	B = B + 1 ; 
	B = B + 2 ; 
	B = B + 3 ; 
	D = B ; 
	C = 5.0 ; 
	printf("\nB=\n");
	printf("%d",D);
	printf("%d",E);
	printf("\n");
	printf("%lf",C);
	printf("\n");
	printf("%s",A);
}