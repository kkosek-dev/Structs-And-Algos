#include <iostream>
#include <string>

int main() {
    std::string line;
    std::cout << "Enter a line of text:\n";
    getline(std::cin, line);
    std::cout << "You entered: " << line << '\n';
    return 0;
}
