cmake_minimum_required(VERSION 3.10)
project(NOTAMTest)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)

# Include GoogleTest
add_subdirectory(googletest)

# Add sources and tests
add_executable(runTests notam_test.cpp notam.cpp)
target_link_libraries(runTests gtest gtest_main pthread)