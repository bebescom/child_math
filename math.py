# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import random
from Ui_math import Ui_Dialog
import pygame
import time
from PyQt5 import sip

file1=r'yes.wav'
file2=r'no.wav'
pygame.mixer.init()

class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_t1_textChanged(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        
    
    @pyqtSlot()
    def on_t2_textChanged(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        
    
    @pyqtSlot()
    def on_t3_textChanged(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        
    
    @pyqtSlot()
    def on_jg_textChanged(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        
    
    @pyqtSlot()
    def on_p1_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        global s1
        global s2
        global s3
        nom = int(self.lineEdit.text())
        s1=str(random.randint(0,nom))
        if fun == 1:
            s2="+"
        if fun == 2:
            s2="-"
        s3=str(random.randint(0,nom))
        if s1 >= s3:
            self.t1.append(s1)
            self.t2.append(s2)
            self.t3.append(s3)


    
    @pyqtSlot()
    def on_p2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.t1.setText("")
        self.t2.setText("")
        self.t3.setText("")
        self.jg.setText("")
        self.lineEdit.setText("")
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        s1a=int(s1)
        s3a=int(s3)
        cont1 = int(self.jg.toPlainText())
        if fun ==1:
            cont = s1a+s3a
            if cont ==cont1:
                track1 = pygame.mixer.music.load(file1)
                pygame.mixer.music.play()
                time.sleep(2)
                pygame.mixer.music.stop()
                print("ok")
            else:
                track2 = pygame.mixer.music.load(file2)
                pygame.mixer.music.play()
                time.sleep(2)
                pygame.mixer.music.stop()
                print("null")
        else:
            cont = s1a-s3a
            if cont == cont1:
                track1 = pygame.mixer.music.load(file1)
                pygame.mixer.music.play()
                time.sleep(2)
                pygame.mixer.music.stop()
                print("ok")
            else:
                track2 = pygame.mixer.music.load(file2)
                pygame.mixer.music.play()
                time.sleep(2)
                pygame.mixer.music.stop()
                print("null")
    
    @pyqtSlot(str)
    def on_lineEdit_textChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        
    
    @pyqtSlot()
    def on_jiafa_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        global fun
        fun = 1
    
    @pyqtSlot()
    def on_jianfa_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        global fun
        fun = 2
       
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Dialog()
    ui.show()
    sys.exit(app.exec_())
