//simple lr
//g++ simplelr.cpp -o lr `pkg-config --cflags --libs mlpack` -fopenmp
//./lr test.csv 

#include<iostream>
#include<mlpack/core.hpp>

using namespace std;
using namespace mlpack;

void regression(double& b0, double&b1, arma::mat& matrix);

int main(int argc, char** argv){
	double b0, b1;
	arma::mat matrix;
	data::Load(argv[1], matrix);
	regression(b0,b1,matrix);
	cout<<"f(x)="<<b0<<"+"<<b1<<"x"<<endl;
	return 0;
}

void regression(double& b0, double& b1, arma::mat& matrix){
	double num=0, den=0, y=0, x=0;
	for(unsigned i=0; i<1000; i++){
		y+=matrix(1,i);
		x+=matrix(0,i);
	}
	y/=1000;
	x/=1000;
	for(unsigned i=0; i<1000; i++){
		num+=(y-matrix(1,i))*matrix(0,i);
		den+=(x-matrix(0,i))*matrix(0,i);
	}
	b1=num/den;
	b0=y-b1*x;
}
