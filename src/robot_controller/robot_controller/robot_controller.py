#!/usr/bin/env python

import rclpy
from std_msgs.msg import Float32
from rclpy.node import Node

class robot(Node):
    def __init__(self):
        super().__init__('movement')
        self.motor_left_pub = self.create_publisher(Float32, 'motor.left.speed', 10)
        self.motor_right_pub = self.create_publisher(Float32, 'motor.right.speed', 10)



        self.left_motor_speed = 0.0
        self.right_motor_speed = 0.0

        self.speed_left_sub = self.create_subscription(Float32, 'motor_left_speed_pid', self.left_motor_speed_callback, 10)
        self.speed_right_sub = self.create_subscription(Float32, 'motor.right.speed_pid', self.right_motor_speed_callback, 10)

    def left_motor_speed_callback(self, msg):
        self.speed_left = msg.data
    
    def right_motor_speed_callback(self, msg):
        self.speed_right = msg.data
    
    def move_forward(self):
        self.left_motor_speed.data = self.speed_left
        self.right_motor_speed.data = self.speed_right
        self.publish_motor_speeds()

    def move_backward(self):
        self.left_motor_speed.data = -self.speed_left
        self.right_motor_speed = -self.speed_right
        self.publish_motor_speeds()

    def move_left(self):
        self.left_motor_speed.data = -self.speed_left
        self.right_motor_speed.data = self.speed_right
        self.publish_motor_speeds()

    def move_right(self):
        self.left_motor_speed.data = self.speed_left
        self.right_motor_speed.data = -self.speed_right
        self.publish_motor_speeds()
    def stop(self):
        self.left_motor_speed.data = 0
        self.right_motor_speed.data = 0
        self.publish_motor_speeds()

    def publish_motor_speeds(self):
        self.motor_left_pub.publish(self.left_motor_speed)
        self.motor_right_pub.publish(self.right_motor_speed)



if __name__ == '__main__':
    try:
        Robot = robot()
        rclpy.spin()
    except rclpy.ROSInterruptException:
        pass
