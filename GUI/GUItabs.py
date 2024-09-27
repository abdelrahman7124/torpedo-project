from PyQt5 import QtCore, QtGui, QtWidgets
import rclpy
from std_msgs.msg import UInt8
from PyQt5.QtWidgets import QApplication, QWidget, QShortcut, QLabel, QHBoxLayout, QMainWindow, QAction, QTextEdit, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer,QThread, pyqtSignal
import sys
from PyQt5 import uic
import cv2
from LineFollower import process_frame 
from tryed import process_shape_detection



circle_count = 0
square_count = 0
triangle_count = 0
Red_count = 0
Green_count = 0
Blue_count = 0
Yellow_count = 0
White_count = 0
Black_count = 0
Station_Shape=""
Cuurent_Shape=""


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("GUI_tabs.ui", self)
        self.show()

        # Find the QLabel objects for live video and grayscale video
        self.cameraVideo = self.findChild(QLabel, "Live_camera_videoLable")
        self.cameraVideoimg_pross = self.findChild(QLabel, "Live_camera_videoLable2")  # For grayscale video

        self.frameLogs_Task1 = self.findChild(QTextEdit, "textEdit_LogsTask1")  
        self.frameLogs_Task2 = self.findChild(QTextEdit, "textEdit_LogsTask2")  


        self.detectShapeButton = self.findChild(QPushButton, "detectShapeButton")
        self.detectShapeButton.clicked.connect(self.detectShapes)  # Connect button to shape detection

        self.Show_res_task2_bouns_push = self.findChild(QPushButton, "Show_res_task2_bouns_push")
        self.Show_res_task2_bouns_push.clicked.connect(self.showTask2bouns)



        self.Set_st_task2_push = self.findChild(QPushButton, "Set_st_task2_push")
        self.Set_st_task2_push.clicked.connect(self.SetStation_Shape)

        self.Match_st_task2_push = self.findChild(QPushButton, "Match_st_task2_push")
        self.Match_st_task2_push.clicked.connect(self.CheckStation_Shape)


        self.cameraVideoimg_pross_Metal = self.findChild(QLabel, "Live_camera_videoLable2_Metal")  # For grayscale video




        # Start the video stream
        self.startVideoStream()

    def startVideoStream(self):
        ip_camera_url = "http://192.168.1.4:8080/video"
        self.capture = cv2.VideoCapture(ip_camera_url)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateFrame)
        self.timer.start(15)

    def updateFrame(self):
        ret, frame = self.capture.read()
        if ret:
            # Send the frame to the image_processing function
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            processed_frame, control_signal = process_frame(frame)
            
            # Display the control signal in the console (optional)
            #print(control_signal)
            self.appendLog(f"Control Signal: {control_signal}", self.frameLogs_Task1)

            self.displayFrameInLabel(processed_frame, self.cameraVideoimg_pross)
            # Convert the original frame to RGB

            # Update the original video label (self.cameraVideo)
            self.displayFrameInLabel(frame_rgb, self.cameraVideo)

        else:
            print("Failed to capture video frame")

    def displayFrameInLabel(self, frame, label):
        height, width, channels = frame.shape
        bytes_per_line = channels * width
        qImg = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        scaled_pixmap = pixmap.scaled(label.width(), label.height(), Qt.KeepAspectRatio)
        label.setPixmap(scaled_pixmap)




    def showTask2bouns(self):
        self.appendLog(
                "----------Shapes------------\n"
                f"Number of Circles: {circle_count},\n"
                f"Number of Squares: {square_count},\n"
                f"Number of Triangles: {triangle_count}\n"
                "----------Colors----------------\n",
                f"Number of Red: {Red_count},\n"
                f"Number of Green: {Green_count},\n"
                f"Number of Blue: {Blue_count},\n"
                f"Number of Yellow: {Yellow_count},\n"
                f"Number of White: {White_count},\n"
                f"Number of Black: {Black_count}\n",
                "--------------------------------\n",
                self.frameLogs_Task2)
        
    def SetStation_Shape(self):
        global Station_Shape, Cuurent_Shape
        Station_Shape= Cuurent_Shape


    def CheckStation_Shape(self):
        global Station_Shape, Cuurent_Shape
        if Station_Shape == Cuurent_Shape:
            #print("The current shape is the station shape")
            self.appendLog("Find Home! -- The current shape is the station shape", self.frameLogs_Task2)
        else:
            #print("The current shape is not the station shape")
            self.appendLog("Not Home! -- The current shape is not the station shape", self.frameLogs_Task2)

    def detectShapes(self):
        global circle_count, square_count, triangle_count ,Cuurent_Shape  
        global Red_count, Green_count, Blue_count, Yellow_count, White_count, Black_count
        ret, frame = self.capture.read()
        if ret:
            processed_frame, shape_count, shape_names ,shapes_color = process_shape_detection(frame)
            # Display the processed frame
            frame_rgb = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
            self.displayFrameInLabel(frame_rgb, self.cameraVideoimg_pross_Metal)

            shapes_with_colors = [f"{color} {shape}" for shape, color in zip(shape_names, shapes_color)]
        
        # Log the detected shapes and their count
            print(f"Detected {shape_count} shapes: {', '.join(shapes_with_colors)}")
            self.appendLog(f"Detected {shape_count} shapes: {', '.join(shapes_with_colors)}", self.frameLogs_Task2)

            """print(f"Detected {shape_count} shapes: {', '.join(shape_names)}")
            self.appendLog(f"Detected {shape_count} shapes: {', '.join(shape_names)}", self.frameLogs_Task2)
            """
        if shape_count == 1:
            Cuurent_Shape= shape_names[0]
            for shape, color in zip(shape_names, shapes_color):
                # Count shapes
                if shape == "circle":
                    circle_count += 1
                elif shape == "sq":
                    square_count += 1
                elif shape == "triangle":
                    triangle_count += 1

                # Count colors
                if color == "Red":
                    Red_count += 1
                elif color == "Green":
                    Green_count += 1
                elif color == "Blue":
                    Blue_count += 1
                elif color == "Yellow":
                    Yellow_count += 1
                elif color == "White":
                    White_count += 1
                elif color == "Black":
                    Black_count += 1
            

            
            print(f"Number of Circles: {circle_count}, "
                  f"Number of Squares: {square_count}, "
                  f"Number of Triangles: {triangle_count}")
            
            print(f"Number of Red: {Red_count}, "
                  f"Number of Green: {Green_count}, "
                  f"Number of Blue: {Blue_count}, "
                  f"Number of Yellow: {Yellow_count}, "
                  f"Number of White: {White_count}, "
                  f"Number of Black: {Black_count}")
            


    def appendLog(self, log_text, log_frame):
        if log_frame:  # Check if the widget is found
            log_frame.append(log_text)  # Append log to QTextEdit
        else:
            print("Log frame not found")


            
    def closeEvent(self, event):
        self.capture.release()
        event.accept()


app = QApplication(sys.argv)
window = UI()
window.show()
app.exec_()