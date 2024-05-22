#include <iostream>

using std::cout;
using std::cin;

double power(double base, double exponent) {
    double total = base;
    for (std::size_t i=0; i < (exponent-1); i++)
        total *= base;
    return total;
};

int main() {
    int base, exponent;
    cout << "Enter base: ";
    cin >> base;
    cout << "Enter exponent: ";
    cin >> exponent;
    cout << power(base,exponent);
};
