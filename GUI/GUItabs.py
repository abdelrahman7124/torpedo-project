from PyQt5 import QtCore, QtGui, QtWidgets
import rclpy
from std_msgs.msg import UInt8
from PyQt5.QtWidgets import QApplication, QWidget, QShortcut, QLabel, QHBoxLayout, QMainWindow, QAction, QTextEdit
from PyQt5.Qt import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
import sys
from PyQt5 import uic
import cv2
from LineFollower import process_frame 

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("GUI_tabs.ui", self)
        self.show()

        # Find the QLabel objects for live video and grayscale video
        self.cameraVideo = self.findChild(QLabel, "Live_camera_videoLable")
        self.cameraVideoimg_pross = self.findChild(QLabel, "Live_camera_videoLable2")  # For grayscale video

        self.frameLogs_Task1 = self.findChild(QTextEdit, "textEdit_LogsTask1")  # Assuming it's a QTextEdit

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
            print(control_signal)
            self.appendLog(f"Control Signal: {control_signal}")


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


    def appendLog(self, log_text):
        if self.frameLogs_Task1:  # Check if the widget is found
            self.frameLogs_Task1.append(log_text)  # Append log to QTextEdit
        else:
            print("Log frame (frameLogs_Task1) not found")

            
    def closeEvent(self, event):
        self.capture.release()
        event.accept()


app = QApplication(sys.argv)
window = UI()
window.show()
app.exec_()