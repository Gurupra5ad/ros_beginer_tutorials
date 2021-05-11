# <h1 align="center"> ROS Basic Tutorials </h1>
## <h2 align="left"> Linux-ROS Commands </h2>

-   **roscd** - To switch to the main ros directory
-   **roscd** [package_name] - To switch to the specific package inside the ros directory
-   **roscore** -  To run the main ros server
-   **rosnode list** - To check the list of nodes that are running 
-   **rostopic list** - To check the list of topics that are running 
-   **rosnode info [node_name]** - To check all the details about the selected node
-   **rostopic info [topic_name]** - To check all the details about the selected topic
-   **rosmsg show [msg_name]** - To check all the details about the particular message that is being sent via topics
-   **rosservice list** - To check the list of services that are running on
-   **rosservice info [service_name]** - To check all the details about the service that is selected
-   **rossrv info [service_name]** - To check all the details about the service that is selected
-   **rosservice call [service_name] [arguments]** - To call the particular service on a running node
## <h2 align="left"> ROS basic commands and CMake lists commands </h2>

#### Create a catkin package :
-      catkin_create_pkg <package_name> [depend1] [depend2] [depend3] 

-----------------------------------------------------------------------------------------------------------------------------------
#### Making the Python file executable in cmakelists example :
-      catkin_install_python(PROGRAMS src/pub_sub_basics/talker.py
       DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
       )

-----------------------------------------------------------------------------------------------------------------------------------

#### Custom message adding in cmake lists example :
-       Generate messages in the 'msg' folder
        add_message_files(
        FILES
        IOTSensor.msg 
        )

-   /Add "message_runtime" in catkin packages
 
 -----------------------------------------------------------------------------------------------------------------------------------
#### Custom service adding in cmake lists example :
-      add_service_files(
       FILES
       AddTwoInts.srv
       )

-   /Check for message generation and message runtime in package.xml then add the service in srv folder 

-----------------------------------------------------------------------------------------------------------------------------------
