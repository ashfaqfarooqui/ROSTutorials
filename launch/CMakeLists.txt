cmake_minimum_required(VERSION 2.8.3)
project(beginner_tutorials_launch)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED)



###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES ur_bringup
#  CATKIN_DEPENDS tf2_ros ur_description ur_driver
#  DEPENDS system_lib
)



install(FILES turtle.launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

