cmake_minimum_required(VERSION 2.8.3)
project(tut_msgs)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS message_generation std_msgs actionlib_msgs)


## Generate messages in the 'msg' folder
# add_message_files(
#   FILES
# )

## Generate services in the 'srv' folder
 add_service_files(
   FILES
   shapeSelector.srv
 )

## Generate actions in the 'action' folder
#add_action_files(
 # DIRECTORY action
# FILES 
#)


## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   std_msgs


)

###################################
## catkin specific configuration ##
###################################
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES 
   CATKIN_DEPENDS 
   message_runtime 
   std_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########

#############
## Install ##
#############

#############
## Testing ##
#############