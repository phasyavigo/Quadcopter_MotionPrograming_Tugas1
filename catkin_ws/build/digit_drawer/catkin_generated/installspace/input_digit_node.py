#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node('digit_input_node')
    pub = rospy.Publisher('/digit_input', String, queue_size=1)
    rate = rospy.Rate(1)
    print("Node input aktif. Ketik angka 0–9 atau 'q' untuk keluar.")
    while not rospy.is_shutdown():
        try:
            d = raw_input("Masukkan angka: ")
        except:
            break
        if not d or d[0] == 'q':
            break
        pub.publish(d[0])
        rate.sleep()
