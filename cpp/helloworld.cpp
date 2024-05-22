#include <iostream>
using std::cout;

struct Complex {
    double real;
    double imaginary;  
};

void Complex_print(Complex number) {
    cout << number.real;
    if (number.imaginary >= 0) {
        cout << '+';
    };
    cout << number.imaginary << std::endl;
};
    
int main() {
    Complex c1 = {3.14,-1.7};
    Complex c2 = {0,0};
    Complex_print(c1);
    Complex_print(c2);
};