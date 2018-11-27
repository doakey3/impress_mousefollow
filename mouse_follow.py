import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QPixmap, QCursor
import threading
import pyxhook

class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.running = False
        label = QLabel(self)
        pixmap = QPixmap('pointer.png')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.hookman = pyxhook.HookManager()
        self.hookman.KeyDown = self.keydown
        self.hookman.KeyUp = self.keyup
        self.hookman.HookKeyboard()
        self.hookman.start()
        
        self.thread = threading.Thread(target=self.worker)
        self.thread.start()
        
    def closeEvent(self, event):
        self.hookman.cancel()
        self.thread.terminate()
    
    def keydown(self, event):
        if event.Key == 'Control_L':
            self.show()
            self.running = True
    
    def keyup(self, event):
        if event.Key == 'Control_L':
            self.hide()
            self.running = False
    
    def worker(self):
        while True:
            print('running')
            if self.running:
                
                #preview_top = 225
                #preview_bottom = 849
                #preview_left = 48
                #preview_right = 1150
                
                res_x = 1920
                res_y = 1080
                
                preview_top = 44
                preview_bottom = 409
                preview_left = 46
                preview_right = 696
                
                width = self.frameGeometry().width()
                height = self.frameGeometry().height()
                
                pos = QCursor().pos()
                x = pos.x()
                y = pos.y()
                
                new_x = (((x - preview_left) / (preview_right - preview_left)) * res_x) + res_x - (width / 2)
                new_y = (((y - preview_top) / (preview_bottom - preview_top)) * res_y) - (height / 2)
                
                if new_x < res_x:
                    new_x = res_x
                elif new_x > (res_x * 2) - width:
                    new_x = (res_x * 2) - width
                
                if new_y < 0:
                    new_y = 0
                elif new_y > res_y - height:
                    new_y = res_y - height
                
                self.move(new_x, new_y)
     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    
