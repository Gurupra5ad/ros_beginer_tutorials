# <h1 align="center"> ROS Basic Tutorials </h1>
## <h2 align="left"> Linux-ROS Commands </h2>

-   **roscd** - To switch to the main ros directory
-   **roscd [package_name]** - To switch to the specific package inside the ros directory
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
-   **roslaunch [package_name] [launch_file_name]** - We can add all the nodes that we need to run in a launch file and run the 
launch file instead of single nodes.
-   **rosrun usb_cam usb_cam_node _pixel_format:=yuyv** - To run the webcam in our laptop for ros related processes
-   **rosrun image_view image_view image:=/usb_cam/image_raw** - To open the image view tool to access our webcam window and to see  the output
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
#### Launch file syntax example :
-      <launch>
       <node name="turtlesim_node" pkg="turtlesim" type="turtlesim_node" output="screen"/>
       <node name="turtlesim_cleaner" pkg="beginer_tutorials" type="spiral.py" output="screen"/>
       </launch>
       
-----------------------------------------------------------------------------------------------------------------------------------
#### OpenCV with ROS:
-   /Install opencv and other tools.

-      sudo apt-get install ros-${distro_name}-opencv3
-      sudo apt-get install ros-${distro_name}-usb-cam
-      sudo apt-get install ros-${distro_name}-image-view

-   /Now all the ros-opencv programs will be able to run without errors
-   /See linux commands to run usb cam and image view
       
-----------------------------------------------------------------------------------------------------------------------------------
