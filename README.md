### Create a catkin package :
# catkin_create_pkg <package_name> [depend1] [depend2] [depend3] 

### Making the Python file executable in cmakelists example :
#   catkin_install_python(PROGRAMS src/pub_sub_basics/talker.py
#    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
#    )

### Custom message adding in cmake lists example :
#    Generate messages in the 'msg' folder
#    add_message_files(
#    FILES
#    IOTSensor.msg 
#    )

#  Add "message_runtime" in catkin packages
# 