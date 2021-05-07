import rospy
from geometry_msgs.msg import Twist

def move():
    speed_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('move', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = 2.0
        twist.linear.y = 5.0
        twist.linear.z = 3.0
        twist.angular.x = 2.0
        twist.angular.y = 1.0
        twist.angular.z = 0.0
        speed_pub.publish(twist)
        rate.sleep()
    
if __name__ == "__main__":
    try:
        move()
    except rospy.ROSInterruptException:
        pass