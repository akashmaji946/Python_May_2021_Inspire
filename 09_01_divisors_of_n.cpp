#include <iostream>
using namespace std;
int main() {

	// Program 2

	// 12 => 1, 2, 3, 4, 6, 12 (divisors of 12)

	int n;
	cin >> n;

	for(int i = 1; i <= n; i++){
		if(n % i == 0){
			cout << i << " is a divisor of " << n << endl;
		}
	}
  

  return 0;
}