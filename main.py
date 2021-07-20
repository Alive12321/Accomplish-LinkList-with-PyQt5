
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
import qtmodern.styles
import qtmodern.windows
from PyQt5 import QtWidgets
import os
import json

op = QtWidgets.QGraphicsOpacityEffect()
op.setOpacity(0.5)
path="test.json"

class Ui_Dialog(object):
    def setupUi(self, Dialog,text=" 插入成功"):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 300)
        Dialog.setMinimumSize(QtCore.QSize(300, 300))
        Dialog.setMaximumSize(QtCore.QSize(300, 300))
        Dialog.setBaseSize(QtCore.QSize(300, 300))
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 220, 100, 41))
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 80, 261, 91))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.text = text
        self.retranslateUi(Dialog)
        self.pushButton.clicked['bool'].connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "确认"))
        self.label.setText(_translate("Dialog",self.text))

class MyWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None,text=" 插入成功"):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self,text)
def Dialog(text=" 插入成功"):
    app = QApplication(sys.argv)
    myWin = MyWindow(text=text)
    myWin.show()
    sys.exit(app.exec_())



class Student(object):

    def __init__(self, sno="19600", name="Nameless", sex='Male', birthday="2001/9/15", pic=""):
        self.sno = sno
        self.name = name
        self.sex = sex
        self.birthday = birthday
        self.pic = pic

    def __repr__(self):
        text = str(self.__dict__)
        return text


class Node(object):
    def __init__(self,data=Student()):
        self.stu=data
        self.pre=self
        self.next=self


def save_json(path, data, pos=0):
    data = json.dumps(data)
    lines = []
    with open(path, 'r', encoding='utf-8') as f:
        for item in f.readlines():
            lines.append(item)

    data += ',\n'
    lines.insert(pos, data)
    s = ''.join(lines)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(s)


def get_file_line_num(path):
    try:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                return len(lines)
    except Exception as e:
        print('File not exist!', e)
        return 0



class SaveJson(object):

    def save_file(self, path, item):
        # 先将字典对象转化为可写入文本的字符串
        item = json.dumps(item)
        try:
            if not os.path.exists(path):
                with open(path, "w", encoding='utf-8') as f:
                    f.write(item + ",\n")
                    print("^_^ write success")

            else:
                with open(path, "w", encoding='utf-8') as f:
                    f.write(item + ",\n")
                    print("^_^ write success")

            return get_file_line_num(path)
        except Exception as e:
            print("write error==>", e)


class LoadJson(object):

    def read_line(self, path, line):
        try:
            if not os.path.exists(path):
                f = open(path, 'w')
            else:
                with open(path, 'r+', encoding='utf-8') as f:
                    lines = f.readlines()
                    print('read success!')
                    return lines[line]

        except Exception as e:
            print('read error!!!', e)

def SaveInfo(path,lis):
    with open(path, "w", encoding='utf-8') as f:
        f.truncate()
    s = SaveJson()
    h=lis.head.next
    K=[]
    for i in range(lis.length):
        K.append(h)
    for k in K:
        item = {
            'sno':k.stu.sno,
            'name':k.stu.name,
            'sex':k.stu.sex,
            'birthday':k.stu.birthday,
            'pic':k.stu.pic
        }
        s.save_file(path, item)

def ReadInfo(path,pos,num):
    s = LoadJson()
    lis=[]
    file_len=get_file_line_num(path)
    if(file_len<pos+num):
        print("读入数据有误")
        return
    for i in range(num):
       data_str = s.read_line(path,i+pos)
       data_str = data_str[:-2]  # 去掉最后的逗号
       data = json.loads(data_str)
       lis.append(data)
    return  lis



class ChainTable(object):
    def __init__(self):
        self.head=Node()
        self.tail=Node()
        self.tail.pre=self.head
        self.tail.next=self.head
        self.head.pre=self.tail
        self.head.next=self.tail
        self.length=0

    def isEmpty(self):
        return self.length==0

    def clear(self):
        self.head = Node()
        self.tail = Node()
        self.tail.pre = self.head
        self.tail.next = self.head
        self.head.pre = self.tail
        self.head.next = self.tail
        self.length=0
        # Dialog(" 清除成功")

    def insert(self,pos,node):
        point = self.head
        if (pos >self.length&~ls.isExist(node)):
            print("插入溢出")
            return False
        for i in range(self.length):
            if (i == pos):
                node.next=point.next
                node.next.pre=node
                point.next=node
                node.pre=point
                break
            point = point.next
        self.length=self.length+1
        return True
        # Dialog()

    def append(self,data):
        data.next=self.tail
        data.pre=self.head
        self.tail.pre=data
        self.head.next=data
        self.length=self.length+1
        # Dialog(" 添加成功")

    def delete(self,pos):
        point=self.head.next
        if(pos>=self.length|pos<0):
            # Dialog(" 删除溢出")
            print("删除溢出")
            return False
        for i in range(self.length):
            if(i==pos):
                point.pre.next=point.next
                point.next.pre=point.pre
                self.length = self.length - 1
                return True
            point = point.next
        #ls_save()
        # Dialog(" 删除成功")

    def isExist(self,node):
        h=ls.head.next
        while h!=ls.tail:
            if(h.stu.name==node.stu.name):
                print("该姓名的信息已存在")
                return True
            h=h.next
        return False



def ls_init():
    ks=ChainTable()
    save_num=get_file_line_num(path)
    ks.length=save_num
    save_Info=ReadInfo(path,0,save_num)
    if (save_num!=0):
        for item in save_Info:
            temp = Node()
            temp.stu.sno = item["sno"]
            temp.stu.sex = item["sex"]
            temp.stu.birthday = item["birthday"]
            temp.stu.pic = item["pic"]
            temp.stu.name = item["name"]
            ks.append(temp)
    return ks

ls=ls_init()
def ls_save():
    print("开始保存文件")
    SaveInfo(path,ls)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(761, 711)
        MainWindow.setStyleSheet("\n"r"background-image: url(C:\Users\34780\PycharmProjects\pythonProject\Example\task1-linklist\util\胰脏_1.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_7.setGeometry(QtCore.QRect(500, 600, 195, 41))
        self.formLayoutWidget_7.setObjectName("formLayoutWidget_7")
        self.formLayout_7 = QtWidgets.QFormLayout(self.formLayoutWidget_7)
        self.formLayout_7.setContentsMargins(0, 0, 0, 0)
        self.formLayout_7.setObjectName("formLayout_7")
        self.pushButton_clear = QtWidgets.QPushButton(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setStyleSheet("background-image: url(:/新前缀/白.png);")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pushButton_clear)
        self.pushButton_close = QtWidgets.QPushButton(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setStyleSheet("background-image: url(:/新前缀/白.png);")
        self.pushButton_close.setObjectName("pushButton_close")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButton_close)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 40, 641, 541))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_add = QtWidgets.QGroupBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(20)
        self.groupBox_add.setFont(font)
        self.groupBox_add.setStyleSheet("background-image: url(:\Moon.jpg);")
        self.groupBox_add.setObjectName("groupBox_add")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_add)
        self.formLayoutWidget.setGeometry(QtCore.QRect(60, 40, 161, 85))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_name_input = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.label_name_input.setFont(font)
        self.label_name_input.setObjectName("label_name_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_name_input)
        self.lineEdit_name_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_name_input.setStyleSheet("background-image: url(:/新前缀/白.png);")
        self.lineEdit_name_input.setObjectName("lineEdit_name_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_name_input)
        self.label_sno_input = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.label_sno_input.setFont(font)
        self.label_sno_input.setObjectName("label_sno_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_sno_input)
        self.lineEdit_sno_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_sno_input.setStyleSheet("background-image: url(:/新前缀/白.png);")
        self.lineEdit_sno_input.setObjectName("lineEdit_sno_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_sno_input)
        self.label_birthday_input = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.label_birthday_input.setFont(font)
        self.label_birthday_input.setObjectName("label_birthday_input")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_birthday_input)
        self.lineEdit_birthday_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_birthday_input.setStyleSheet("background-image: url(:/新前缀/白.png);")
        self.lineEdit_birthday_input.setObjectName("lineEdit_birthday_input")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_birthday_input)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_add)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(250, 40, 174, 84))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_sex_input = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.label_sex_input.setFont(font)
        self.label_sex_input.setObjectName("label_sex_input")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_sex_input)
        self.label_pos_input = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.label_pos_input.setFont(font)
        self.label_pos_input.setObjectName("label_pos_input")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_pos_input)
        self.comboBox_sex_input = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.comboBox_sex_input.setObjectName("comboBox_sex_input")
        self.comboBox_sex_input.addItem("")
        self.comboBox_sex_input.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_sex_input)
        self.lineEdit_pos_input = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_pos_input.setStyleSheet("background-image: url(:/新前缀/白.png);")
        self.lineEdit_pos_input.setObjectName("lineEdit_pos_input")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_pos_input)
        self.pushButton_add_input = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pushButton_add_input.setObjectName("pushButton_add_input")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton_add_input)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_add)
        self.layoutWidget1.setGeometry(QtCore.QRect(470, 30, 95, 121))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_pic_input = QtWidgets.QLabel(self.layoutWidget1)
        self.label_pic_input.setStyleSheet("background-image: url(:/新前缀/白.png);")
        self.label_pic_input.setText("")
        self.label_pic_input.setObjectName("label_pic_input")
        self.verticalLayout_2.addWidget(self.label_pic_input)
        self.pushButton_upload_input = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_upload_input.setObjectName("pushButton_upload_input")
        self.verticalLayout_2.addWidget(self.pushButton_upload_input)
        self.verticalLayout.addWidget(self.groupBox_add)
        self.groupBox_search = QtWidgets.QGroupBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(20)
        self.groupBox_search.setFont(font)
        self.groupBox_search.setStyleSheet("\n""background-image: url(:/新前缀/Moon_1.jpg);")
        self.groupBox_search.setObjectName("groupBox_search")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_search)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(270, 40, 160, 85))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_sno_find = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.label_sno_find.setFont(font)
        self.label_sno_find.setObjectName("label_sno_find")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_sno_find)
        self.lineEdit_sno_find = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_sno_find.setStyleSheet("background-image: url(:/新前缀/白.png);")
        self.lineEdit_sno_find.setReadOnly(True)
        self.lineEdit_sno_find.setObjectName("lineEdit_sno_find")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_sno_find)
        self.label_birthday_find = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.label_birthday_find.setFont(font)
        self.label_birthday_find.setObjectName("label_birthday_find")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_birthday_find)
        self.lineEdit_birthday_find = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_birthday_find.setStyleSheet("background-image: url(:/新前缀/白.png);")
        self.lineEdit_birthday_find.setReadOnly(True)
        self.lineEdit_birthday_find.setObjectName("lineEdit_birthday_find")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_birthday_find)
        self.label_sex_find = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.label_sex_find.setFont(font)
        self.label_sex_find.setObjectName("label_sex_find")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_sex_find)
        self.lineEdit_sex_find = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_sex_find.setStyleSheet("background-image: url(:/新前缀/白.png);")
        self.lineEdit_sex_find.setReadOnly(True)
        self.lineEdit_sex_find.setObjectName("lineEdit_sex_find")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_sex_find)
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_search)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(40, 40, 174, 92))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_name_search = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.label_name_search.setFont(font)
        self.label_name_search.setObjectName("label_name_search")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_name_search)
        self.label_name_find = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.label_name_find.setFont(font)
        self.label_name_find.setObjectName("label_name_find")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_name_find)
        self.lineEdit_name_find = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_name_find.setStyleSheet("background-image: url(:/新前缀/白.png);")
        self.lineEdit_name_find.setReadOnly(True)
        self.lineEdit_name_find.setObjectName("lineEdit_name_find")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_name_find)
        self.pushButton_search = QtWidgets.QPushButton(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setObjectName("pushButton_search")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton_search)
        self.lineEdit_name_search = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_name_search.setStyleSheet("background-image: url(:/新前缀/白.png);")
        self.lineEdit_name_search.setObjectName("lineEdit_name_search")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_name_search)
        self.label_pic_find = QtWidgets.QLabel(self.groupBox_search)
        self.label_pic_find.setGeometry(QtCore.QRect(470, 30, 91, 101))
        self.label_pic_find.setStyleSheet("\n""background-image: url(:/新前缀/白.png);\n""")
        self.label_pic_find.setText("")
        self.label_pic_find.setObjectName("label_pic_find")
        self.verticalLayout.addWidget(self.groupBox_search)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_delete = QtWidgets.QGroupBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(20)
        self.groupBox_delete.setFont(font)
        self.groupBox_delete.setStyleSheet("background-image: url(:/新前缀/樱花.jpg);")
        self.groupBox_delete.setObjectName("groupBox_delete")
        self.formLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_delete)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(50, 50, 211, 81))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_pos_delete = QtWidgets.QLabel(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.label_pos_delete.setFont(font)
        self.label_pos_delete.setObjectName("label_pos_delete")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_pos_delete)
        self.lineEdit_pos_delete = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_pos_delete.setStyleSheet("background-image: url(:/新前缀/白.png);")
        self.lineEdit_pos_delete.setObjectName("lineEdit_pos_delete")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_pos_delete)
        self.pushButton_delete = QtWidgets.QPushButton(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton_delete)
        self.horizontalLayout.addWidget(self.groupBox_delete)
        self.groupBox_4 = QtWidgets.QGroupBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(20)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("background-image: url(:/新前缀/樱花.jpg);")
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayoutWidget_6 = QtWidgets.QWidget(self.groupBox_4)
        self.formLayoutWidget_6.setGeometry(QtCore.QRect(47, 50, 201, 71))
        self.formLayoutWidget_6.setObjectName("formLayoutWidget_6")
        self.formLayout_6 = QtWidgets.QFormLayout(self.formLayoutWidget_6)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_num_info = QtWidgets.QLabel(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.label_num_info.setFont(font)
        self.label_num_info.setObjectName("label_num_info")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_num_info)
        self.lineEdit_num_info = QtWidgets.QLineEdit(self.formLayoutWidget_6)
        self.lineEdit_num_info.setStyleSheet("background-image: url(:/新前缀/白.png);")
        self.lineEdit_num_info.setReadOnly(True)
        self.lineEdit_num_info.setObjectName("lineEdit_num_info")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_num_info)
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 761, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_clear.setText(_translate("MainWindow", "清空链表"))
        self.pushButton_close.setText(_translate("MainWindow", "关闭"))
        self.groupBox_add.setTitle(_translate("MainWindow", "添加信息"))
        self.label_name_input.setText(_translate("MainWindow", "姓名"))
        self.label_sno_input.setText(_translate("MainWindow", "学号"))
        self.label_birthday_input.setText(_translate("MainWindow", "生日"))
        self.label_sex_input.setText(_translate("MainWindow", "性别"))
        self.label_pos_input.setText(_translate("MainWindow", "插入位置"))
        self.comboBox_sex_input.setItemText(0, _translate("MainWindow", "男"))
        self.comboBox_sex_input.setItemText(1, _translate("MainWindow", "女"))
        self.pushButton_add_input.setText(_translate("MainWindow", "添加"))
        self.pushButton_upload_input.setText(_translate("MainWindow", "上传照片"))
        self.groupBox_search.setTitle(_translate("MainWindow", "查找信息"))
        self.label_sno_find.setText(_translate("MainWindow", "学号"))
        self.label_birthday_find.setText(_translate("MainWindow", "生日"))
        self.label_sex_find.setText(_translate("MainWindow", "性别"))
        self.label_name_search.setText(_translate("MainWindow", "查找姓名"))
        self.label_name_find.setText(_translate("MainWindow", "姓名"))
        self.pushButton_search.setText(_translate("MainWindow", "查找"))
        self.groupBox_delete.setTitle(_translate("MainWindow", "删除信息"))
        self.label_pos_delete.setText(_translate("MainWindow", "删除位置"))
        self.pushButton_delete.setText(_translate("MainWindow", "删除"))
        self.groupBox_4.setTitle(_translate("MainWindow", "链表信息"))
        self.label_num_info.setText(_translate("MainWindow", "链表总人数"))


class Friendship(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Friendship, self).__init__()
        self.setupUi(self)
        self.pushButton_clear.setGraphicsEffect(op)
        self.connecter()
        self.show()

    def connecter(self):
        self.pushButton_add_input.clicked.connect(self.press_add)
        self.pushButton_clear.clicked.connect(self.press_clear)
        self.pushButton_close.clicked.connect(self.press_close)
        self.pushButton_delete.clicked.connect(self.press_delete)
        self.pushButton_upload_input.clicked.connect(self.press_upload)
        self.pushButton_search.clicked.connect(self.press_search)

    def press_add(self):
        # 获取表单数据
        stu = Student()
        stu.name = self.lineEdit_name_input.text()
        stu.sno = self.lineEdit_sno_input.text()
        stu.birthday = self.lineEdit_birthday_input.text()
        stu.sex = self.comboBox_sex_input.currentText()
        stu.pic = self.imgName

        pos = int(self.lineEdit_pos_input.text())

        # 新建学生节点并插入到链表
        node = Node(data=stu)
        if(ls.isExist(node)==False):
            if(ls.insert(pos, node)):
                 self.lineEdit_num_info.setText(str(ls.length))
                 print("112")
                 ls_save()
        # 将新的学生数据存入文件中

    def press_clear(self):
        ls.clear()
        self.lineEdit_num_info.setText(str(ls.length))

    def press_close(self):
        sys.exit()

    def press_delete(self):
        pos = self.lineEdit_pos_delete.text()
        ls.delete(int(pos))
        self.lineEdit_num_info.setText(str(ls.length))

    def press_upload(self):
        self.imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(self.imgName).scaled(self.label_pic_input.width(), self.label_pic_input.height())
        self.label_pic_input.setPixmap(jpg)

    def press_search(self):
        name_search = self.lineEdit_name_search.text()
        item = ls.head.next
        while item != None and name_search != item.stu.name and item!=ls.head:
            item = item.next

        if item != None:
            name = item.stu.name
            sno = item.stu.sno
            birthday = item.stu.birthday
            sex = item.stu.sex
            pic = item.stu.pic
            self.lineEdit_name_find.setText(name)
            self.lineEdit_sno_find.setText(sno)
            self.lineEdit_birthday_find.setText(birthday)
            self.lineEdit_sex_find.setText(sex)

            imgName = pic
            jpg = QtGui.QPixmap(pic).scaled(self.label_pic_find.width(), self.label_pic_find.height())
            self.label_pic_find.setPixmap(jpg)

        else:
            print('No student named ', name_search)


def main():
    stu_list = ls
    app = QApplication(sys.argv)
    w = Friendship()
    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(w)
    mw.show()
    sys.exit(app.exec_())

main()


