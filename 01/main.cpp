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

    int maxNbOfCalories = 0;
    std::set<int> firstElves;

    int current = 0;
    std::string line;
    while(getline(listFile, line)) {
        if (!line.empty()) {
            current += std::stoi(line);
        } else {
            if (current > maxNbOfCalories) {
                maxNbOfCalories = current;
            }
            if (firstElves.size() < 3) {
                firstElves.insert(current);
            } else if (*firstElves.begin() < current) {
                firstElves.erase(firstElves.begin());
                firstElves.insert(current);
            }
            current = 0;
        }
    }
    int sumOfFirst = 0;
    for (int nbCal:firstElves) {
        sumOfFirst += nbCal;
    }
    std::cout << "Max number of calories: " << maxNbOfCalories << std::endl;
    std::cout << "Sum of first: " << sumOfFirst << std::endl;
    return EXIT_SUCCESS;
}
