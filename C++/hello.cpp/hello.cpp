//-exec x/16x 0x7fffffffdf14
//:!g++ -o hello % && ./hello


#include <iostream>
using namespace std;

// main() is where program execution begins.
int main() {
	int arr[5];
	int a = 8;
	void *b = &a;
	arr[0] =1;
	arr[1] = 2;
	arr[3] = 3;
   	std::cout <<"hi Dass";
	std::cout << arr[1]; // prints Hello World
   return 0;
}
