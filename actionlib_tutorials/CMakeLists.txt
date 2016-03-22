cmake_minimum_required(VERSION 2.8.3)
project(action_tutorial)

## Find catkin dependencies
find_package(catkin REQUIRED COMPONENTS actionlib message_generation)

## Find Boost
find_package(Boost REQUIRED COMPONENTS system thread)

## Add actions
add_action_files(DIRECTORY action FILES Fibonacci.action )

## Generate messages
generate_messages(DEPENDENCIES std_msgs actionlib_msgs)

## Define catkin exports
catkin_package(
  CATKIN_DEPENDS roscpp actionlib
  DEPENDS Boost
)

## Install scripts and executables
install(PROGRAMS
  scripts/fibonacci_client.py
  scripts/fibonacci_server.py
  scripts/gen_numbers.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
