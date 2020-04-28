#!/usr/bin/env python
# license removed for brevity
import rospy, random
from std_msgs.msg import String

def talkers():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    while not rospy.is_shutdown():
        random_str = "Numero aleatorio => " + str(random.randint(0,1000))
        rospy.loginfo(random_str)
        pub.publish(random_str)
        rospy.sleep(5.)

if __name__ == '_main_':
    try:
        talkers()
    except rospy.ROSInterruptException:
        pass
