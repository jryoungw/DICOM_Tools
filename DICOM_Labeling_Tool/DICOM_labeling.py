import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPainter, QPalette, QPixmap, qRgb
from PyQt5.QtCore import Qt
from PyQt5 import uic, QtGui
import pandas as pd
import csv
import cv2
import SimpleITK as sitk
import numpy as np
import os

class LabelingTool(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.labels = ["good", 'bad']
        self.image_column = 'filePath'
        self.final_column = "RelabeledColumn"


        self.press_num = 0
        self.final_labels = []
        self.image_names = []
        self.gray_color_table = [qRgb(i, i, i) for i in range(256)]
        self.opened = False
        self.qtkeys = []
        for i in range(len(self.labels)):
            exec(f"self.qtkeys.append(Qt.Key_{i+1})")
        self.setupUI()


    def setupUI(self):
        self.imageLabel = QLabel()
        self.imageLabel.setBackgroundRole(QPalette.Base)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)

        self.scrollArea = QScrollArea()
        self.scrollArea.setBackgroundRole(QPalette.Dark)
        self.scrollArea.setWidget(self.imageLabel)
        self.setCentralWidget(self.scrollArea)
        
        self.createActions()
        
        self.setWindowTitle("Image Viewer")
        self.resize(400, 400)
        if self.opened:
            image = cv2.imread(self.images[self.press_num])
            self.openImage(image=self.toQImage(image))

        self.setGeometry(200, 200, 1000, 1000)
        self.setWindowTitle("Classification Labeling Tool")
        self.openfolder = QPushButton(self)
        self.openfolder.move(20, 950)
        self.openfolder.setText('Open CSV')
        self.openfolder.clicked.connect(self.openFolder)

        self.view = QPushButton(self)
        self.view.move(880, 850)
        self.view.setText('View Image')
        self.view.clicked.connect(self.viewImage)
        
        self.saveresult = QPushButton(self)
        self.saveresult.move(880, 950)
        self.saveresult.setShortcut("Ctrl+S")
        self.saveresult.setText('Save Result')
        self.saveresult.clicked.connect(self.saveResult)

        self.backward = QPushButton(self)
        self.backward.move(880, 750)
        self.backward.setText('Backward')
        self.backward.clicked.connect(self.backwardFunction)


        for i in range(len(self.labels)):
            self.addButton(i)

        layout = QVBoxLayout()
        layout.addWidget(self.openfolder)
        self.setLayout(layout)

    def backwardFunction(self):
        self.final_labels.pop(self.press_num-1)
        self.image_names.pop(self.press_num-1)
        self.press_num -= 1
        self.saveResult()
        self.viewImage()


    def addButton(self, i):
        exec(f"self.{self.labels[i]} = QPushButton(self)")
        exec(f"self.{self.labels[i]}.move(200 + 100*{i}, 950)")
        exec(f"self.{self.labels[i]}.resize(100, 40)")
        exec(f"self.{self.labels[i]}.setText('Press {i+1} to \\nadd {self.labels[i]}')")
        # exec(f"self.{self.labels[i]}.clicked.connect(self.buttonClicked)")
    
    def buttonClicked(self):
        sender = self.sender()
        for l in self.labels:
            if l == sender.text():
                self.final_labels.append(l)
    

    def openFolder(self):
        fname = QFileDialog.getOpenFileName(self)[0]
        self.fname = fname
        self.savename = self.fname[:-4] + '_relabeled.csv'
        self.df = pd.read_csv(self.fname)
        self.columns = list(self.df.columns)
        self.images = self.df[self.image_column].tolist()
        self.opened = True
        

    def keyPressEvent(self, e):
        rightButton = False
        if self.press_num < len(self.df):
                
            for i in range(len(self.labels)):
                if e.key() == self.qtkeys[i]:
                    self.final_labels.append(self.labels[i])
                    self.image_names.append(self.images[self.press_num])
                    self.press_num += 1
                    rightButton = True
            if not rightButton:
                self.final_labels.append('Indeterminate')
                self.image_names.append(self.images[self.press_num])
                self.press_num += 1
            self.saveResult()
            self.viewImage()

    def updateActions(self):
        self.normalSizeAct.setEnabled(not self.fitToWindowAct.isChecked())

    def saveResult(self):
        final_df = pd.DataFrame({self.image_column: self.image_names, \
                                self.final_column:self.final_labels})
        final_df.to_csv(self.savename)

    def createActions(self):
        self.normalSizeAct = QAction("&Normal Size", self, shortcut="Ctrl+N",
                enabled=False, triggered=self.normalSize)

        self.fitToWindowAct = QAction("&Fit to Window", self, enabled=False,
                checkable=True, shortcut="Ctrl+F", triggered=self.fitToWindow)

    def normalSize(self):
        self.imageLabel.adjustSize()

    def fitToWindow(self):
        fitToWindow = self.fitToWindowAct.isChecked()
        self.scrollArea.setWidgetResizable(fitToWindow)
        if not fitToWindow:
            self.normalSize()
        self.updateActions()

    def viewImage(self):
        self.openImage()

    def writetext(self, canvas, filename):
        # File name
        canvas = cv2.putText(canvas, filename, (0, 25), cv2.FONT_HERSHEY_PLAIN, fontScale=1.5, color=(255,255,255), lineType=4, thickness=4)
        canvas = cv2.putText(canvas, filename, (0, 25), cv2.FONT_HERSHEY_PLAIN, fontScale=1.5, color=(0,0,0), lineType=4, thickness=2)
        return canvas

    def openImage(self, image=None, fileName=None):
        if image == None:
            img = cv2.imread(self.images[self.press_num])
            if img is None:
                img = sitk.GetArrayFromImage(sitk.ReadImage(self.images[self.press_num]))
                slice_num = img.shape[0] // 2
                img = img[slice_num,...]
                img =self.windowing(img)
            img = cv2.resize(img, (int(3564*4/5), int(2072*4/5)), interpolation=cv2.INTER_LINEAR)
            
        img = self.writetext(img, os.path.basename(self.images[self.press_num]))
        image = self.toQImage(img)
        self.imageLabel.setPixmap(QPixmap.fromImage(image))
        self.fitToWindowAct.setEnabled(True)
        self.updateActions()
        if not self.fitToWindowAct.isChecked():
            self.imageLabel.adjustSize()
        image = None
    def windowing(self, img, WL=-600, WW=1500):
        canvas = img.copy()
        canvas[img<WL-WW//2] = WL-WW//2
        canvas[img>WL+WW//2] = WL+WW//2
        canvas = (canvas - canvas.min()) / (canvas.max() - canvas.min())
        canvas = (canvas * 255).astype(np.uint8)
        return canvas

    def toQImage(self, im, copy=False):
        if im is None:
            return QImage()

        if im.dtype == np.uint8:
            if len(im.shape) == 2:
                qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_Indexed8)
                qim.setColorTable(self.gray_color_table)
                return qim.copy() if copy else qim

            elif len(im.shape) == 3:
                if im.shape[2] == 3:
                    qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_RGB888)
                    return qim.copy() if copy else qim
                elif im.shape[2] == 4:
                    qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_ARGB32)
                    return qim.copy() if copy else qim

if __name__=='__main__':
    app = QApplication(sys.argv)
    labeler = LabelingTool()
    labeler.show()
    app.exec_()