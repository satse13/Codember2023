#include <iostream>
using namespace std;

void challenge(string mensaje){
	int ret = 0;

	for(char c: mensaje){

		switch(c){
			case '#':
				ret += 1;
				break;
			case '@':
				ret -= 1;
				break;
			case '*':
				ret *= ret;
				break;
			case '&':
				cout << ret;
				break;
			default:
				break;
		}

	}
}


int main(){

	challenge("&###@&*&###@@##@##&######@@#####@#@#@#@##@@@@@@@@@@@@@@@*&&@@@@@@@@@####@@@@@@@@@#########&#&##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@&");

	return 0;
}