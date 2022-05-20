import sys
import os
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *
from window import *
from PySide6.QtWidgets import QTableWidget, QApplication
import time

root = Tk()
root.withdraw()

class mainwindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        ## Buttons
        self.ui.pushButton_2.clicked.connect(lambda: self.findFolder())
        self.ui.pushButton_3.clicked.connect(lambda: self.convert())

    def findFolder(self):
        root.filename = filedialog.askdirectory(title="Select a folder")
        self.ui.lineEdit_2.setText(root.filename)

    def runloading(self, n):
        for i in range(n):
            time.sleep(0.01)
            self.ui.progressBar.setValue(i + 1)

## if(not(test_str2 and test_str2.strip())):
    def convert(self):
        path = self.ui.lineEdit_2.text()
        if(not(path and path.strip())):
            showerror("Error Ocurred", "Folder Directory is not specified or selected! ")
            return
        base = self.ui.base.text()
        goal = self.ui.finish.text()
        for root, dirs, files in os.walk(path):
            for file in files:
                if (file.endswith(base)):
                    newname = file.replace(base, goal)
                    form = os.path.join(root, file)
                    form2 = os.path.join(root, newname)
                    output = os.rename(form, form2)
        self.runloading(100)
        showinfo("Process", "Extension changed successfully")
        self.ui.progressBar.setValue(0)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainwindow()
    sys.exit(app.exec())