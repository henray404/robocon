import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math


class TurtleMover(Node):
    def __init__(self):
        super().__init__('turtle_mover')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        time.sleep(1)

    def move_forward(self, speed, duration):
        twist = Twist()
        twist.linear.x = float(speed)
        self.publisher.publish(twist)
        time.sleep(duration)
        self.stop()

    def rotate_by_angle(self, angle_degrees, angular_speed):
        angle_radians = math.radians(angle_degrees)
        duration = angle_radians / angular_speed

        twist = Twist()
        twist.angular.z = float(
            angular_speed) if angle_degrees > 0 else -float(angular_speed)

        self.publisher.publish(twist)
        time.sleep(duration)
        self.stop()

    def stop(self):
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.publisher.publish(twist)


def main(args=None):
    rclpy.init(args=args)
    node = TurtleMover()

    def move_270():
        node.rotate_by_angle(angle_degrees=90, angular_speed=1.5)
        node.rotate_by_angle(angle_degrees=90, angular_speed=1.5)
        node.rotate_by_angle(angle_degrees=90, angular_speed=1.5)

    def move_180():
        node.rotate_by_angle(angle_degrees=90, angular_speed=1.5)
        node.rotate_by_angle(angle_degrees=90, angular_speed=1.5)

    def move_90():

        node.rotate_by_angle(angle_degrees=90, angular_speed=1.5)

    node.rotate_by_angle(angle_degrees=45, angular_speed=1.5)
    """ 1 """
    node.move_forward(speed=2.0, duration=1.0)
    move_90()
    node.rotate_by_angle(angle_degrees=20, angular_speed=1.5)
    """ 2 """
    node.move_forward(speed=2.5, duration=1.0)
    move_270()
    node.rotate_by_angle(angle_degrees=40, angular_speed=1.5)
    """ 3 """
    node.move_forward(speed=1.0, duration=1.0)
    move_180()
    node.rotate_by_angle(angle_degrees=70, angular_speed=1.5)
    """ 4 """
    node.move_forward(speed=3.5, duration=1.0)

    node.rotate_by_angle(angle_degrees=40, angular_speed=1.5)
    move_270()
    """ 5 """
    node.move_forward(speed=1.0, duration=1.0)
    move_270()

    node.rotate_by_angle(angle_degrees=60, angular_speed=1.5)
    """ 6 """

    node.move_forward(speed=1.0, duration=1.0)
    move_90()

    node.rotate_by_angle(angle_degrees=20, angular_speed=1.5)
    """ 7 """
    node.move_forward(speed=0.7, duration=1.0)
    move_270()
    node.rotate_by_angle(angle_degrees=35, angular_speed=1.5)
    """ 8 """
    node.move_forward(speed=1.0, duration=1.0)
    move_180()
    node.rotate_by_angle(angle_degrees=75, angular_speed=1.5)
    """ 9 """
    node.move_forward(speed=1.4, duration=1.0)

    node.rotate_by_angle(angle_degrees=70, angular_speed=1.5)
    """ 10 """
    node.move_forward(speed=1.1, duration=1.0)
    move_180()
    node.rotate_by_angle(angle_degrees=55, angular_speed=1.5)
    """ 11 """
    node.move_forward(speed=2.8, duration=1.0)
    node.rotate_by_angle(angle_degrees=65, angular_speed=1.5)
    """ 12 """
    node.move_forward(speed=1.0, duration=1.0)
    move_90()
    node.rotate_by_angle(angle_degrees=30, angular_speed=1.5)

    """ 13 """
    node.move_forward(speed=4.0, duration=1.0)
    move_90()
    node.rotate_by_angle(angle_degrees=35, angular_speed=1.5)
    """ 14 """

    node.move_forward(speed=1.0, duration=1.0)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
