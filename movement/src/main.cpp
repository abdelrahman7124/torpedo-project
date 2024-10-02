#include <Arduino.h>
#include <micro_ros_platformio.h>


#include <rclc/rclc.h>
#include <rclc/executor.h>
#include <rcl/rcl.h>

#include <std_msgs/msg/float32.h>
#include <std_msgs/msg/string.h>
#include <string>


using namespace std;

const char *ssid = "wifi name";   // name to be changed
const char *password =  "password";  // password to be changed

#define leftMotor_neg 9
#define leftMotor_pos 8
#define rightMotor_neg 13
#define rightMotor_pos 12

rcl_publisher_t publisher;   


std_msgs__msg__Float32 msg; 


rcl_subscription_t subscriber_right;
rcl_subscription_t subscriber_left;
rcl_subscription_t subscriber_direction;


std_msgs__msg__Float32 movement_msg_left;
std_msgs__msg__Float32 movement_msg_right;
std_msgs__msg__String movement_msg_direction;

int left_speed=0;
int right_speed=0;
String direction = "stop";


  void moveforward(int left,int right);
  void movebackward(int left,int right);
  void turnleft(int left,int right);
  void turnright(int left,int right);
  void stop();
  void motor_left_speed_callback(const void * msgin);
  void motor_right_speed_callback(const void * msgin);
  void motor_direction_callback(const void *msgin);



void setup() {

    pinMode(leftMotor_neg, OUTPUT);
    pinMode(leftMotor_pos, OUTPUT);
    pinMode(rightMotor_neg, OUTPUT);
    pinMode(rightMotor_pos, OUTPUT);  

    rcl_allocator_t allocator = rcl_get_default_allocator();  
    rclc_support_t support; 
    rclc_support_init(&support, 0, NULL, &allocator);  

    rcl_node_t node;  
    rclc_node_init_default(&node, "data", "", &support);
    //publishers
    rclc_publisher_init_default(&publisher,&node,ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, msg, Float32),"imu_data");  

    //subscribers
    rclc_subscription_init_default(&subscriber_left, &node, ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, movement_msg_left, Float32), "motor_left_speed");
    rclc_subscription_init_default(&subscriber_right, &node, ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, movement_msg_right, Float32), "motor_right_speed");
    rclc_subscription_init_default(&subscriber_direction, &node, ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, movement_msg_direction, String), "motor_direction");

    rclc_executor_t executor;
    rclc_executor_init(&executor, &support.context, 3, &allocator);
    rclc_executor_add_subscription(&executor, &subscriber_left, &movement_msg_left, motor_left_speed_callback, ON_NEW_DATA);
    rclc_executor_add_subscription(&executor, &subscriber_right, &movement_msg_right, motor_right_speed_callback, ON_NEW_DATA);
    rclc_executor_add_subscription(&executor, &subscriber_direction, &movement_msg_direction, motor_direction_callback, ON_NEW_DATA);


}

void motor_left_speed_callback(const void * msgin){
  movement_msg_left = *(const std_msgs__msg__Float32 *)msgin;
  left_speed = (int)movement_msg_left.data;
}

void motor_right_speed_callback(const void * msgin){
  movement_msg_right = *(const std_msgs__msg__Float32 *)msgin;
  right_speed = (int)movement_msg_right.data;
}

void motor_direction_callback(const void *msgin){
  movement_msg_direction = *(const std_msgs__msg__String *)msgin;
  direction = (string)movement_msg_direction.data;
}



void loop() {
  if(direction == "forward"){
    moveforward(left_speed, right_speed);
  }
  else if(direction == "backward"){
    movebackward(left_speed, right_speed);
  }
  else if(direction == "left"){
    turnleft(left_speed, right_speed);
  }
  else if(direction == "right"){
    turnright(left_speed, right_speed);
  }
  else if(direction == "stop"){
    stop();
  }
}


void moveforward(int left,int right){
  analogWrite(leftMotor_neg, 0);
  analogWrite(leftMotor_pos, left);
  analogWrite(rightMotor_neg, 0);
  analogWrite(rightMotor_pos, right);
}

void movebackward(int left,int right){
  analogWrite(leftMotor_neg, left);
  analogWrite(leftMotor_pos, 0);
  analogWrite(rightMotor_neg, right);
  analogWrite(rightMotor_pos, 0);
}

void turnleft(int left,int right){
  analogWrite(leftMotor_neg, 0);
  analogWrite(leftMotor_pos, left/4);
  analogWrite(rightMotor_neg, 0);
  analogWrite(rightMotor_pos, right);
}

void turnright(int left,int right){
  analogWrite(leftMotor_neg, left);
  analogWrite(leftMotor_pos, 0);
  analogWrite(rightMotor_neg, right/4);
  analogWrite(rightMotor_pos, 0);
}

void stop(){
  analogWrite(leftMotor_neg, 0);
  analogWrite(leftMotor_pos, 0);
  analogWrite(rightMotor_neg, 0);
  analogWrite(rightMotor_pos, 0);
}
