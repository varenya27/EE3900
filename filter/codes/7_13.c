#include <stdio.h>
#include <math.h>
#include <complex.h>
#include <stdlib.h>
#define pi 3.14159

complex *fft(int N, complex *x) {
    if(N==1) return x;
    complex *X1 = (complex *)malloc(N/2*sizeof(complex));
    complex *X2 = (complex *)malloc(N/2*sizeof(complex));
    for(int i=0;i<N;i++){
        if(i%2==0) X1[i/2]=x[i];
        else X2[i/2]=x[i];
    }

    X1= fft(N/2,X1);
    X2= fft(N/2,X2);

    int k=0;
    for(int i=0;i<N;i++){
        if(i==N/2) k=0;
        // printf("%d %d\n",i,k);
        // x[i]=X1[k]+cexp(-I*2*M_PI*i/N)*X2[k];
        x[i]=X1[i%(N/2)]+cexp(-I*2*pi*i/N)*X2[i%(N/2)];
        k++;
    }
    free(X1);
    free(X2);
    return x;
}

int main() { 
    int N=8;
    complex* x = (complex*)malloc(N*sizeof(complex));
    x[0]=1.;
    x[1]=2.;
    x[2]=3.;
    x[3]=4.;
    x[4]=2.;
    x[5]=1.;
    x[6]=0.;
    x[7]=0.;
    complex* X = (complex*)malloc(N*sizeof(complex));
    X=fft(N,x);
    for(int i=0;i<N;i++){
        printf("X(%d) = %.2f + j(%.2f)\n",i,creal(X[i]),cimag(X[i]));
    }
	return 0;


}