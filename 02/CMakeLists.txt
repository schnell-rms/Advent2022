cmake_minimum_required(VERSION 3.27)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
#set(CMAKE_CXX_EXTENSIONS OFF)

project(advent)

include_directories("${PROJECT_SOURCE_DIR}")
add_executable(advent main.cpp)
