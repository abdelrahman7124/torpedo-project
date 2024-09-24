from PyQt5 import QtCore, QtGui, QtWidgets
import rclpy
from std_msgs.msg import UInt8
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QShortcut, QLabel, QHBoxLayout, QMainWindow
from PyQt5.Qt import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
import sys
from PyQt5 import uic
import cv2

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("Tm1GUI.ui", self)
        self.show()

        self.cameraVideo= self.findChild(QLabel, "Live_camera_videoLable")
        self.startVideoStream()

    def startVideoStream(self):
        ip_camera_url = "http://192.168.1.22:8080/video"
        self.capture = cv2.VideoCapture(ip_camera_url)
        
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateFrame)
        self.timer.start(30)

  
    def updateFrame(self):

        ret, frame = self.capture.read()
        if ret:
            # Convert the frame to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Get the image size
            height, width, channels = frame.shape
            bytes_per_line = channels * width

            # Convert to QImage
            qImg = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)

            # Convert QImage to QPixmap
            pixmap = QPixmap.fromImage(qImg)

            # Scale the pixmap to fit the QLabel while keeping the aspect ratio
            scaled_pixmap = pixmap.scaled(self.cameraVideo.width(), self.cameraVideo.height(), Qt.KeepAspectRatio)

            # Set the scaled QPixmap into the QLabel
            self.cameraVideo.setPixmap(scaled_pixmap)
        else:
            print("Failed to capture video frame")


    def closeEvent(self, event):
        # Release the video capture on closing the window
        self.capture.release()
        event.accept()


app = QApplication(sys.argv)
window = UI()
window.show()
app.exec_()