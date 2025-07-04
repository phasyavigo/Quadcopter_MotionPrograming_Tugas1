#!/usr/bin/env python3
import rospy, math, time
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
from turtlesim.srv import SetPen, TeleportAbsolute

input_digit = None
def cb_digit(msg):
    global input_digit
    input_digit = msg.data

def move(pub, linear=0, angular=0, duration=1.0):
    t = Twist(); t.linear.x = linear; t.angular.z = angular
    rate = rospy.Rate(10)
    for _ in range(int(duration * 10)):
        pub.publish(t); rate.sleep()

digit_paths = {
    '0': [('forward',1), ('turn', math.pi/2)]*4,
    '1': [('turn', -math.pi/2), ('forward',1)],
    '2': [('forward',1), ('turn', math.pi/2), ('forward',1), ('turn', math.pi/2),
          ('forward',1), ('turn', -math.pi/2), ('forward',1)],
    '3': [('forward',1), ('turn', math.pi/2), ('forward',1),
          ('turn', math.pi/2), ('forward',1)],
    '4': [('turn', -math.pi/2), ('forward',1), ('turn', math.pi/2),
          ('forward',1), ('turn',180), ('forward',2)],
    '5': [('forward',1), ('turn', math.pi/2), ('forward',1),
          ('turn', math.pi/2), ('forward',1), ('turn', math.pi/2), ('forward',1)],
    '6': [('forward',1), ('turn', math.pi/2), ('forward',1), ('turn', math.pi/2),
          ('forward',1), ('turn', math.pi/2), ('forward',0.5), ('turn', math.pi/2), ('forward',0.5)],
    '7': [('forward',1), ('turn', math.pi/2), ('forward',1)],
    '8': [('forward',1), ('turn', math.pi/2), ('forward',1), ('turn', math.pi/2),
          ('forward',1), ('turn', math.pi/2), ('forward',1), ('turn', math.pi/2), ('forward',1)],
    '9': [('forward',1), ('turn', math.pi/2), ('forward',1), ('turn', math.pi/2),
          ('forward',1), ('turn', math.pi/2), ('forward',1)],
}

def draw_digit(pub, d):
    for cmd, val in digit_paths[d]:
        if cmd == 'forward':
            move(pub, linear=1.0, angular=0, duration=val)
        else:
            move(pub, linear=0, angular=1.0 if val>0 else -1.0, duration=abs(val))

if __name__ == '__main__':
    rospy.init_node('digit_drawer')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
    rospy.Subscriber('/digit_input', String, cb_digit)
    rospy.wait_for_service('/clear'); rospy.wait_for_service('/turtle1/teleport_absolute')
    rospy.wait_for_service('/turtle1/set_pen')
    clear = rospy.ServiceProxy('/clear', Empty)
    teleport = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
    pen = rospy.ServiceProxy('/turtle1/set_pen', SetPen)
    rate = rospy.Rate(10)
    print("Digit drawer ready. Tunggu input angka dari node input.")
    while not rospy.is_shutdown():
        
        if input_digit:
            d = input_digit; input_digit = None
            if d not in digit_paths:
                print("Angka belum didukung:", d)
            else:
                pen(255,0,0,2,0)
                draw_digit(pub, d)
                clear()
                teleport(5.5, 5.5, 0)
                time.sleep(0.5)
        rate.sleep()
