#include <iostream>
#include <FTGL/ftgl.h>

int main() {
    std::cout << "FTGL: " << FTGL::GetString(FTGL::CONFIG_VERSION) << std::endl;
    return 0;
}
