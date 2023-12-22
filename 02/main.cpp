#include <stdio.h>

#include <iostream>
#include <fstream>
#include <set>

int main(int argc, char *argv[]) {

    std::string inputFilePath;
    if (argc > 1) {
        inputFilePath = argv[1];
    } else {
        std::cout << "No input path" << std::endl;
        return EXIT_FAILURE;
    }

    std::ifstream listFile(inputFilePath);
    if (!listFile.is_open()) {
        std::cout << "Could not open input file" << std::endl;
        return EXIT_FAILURE;
    }

    std::string line;
    while(getline(listFile, line)) {
        if (!line.empty()) {

        }
    }
    std::cout << "Solution " << 0 << std::endl;
    return EXIT_SUCCESS;
}
