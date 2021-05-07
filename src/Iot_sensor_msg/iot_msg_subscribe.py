import rospy
from beginer_tutorials.msg import IOTSensor

def iot_sensor_callback(iot_sensor_message):
    rospy.loginfo("new IoT data recieved: (%d, %s, %.2f, %.2f)",
                iot_sensor_message.id, iot_sensor_message.name, iot_sensor_message.temperature, iot_sensor_message.humidity)

rospy.init_node('iot_sensor_subscriber_node', anonymous = True)
rospy.Subscriber('iot_sensor_topic',IOTSensor, iot_sensor_callback)
rospy.spin()

