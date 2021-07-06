#include <iostream>
using namespace std;
int main() {

	//Program 5

	//fibonacci numbers


	// 0 1  1 2  3  5   8  13 .......
	// current = last + secondlast

	// f(0) = 0;
	// f(1) = 1;
	// f(n) = f(n-1) + f(n-2);

	int first = 0;
	int second = 1;
	cout << first << " " << second << " ";

	for(int i = 3; i <= 20; i++){
		int third = first + second;
		cout << third << " ";
		first = second;
		second = third;

	}

	// 0 1
	//i=3    f=0, s=1, t=f+s=0+1=1
	     //  f=1, s=1
	//i=4   f=1, s=1, t = f+s = 1+1 = 2
	    //  f = 1, s = 2
	// i = 5  f=1, s=2, t=1+2=3
	   // f=2, s=3

// 0 1  1  2  3 ......
  
 
  return 0;
}