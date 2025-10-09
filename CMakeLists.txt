cmake_minimum_required(VERSION 3.14)

include(cmake/prelude.cmake)

project(
    cpp-high-performance
    VERSION 0.1.0
    DESCRIPTION "Short description"
    HOMEPAGE_URL " https://github.com/haha454/cpp-high-performance"
    LANGUAGES CXX
)

include(cmake/project-is-top-level.cmake)
include(cmake/variables.cmake)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED YES)
set(CMAKE_CXX_EXTENSIONS NO)

find_package(Boost CONFIG REQUIRED)
find_package(GTest CONFIG REQUIRED)
include(GoogleTest)
find_package(benchmark CONFIG REQUIRED)

enable_testing()
add_subdirectory("Chapter01")
add_subdirectory("Chapter02")
add_subdirectory("Chapter03")
add_subdirectory("Chapter04")
add_subdirectory("Chapter05")
add_subdirectory("Chapter06")
add_subdirectory("Chapter07")
add_subdirectory("Chapter08")
add_subdirectory("Chapter09")
add_subdirectory("Chapter10")
add_subdirectory("Chapter11")
add_subdirectory("Chapter12")
add_subdirectory("Chapter13")
add_subdirectory("Chapter14")

# ---- Developer mode ----

if(NOT cpp-high-performance_DEVELOPER_MODE)
  return()
elseif(NOT PROJECT_IS_TOP_LEVEL)
  message(
      AUTHOR_WARNING
      "Developer mode is intended for developers of cpp-high-performance"
  )
endif()

include(cmake/dev-mode.cmake)
