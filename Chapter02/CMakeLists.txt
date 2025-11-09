cmake_minimum_required(VERSION 3.14)

project(Chapter02-Essential_C++_Techniques)

file(GLOB CHAPTER_SRC_FILES "${CMAKE_CURRENT_SOURCE_DIR}/*.cpp" "${CMAKE_CURRENT_SOURCE_DIR}/*.h")

add_executable(${PROJECT_NAME} ${CHAPTER_SRC_FILES})
target_link_libraries(${PROJECT_NAME} GTest::gtest_main)
gtest_discover_tests(${PROJECT_NAME})
if(CMAKE_BUILD_TYPE STREQUAL "Release")
    add_subdirectory("benchmarks")
endif()
