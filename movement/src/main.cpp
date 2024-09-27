#include <Arduino.h>
#include <micro_ros_arduino.h>
#include <std_msgs/msg/float32.h>
#include <std_msgs/msg/string.h>


#define leftMotor 14         
#define rightMotor 15       
#define imu_sensor 8       

rcl_publisher_t publisher;   


std_msgs__msg__Float32 msg; 


rcl_subscription_t subscriber_right;
rcl_subscription_t subscriber_left;
rcl_subscription_t subscriber_direction;


std_msgs__msg__Float32 movement_msg_left;
std_msgs__msg__Float32 movement_msg_right;
std_msgs__msg__String movement_msg_direction;

float left_speed=0.0;
float right_speed=0.0;
string direction = "stop";

void setup() {
    pinMode(leftMotor, OUTPUT);   
    pinMode(rightMotor, OUTPUT);  
    pinMode(imu_sensor, INPUT);   
    set_microros_transports();  
    rcl_allocator_t allocator = rcl_get_default_allocator();  
    rclc_support_t support; 
    rclc_support_init(&support, 0, NULL, &allocator);  

    rcl_node_t node;  
    rclc_node_init_default(&node, "imu_data", "", &support);
    //publishers
    rclc_publisher_init_default(&publisher,&node,ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, msg, Float32),"imu_data");  

    //subscribers
    rclc_subscription_init_default(&subscriber_left, &node, ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, movement_msg_left, Float32), "motor_left_speed");
    rclc_subscription_init_default(&subscriber_right, &node, ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, movement_msg_right, Float32), "motor_right_speed");
    rclc_subscription_init_default(&subscriber_direction, &node, ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, movement_msg_direction, String), "motor_direction");

    rclc_subscription_set_callback(&subscriber_left, motor_left_speed_callback, NULL);
    rclc_subscription_set_callback(&subscriber_right, motor_right_speed_callback, NULL);
    rclc_subscription_set_callback(&subscriber_direction, motor_direction_callback, NULL);


    //sexcutor for the subscribers
    rclc_executor_t executor;
    rclc_executor_init(&executor, &support.context, 1, &allocator);
    rclc_executor_add_subscription(&executor, &subscriber_left, &movement_msg_left, NULL);
    rclc_executor_add_subscription(&executor, &subscriber_right, &movement_msg_right, NULL);
    rclc_executor_spin(&executor);

}

void motor_left_speed_callback(const void * msgin){
  movement_msg_left = *(const std_msgs__msg__Float32 *)msgin;
  left_speed = movement_msg_left.data;
}

void motor_right_speed_callback(const void * msgin){
  movement_msg_right = *(const std_msgs__msg__Float32 *)msgin;
  right_speed = movement_msg_right.data;
}

void motor_direction_callback(const void *msgin){
  movement_msg_direction = *(const std_msgs__msg__String *)msgin;
  direvtion = movement_msg_direction.data
}


void loop() {
  static unsigned long last_time = 0;
  unsigned long current_time = millis();
// publish the data for imu sensor every 1 second
  if (current_time - last_time >= 1000) {
    last_time = current_time;
    int sensor_value = digitalRead(imu_sensor);  
    msg.data = sensor_value;
    rcl_publish(&publisher, &msg, NULL); 
  }
  //move according to received speed and direction
  if(direction == "forward"){
    moveforward();
  }
  else if(direction == "backward"){
    movebackward();
  }
  else if(direction == "left"){
    turnleft();
  }
  else if(direction == "right"){
    turnright();
  }
  else if(direction == "stop"){
    stop();
  }

}


void moveforward(){
  digitalWrite(leftMotor, HIGH);
  digitalWrite(rightMotor, HIGH);
}

void movebackward(){
  digitalWrite(leftMotor, LOW);
  digitalWrite(rightMotor, LOW);
}

void turnleft(){
  digitalWrite(leftMotor, LOW);
  digitalWrite(rightMotor, HIGH);
}

void turnright(){
  digitalWrite(leftMotor, HIGH);
  digitalWrite(rightMotor, LOW);
}

void stop(){
  digitalWrite(leftMotor, LOW);
  digitalWrite(rightMotor, LOW);
}



