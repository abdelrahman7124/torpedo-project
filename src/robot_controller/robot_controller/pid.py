#!/usr/bin/env python

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from std_msgs.msg import Float32
import tf_transformations as tft

class PIDController(Node):
    def __init__(self):
        super().__init__('pid_controller')

        self.Kp = 1.0
        self.Ki = 0.05
        self.Kd = 0.01
        self.setpoint = 0.0 
        self.integral = 0.0
        self.last_error = 0.0
        self.last_time = self.get_clock().now().nanoseconds / 1e9

        self.base_speed = 100.0

        self.sub_imu = self.create_subscription(Imu, "imu_data", self.imu_callback, 10)

        self.motor_left_pub = self.create_publisher(Float32, 'motor_left_speed_pid', 10)
        self.motor_right_pub = self.create_publisher(Float32, 'motor_right_speed_pid', 10)

        self.current_angle = 0.0

    def imu_callback(self, data):
        orientation = data.orientation
        self.current_angle = self.get_pitch_from_imu(orientation)


    def get_pitch_from_imu(self, orientation):
        (roll, pitch, yaw) = tft.euler_from_quaternion([orientation.x, orientation.y, orientation.z, orientation.w])
        return pitch * 180.0 / 3.14159  

    def compute_pid(self):
        current_time = self.get_clock().now().nanoseconds / 1e9
        dt = current_time - self.last_time

        # PID error calculations
        error = self.setpoint - self.current_angle
        self.integral += error * dt
        if dt > 0:
            derivative = (error - self.last_error) / dt 
        else:
            derivative = 0.0

        # PID output
        output = (self.Kp * error) + (self.Ki * self.integral) + (self.Kd * derivative)

        self.last_error = error
        self.last_time = current_time

        return output

    def control_motors(self):
        pid_output = self.compute_pid()

        left_motor_speed = self.base_speed - pid_output 
        right_motor_speed = self.base_speed + pid_output

        left_motor_speed = max(min(left_motor_speed, 255), -255)
        right_motor_speed = max(min(right_motor_speed, 255), -255)

        self.motor_left_pub.publish(left_motor_speed)
        self.motor_right_pub.publish(right_motor_speed)

    def run(self):
        rate = self.create_rate(50)  
        while rclpy.ok():
            self.control_motors()
            rate.sleep()

def main(args=None):
    rclpy.init(args=args)
    try:
        pid_controller = PIDController()
        rclpy.spin(pid_controller)
    except KeyboardInterrupt:
        pass
    finally:
        pid_controller.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
