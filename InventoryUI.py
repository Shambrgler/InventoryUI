import os
import shutil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QListWidget, QLineEdit, QLabel, QMessageBox, QMenuBar, QStatusBar, QInputDialog
from PyQt5.QtGui import QFont

filename = r"S:\IS\Inventory DB\PC_Inventory.txt"

def backup_file():
    split_name = filename.split('.')
    new_name = ("%s_backup.txt" % (split_name[0]))
    shutil.copyfile(filename, new_name)

def sort_file():
    sort_list = []
    with open(filename) as oldfile:
        for item in oldfile:
            if item is not None:
                sort_list.append(item)
    sort_list.sort()
    with open("%s.bak" % (filename), 'w') as newfile:
        for i in sort_list:
            if i is not None:
                newfile.write("%s" % (i))
    os.remove(filename)
    os.rename(("%s.bak" % (filename)), filename)
    newfile.close()
    ui.refreshList()


def change_dir():
    global filename
    editdirtxt, editdirBool = QInputDialog.getText(MainWindow, "Change Directory", "Enter filepath for inventory file:", text=filename)
    if editdirBool:
        filename = editdirtxt
        ui.refreshList()


#opens inventory file and writes a new line at the end
#called by addButton
def add_line(add_string):
    with open(filename, 'a') as open_file:
        open_file.write("%s\n" % (add_string))
    open_file.close()

#opens a new file with same name plus ".bak"; writes everything that doesn't have "delete_string" to new file, then deletes old file and ".bak"
#called by deleteButton
def delete_line(delete_string):
    with open(filename) as oldfile, open("%s.bak" % (filename), 'w') as newfile:
        for item in oldfile:
            if delete_string != item:
                newfile.write(item)
    os.remove(filename)
    os.rename(("%s.bak" % (filename)), filename)
    newfile.close()

#opens new file with same name plus ".bak"; writes everything that isn't "currentItem" to new file; then replaces "currentItem" with "editLinetxt", and writes it to new file
#called by editButton
def edit_line(currentItem,editLinetxt):
    with open(filename) as oldfile, open("%s.bak" % (filename), 'w') as newfile:
        for item in oldfile:
            if currentItem != item:
                newfile.write(item)
            if currentItem == item:
                newfile.write(editLinetxt + '\n')
    os.remove(filename)
    os.rename(("%s.bak" % (filename)), filename)
    newfile.close()
    
#Class object that has all objects for the GUI with styles, methods, etc.
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        objectfilename = filename
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(885, 620)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #Text search box; contains connection to "textChanged" method
        self.searchInput = QtWidgets.QLineEdit(self.centralwidget)
        self.searchInput.setGeometry(QtCore.QRect(20, 80, 650, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.searchInput.setFont(font)
        self.searchInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.searchInput.setInputMethodHints(QtCore.Qt.ImhNone)
        self.searchInput.setText("")
        self.searchInput.setClearButtonEnabled(True)
        self.searchInput.setObjectName("searchInput")
        self.searchInput.textChanged.connect(self.listTextChanged)
        
        #Search label for search box
        self.searchLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchLabel.setGeometry(QtCore.QRect(20, 20, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.searchLabel.setFont(font)
        self.searchLabel.setObjectName("searchLabel")
        
        #list widget that is updated by most functions; displays contents of "filename"
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 130, 650, 450))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        
        #Push button; contains connection to addButtonClicked method
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(690, 130, 175, 100))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.addButton.setFont(font)
        self.addButton.setToolTip("")
        self.addButton.setStyleSheet("background-color: rgb(212, 212, 255);")
        self.addButton.setObjectName("addButton")
        self.addButton.clicked.connect(self.addButtonClicked)
        
        #Push button; contains connection to deleteButtonClicked method
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(690, 480, 175, 100))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.deleteButton.setFont(font)
        self.deleteButton.setStyleSheet("background-color: rgb(255, 105, 105);")
        self.deleteButton.setObjectName("deleteButton")
        self.deleteButton.clicked.connect(self.deleteButtonClicked)
        
        #Push button; contains connection to editButtonClicked method
        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        self.editButton.setGeometry(QtCore.QRect(690, 305, 175, 100))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.editButton.setFont(font)
        self.editButton.setStyleSheet("background-color: rgb(212, 212, 255);")
        self.editButton.setObjectName("editButton")
        self.editButton.clicked.connect(self.editButtonClicked)
        
        #Menu Bar;  Menu options non-functional
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 885, 20))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        
        #Status Bar; displays status tips from retranslateUI method
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        #Menu bar item;  Change Directory; Sort File; Backup file
        self.actionChange_Directory = QtWidgets.QAction(MainWindow)
        self.actionChange_Directory.setObjectName("actionChange_Directory")
        self.menuSettings.addAction(self.actionChange_Directory)
        self.actionChange_Directory.triggered.connect(self.change_inventory_clicked)

        self.actionSort_File = QtWidgets.QAction(MainWindow)
        self.actionSort_File.setObjectName("actionSort_File")
        self.menuSettings.addAction(self.actionSort_File)
        self.actionSort_File.triggered.connect(self.sort_file_clicked)

        self.actionBackup_File = QtWidgets.QAction(MainWindow)
        self.actionBackup_File.setObjectName("actionBackup_File")
        self.menuSettings.addAction(self.actionBackup_File)
        self.actionBackup_File.triggered.connect(self.backup_file_clicked)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    #Translate UI method;  makes applicable changes to text on all GUI objects
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inventory UI Application"))
        MainWindow.setWindowIcon(QtGui.QIcon("C:/Windows/System32/@WLOGO_48x48.png"))
        
        self.searchInput.setStatusTip(_translate("MainWindow", "Enter Search String"))
        self.searchInput.setPlaceholderText(_translate("MainWindow", "Enter Search"))
        
        self.searchLabel.setText(_translate("MainWindow", "Search"))
        
        self.addButton.setStatusTip(_translate("MainWindow", "Add New Entry"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        
        self.deleteButton.setStatusTip(_translate("MainWindow", "Delete Selected Entry"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        
        self.editButton.setStatusTip(_translate("MainWindow", "Edit Selected Entry"))
        self.editButton.setText(_translate("MainWindow", "Edit"))
        
        self.menuSettings.setTitle(_translate("MainWindow", "File"))
        
        self.actionChange_Directory.setText(_translate("MainWindow", "Change Directory"))
        self.actionChange_Directory.setToolTip(_translate("MainWindow", "Change Inventory Location"))

        self.actionSort_File.setText(_translate("MainWindow", "Sort Inventory"))
        self.actionSort_File.setToolTip(_translate("MainWindow", "Sort Inventory File"))

        self.actionBackup_File.setText(_translate("MainWindow", "Backup File"))
        self.actionBackup_File.setToolTip(_translate("MainWindow", "Backup Inventory File"))
        
    #Fuction called by editButton
    #pulls currently selected item in listWidget; If nothing is selected an message box appears, prompting user to make a selection
    #strips whitespace off selection and opens an Input Dialog box for user to edit the selected entry
    #calls "edit_line" function
    def editButtonClicked(self):
        currentItem = self.listWidget.currentItem()
        if currentItem is None:
            errormsg = QMessageBox()
            errormsg.setWindowTitle("Error Message")
            errormsg.setText("Make a selection in the list to edit!")
            x = errormsg.exec_()
        else:
            helperText = currentItem.text().strip()
            editLinetxt, editLineBool = QInputDialog.getText(MainWindow, "Edit Entry", "Enter New Value for: \n%s" % (currentItem.text()), echo=QLineEdit.Normal, text=helperText)
            if editLineBool:
                edit_line(currentItem.text(),editLinetxt)
                self.refreshList()

    #Function called by addButton
    #Opens Input Dialog box for user to enter a new line into inventory
    #Calls "add_line" function
    def addButtonClicked(self):
        addLinetxt, addLineBool = QInputDialog.getText(MainWindow, "Add Line", "Enter Inventory Info to Add")
        if addLineBool:
            add_line(addLinetxt)
            self.refreshList()

    #Pulls current selection from "listWidget"
    #if nothing is selected, a message popup prompts user to make a selection
    #deletes the currently selected item in "listWidget"
    #calls "delete_line" function
    def deleteButtonClicked(self):
        deleteItem = self.listWidget.currentItem()
        if deleteItem is None:
            errormsg = QMessageBox()
            errormsg.setWindowTitle("Error Message")
            errormsg.setText("Make a selection in the list to edit!")
            x = errormsg.exec_()
        elif not deleteItem.text().isspace():
            delete_line(deleteItem.text())
            self.refreshList()

    #clears the "listWidget" then reopens "filename"
    #used to update "listWidget" after lines are added/removed/changed
    def refreshList(self):
        self.listWidget.clear()
        with open(filename, 'r') as openListFile:
            for line in openListFile:
                if not line.isspace():
                    self.listWidget.addItem(line)

    #when anythng is typed into the search box, this function is called
    #first clears "listWidget", then repopulates list with search criteria; not case sensitive
    def listTextChanged(self, searchString):
        self.listWidget.clear()
        with open(filename, 'r') as openListFile:
            for line in openListFile:
                if searchString.lower() in line.lower() and not line.isspace():
                    self.listWidget.addItem(line)

    def change_inventory_clicked(self):
        change_dir()

    def sort_file_clicked(self):
        sort_file()

    def backup_file_clicked(self):
        backup_file()    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #added refresh so that list populates when the program is opened
    ui.refreshList()
    sys.exit(app.exec_())
