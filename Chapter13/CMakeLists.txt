cmake_minimum_required(VERSION 3.14)

project(Chapter13-Asynchronous_Programming_With_Coroutines)

add_definitions(-DBOOST_ASIO_DISABLE_CONCEPTS)
add_definitions(-DBOOST_DATE_TIME_NO_LIB)
add_definitions(-DBOOST_REGEX_NO_LIB)

# Build test
file(GLOB CHAPTER_SRC_FILES "${CMAKE_CURRENT_SOURCE_DIR}/*.cpp" "${CMAKE_CURRENT_SOURCE_DIR}/*.h")
list(FILTER CHAPTER_SRC_FILES EXCLUDE REGEX ".*asio_server.cpp")
add_executable(${PROJECT_NAME} ${CHAPTER_SRC_FILES})
target_link_libraries(${PROJECT_NAME} GTest::gtest_main Boost::boost)

# Boost 1.72 only supports awaitable when using MSVC or Clang
if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "MSVC" OR "${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang" OR "${CMAKE_CXX_COMPILER_ID}" STREQUAL "AppleClang")
  # Build asio server as a standalone program
  file(GLOB SERVER_SRC_FILES "${CMAKE_CURRENT_SOURCE_DIR}/*.h" "${CMAKE_CURRENT_SOURCE_DIR}/asio_server.cpp")
  set(ASIO_SERVER_EXE_NAME asio_server)
  add_executable(${ASIO_SERVER_EXE_NAME} ${SERVER_SRC_FILES})
  target_link_libraries(${ASIO_SERVER_EXE_NAME} Boost::boost)
endif()
