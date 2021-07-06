#include <iostream>
using namespace std;
int main() {
  //program 1
  // user input => n
  // n is prime or not

  // Prime: 2   3   7   13 ....
  // Composite: 2 8   10  100....

//   n = 17 => when it is divisible by 1 and itself
//  1, 2, 3, ......, n
// total 2 times divide => prime

  int n;
 

  cout << "Enter a number: ";
   cin >> n;

   int total_divisors = 0;

   for(int i = 1; i <= n; i++){
	   if(n % i == 0){
		   total_divisors++;
	   }
   }

   cout << "Total Divisors: " << total_divisors << endl;

   if(total_divisors ==  2){
	   cout << n << " is prime\n";
   }else{
	   cout << n << " is not prime\n";
   }








  return 0;
}