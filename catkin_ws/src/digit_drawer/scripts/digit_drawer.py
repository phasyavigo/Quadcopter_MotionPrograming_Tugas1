import rospy, math, time
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
from turtlesim.srv import SetPen, TeleportAbsolute

current_digit = None

def cb_digit(msg):
    global current_digit
    current_digit = msg.data

def move_turtle(pub, linear=0, angular=0, duration=1.0):
    twist = Twist()
    twist.linear.x = linear
    twist.angular.z = angular
    
    rate = rospy.Rate(50)
    start_time = rospy.Time.now()
    
    while (rospy.Time.now() - start_time).to_sec() < duration and not rospy.is_shutdown():
        pub.publish(twist)
        rate.sleep()
    
    twist.linear.x = 0
    twist.angular.z = 0
    pub.publish(twist)

def move_forward(pub, distance, speed=1.0):
    duration = distance / speed
    move_turtle(pub, linear=speed, angular=0, duration=duration)

def turn_degrees(pub, degrees, angular_speed=90):
    radians = math.radians(degrees)
    duration = abs(radians) / math.radians(angular_speed)
    angular_vel = math.radians(angular_speed) if degrees > 0 else -math.radians(angular_speed)
    move_turtle(pub, linear=0, angular=angular_vel, duration=duration)

def pen_up(pen_service):
    pen_service(0, 0, 0, 0, 1)

def pen_down(pen_service, r=255, g=0, b=0, width=3):
    pen_service(r, g, b, width, 0)

def draw_0(pub, pen_service):
    pen_down(pen_service)
    move_forward(pub, 2.0)
    turn_degrees(pub, 90)
    move_forward(pub, 3.0)
    turn_degrees(pub, 90)
    move_forward(pub, 2.0)
    turn_degrees(pub, 90)
    move_forward(pub, 3.0)
    pen_up(pen_service)

def draw_1(pub, pen_service):
    pen_up(pen_service) 
    move_forward(pub, 2.0)
    pen_down(pen_service)
    turn_degrees(pub, 90)
    move_forward(pub, 3.0)
    turn_degrees(pub, 135)
    move_forward(pub, 1)
    pen_up(pen_service)

def draw_2(pub, pen_service):
    pen_down(pen_service)
    turn_degrees(pub, 180)
    move_forward(pub, 2.0)
    turn_degrees(pub, -90)
    move_forward(pub, 1.5)
    turn_degrees(pub, -90)
    move_forward(pub, 2.0)
    turn_degrees(pub, 90)
    move_forward(pub, 1.5)
    turn_degrees(pub, 90)
    move_forward(pub, 2.0)
    pen_up(pen_service)

def draw_3(pub, pen_service):
    pen_down(pen_service)
    move_forward(pub, 2.0)
    turn_degrees(pub, 90)
    move_forward(pub, 1.5)
    turn_degrees(pub, 90)
    move_forward(pub, 1.5)
    turn_degrees(pub, 180)
    move_forward(pub, 1.5)
    turn_degrees(pub, 90)
    move_forward(pub, 1.5)
    turn_degrees(pub, 90)
    move_forward(pub, 2.0)
    pen_up(pen_service)

def draw_4(pub, pen_service):
    pen_down(pen_service)
    turn_degrees(pub, 90)
    move_forward(pub, 3)
    turn_degrees(pub, 180)
    move_forward(pub, 1.5)
    turn_degrees(pub, -90)
    move_forward(pub, 2.0)
    turn_degrees(pub, -90)
    move_forward(pub, 1.5)
    pen_up(pen_service)

def draw_5(pub, pen_service):
    pen_down(pen_service)
    move_forward(pub, 2.0)
    turn_degrees(pub, 90)
    move_forward(pub, 1.5)
    turn_degrees(pub, 90)
    move_forward(pub, 2.0)
    turn_degrees(pub, -90)
    move_forward(pub, 1.5)
    turn_degrees(pub, -90)
    move_forward(pub, 2.0)
    pen_up(pen_service)

def draw_6(pub, pen_service):
    pen_down(pen_service)
    move_forward(pub, 2.0)
    turn_degrees(pub, 90)
    move_forward(pub, 1.5)
    turn_degrees(pub, 90)
    move_forward(pub, 2.0)
    turn_degrees(pub, 90)
    move_forward(pub, 1.5)
    turn_degrees(pub, 180)
    move_forward(pub, 3.0)
    turn_degrees(pub, -90)
    move_forward(pub, 2.0)
    pen_up(pen_service)

def draw_7(pub, pen_service):
    pen_down(pen_service)
    move_forward(pub, 2.0)
    turn_degrees(pub, -135)
    move_forward(pub, 3.0)
    pen_up(pen_service)

def draw_8(pub, pen_service):
    pen_down(pen_service)
    move_forward(pub, 2.0)
    turn_degrees(pub, 90)
    move_forward(pub, 1.5)
    turn_degrees(pub, 90)
    move_forward(pub, 2.0)
    turn_degrees(pub, 90)
    move_forward(pub, 3.0)
    turn_degrees(pub, 90)
    move_forward(pub, 2.0)
    turn_degrees(pub, 90)
    move_forward(pub, 1.5)
    turn_degrees(pub, 90)
    move_forward(pub, 2.0)
    pen_up(pen_service)

def draw_9(pub, pen_service):
    pen_down(pen_service)
    move_forward(pub, 2.0)
    turn_degrees(pub, 90)
    move_forward(pub, 1.5)
    turn_degrees(pub, 90)
    move_forward(pub, 2.0)
    turn_degrees(pub, 90)
    move_forward(pub, 1.5)
    turn_degrees(pub, 90)
    move_forward(pub, 2.0)
    turn_degrees(pub, -90)
    move_forward(pub, 1.5)
    turn_degrees(pub, -90)
    move_forward(pub, 2.0)
    pen_up(pen_service)

digit_functions = {
    '0': draw_0,
    '1': draw_1, 
    '2': draw_2,
    '3': draw_3,
    '4': draw_4,
    '5': draw_5,
    '6': draw_6,
    '7': draw_7,
    '8': draw_8,
    '9': draw_9
}

def draw_digit(pub, pen_service, digit):
    if digit in digit_functions:
        print(f"Drawing digit: {digit}")
        digit_functions[digit](pub, pen_service)
        time.sleep(0.5)
    else:
        print(f"Digit {digit} not supported")

if __name__ == '__main__':
    rospy.init_node('digit_drawer')
    
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/digit_input', String, cb_digit)
    
    rospy.wait_for_service('/clear')
    rospy.wait_for_service('/turtle1/teleport_absolute')
    rospy.wait_for_service('/turtle1/set_pen')
    
    clear = rospy.ServiceProxy('/clear', Empty)
    teleport = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
    pen = rospy.ServiceProxy('/turtle1/set_pen', SetPen)
    
    print("Digit drawer ready. Send digit via: rostopic pub /digit_input std_msgs/String \"data: 'X'\"")
    
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        if current_digit is not None:
            digit = current_digit
            current_digit = None
            
            clear()
            time.sleep(0.3)
            
            start_x, start_y = 5.5, 5.5
            teleport(start_x, start_y, 0)
            time.sleep(0.5)
            
            draw_digit(pub, pen, digit)
            
            print(f"Finished drawing: {digit}")
            
        rate.sleep()