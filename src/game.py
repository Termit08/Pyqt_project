import sys
import io

import random
from PyQt6 import uic 
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow


template_game = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1075</width>
    <height>835</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>1071</width>
      <height>801</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>../data/phones/game_phone.jpeg</pixmap>
    </property>
    <property name="scaledContents">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QTextBrowser" name="sum_in_box">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>680</y>
      <width>231</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QListWidget" name="lost_sum">
    <property name="geometry">
     <rect>
      <x>430</x>
      <y>140</y>
      <width>271</width>
      <height>571</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>450</x>
      <y>110</y>
      <width>241</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(255, 255, 255);</string>
    </property>
    <property name="text">
     <string>Возможные суммы выйгрыша</string>
    </property>
   </widget>
   <widget class="QPushButton" name="give_number">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>10</y>
      <width>93</width>
      <height>91</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(212, 224, 255);</string>
    </property>
    <property name="text">
     <string>Выдать число</string>
    </property>
   </widget>
   <widget class="QLabel" name="labe">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>110</y>
      <width>231</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(255, 255, 255);</string>
    </property>
    <property name="text">
     <string>Номера оставшихся коробок</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>790</x>
      <y>100</y>
      <width>141</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(255, 255, 255);</string>
    </property>
    <property name="text">
     <string>Банкир</string>
    </property>
   </widget>
   <widget class="QDialogButtonBox" name="choice">
    <property name="geometry">
     <rect>
      <x>720</x>
      <y>640</y>
      <width>221</width>
      <height>61</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(212, 224, 255);</string>
    </property>
    <property name="standardButtons">
     <set>QDialogButtonBox::Cancel|QDialogButtonBox::Ok</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_6">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>660</y>
      <width>231</width>
      <height>16</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(255, 255, 255);</string>
    </property>
    <property name="text">
     <string>Сумма, которая выбывает:</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>280</x>
      <y>50</y>
      <width>291</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(255, 255, 255);</string>
    </property>
    <property name="text">
     <string> Номер вашей коробки:</string>
    </property>
   </widget>
   <widget class="QTextBrowser" name="bank">
    <property name="geometry">
     <rect>
      <x>710</x>
      <y>140</y>
      <width>256</width>
      <height>491</height>
     </rect>
    </property>
   </widget>
   <widget class="QTextBrowser" name="win_sum">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>740</y>
      <width>256</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>150</y>
      <width>231</width>
      <height>508</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QRadioButton" name="box1">
       <property name="styleSheet">
        <string notr="true">color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>RadioButton</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="box2">
       <property name="styleSheet">
        <string notr="true">color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>RadioButton</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="box3">
       <property name="styleSheet">
        <string notr="true">color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>RadioButton</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="box4">
       <property name="styleSheet">
        <string notr="true">color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>RadioButton</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="box5">
       <property name="styleSheet">
        <string notr="true">color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>RadioButton</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="box6">
       <property name="styleSheet">
        <string notr="true">color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>RadioButton</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="box7">
       <property name="styleSheet">
        <string notr="true">color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>RadioButton</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="box8">
       <property name="styleSheet">
        <string notr="true">color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>RadioButton</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="box9">
       <property name="styleSheet">
        <string notr="true">color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>RadioButton</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="box10">
       <property name="styleSheet">
        <string notr="true">color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>RadioButton</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="box11">
       <property name="styleSheet">
        <string notr="true">color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>RadioButton</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="box12">
       <property name="styleSheet">
        <string notr="true">color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>RadioButton</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="box13">
       <property name="styleSheet">
        <string notr="true">color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>RadioButton</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="box14">
       <property name="styleSheet">
        <string notr="true">color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>RadioButton</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="box15">
       <property name="styleSheet">
        <string notr="true">color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>RadioButton</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="box16">
       <property name="styleSheet">
        <string notr="true">color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>RadioButton</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="box17">
       <property name="styleSheet">
        <string notr="true">color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>RadioButton</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="box18">
       <property name="styleSheet">
        <string notr="true">color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>RadioButton</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="box19">
       <property name="styleSheet">
        <string notr="true">color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>RadioButton</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QLabel" name="label_7">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>730</y>
      <width>121</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(255, 255, 255);</string>
    </property>
    <property name="text">
     <string>Cумма выйгрыша:</string>
    </property>
   </widget>
   <widget class="QTextBrowser" name="num">
    <property name="geometry">
     <rect>
      <x>580</x>
      <y>40</y>
      <width>61</width>
      <height>51</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="next_turn">
    <property name="geometry">
     <rect>
      <x>700</x>
      <y>40</y>
      <width>261</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(212, 224, 255);</string>
    </property>
    <property name="text">
     <string>Следующий ход</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1075</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

class Game_window(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template_game)
        uic.loadUi(f, self)
        self.dicti = {}
        self.lis_box = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
                        '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
        self.sum = ['0', '1', '5', '10', '50',
                     '100', '500', '1000','5000', '10000',
                       '50000', '100000', '250000', '500000', '750000',
                         '1000000', '2500000', '5000000', '7500000', '10000000']
        self.give_number.clicked.connect(self.random_number)

    def random_number(self):
        for i in self.lis_box:
            summ = random.choice(self.sum)
            self.dicti[i] = summ
            self.sum.remove(summ)
        player_number = random.choice(self.lis_box)
        self.num.setText(player_number)
        self.lis_box.remove(player_number)
        number = self.lis_box[0]
        self.box1.setText(number)
        self.lis_box.remove(number)
        number = self.lis_box[0]
        self.box2.setText(number)
        self.lis_box.remove(number)
        number = self.lis_box[0]
        self.box3.setText(number)
        self.lis_box.remove(number)
        number = self.lis_box[0]
        self.box4.setText(number)
        self.lis_box.remove(number)
        number = self.lis_box[0]
        self.box5.setText(number)
        self.lis_box.remove(number)
        number = self.lis_box[0]
        self.box6.setText(number)
        self.lis_box.remove(number)
        number = self.lis_box[0]
        self.box7.setText(number)
        self.lis_box.remove(number)
        number = self.lis_box[0]
        self.box8.setText(number)
        self.lis_box.remove(number)
        number = self.lis_box[0]
        self.box9.setText(number)
        self.lis_box.remove(number)
        number = self.lis_box[0]
        self.box10.setText(number)
        self.lis_box.remove(number)
        number = self.lis_box[0]
        self.box11.setText(number)
        self.lis_box.remove(number)
        number = self.lis_box[0]
        self.box12.setText(number)
        self.lis_box.remove(number)
        number = self.lis_box[0]
        self.box13.setText(number)
        self.lis_box.remove(number)
        number = self.lis_box[0]
        self.box14.setText(number)
        self.lis_box.remove(number)
        number = self.lis_box[0]
        self.box15.setText(number)
        self.lis_box.remove(number)
        number = self.lis_box[0]
        self.box16.setText(number)
        self.lis_box.remove(number)
        number = self.lis_box[0]
        self.box17.setText(number)
        self.lis_box.remove(number)
        number = self.lis_box[0]
        self.box18.setText(number)
        self.lis_box.remove(number)
        number = self.lis_box[0]
        self.box19.setText(number)
        self.lis_box.remove(number)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Game_window()
    ex.show()
    sys.exit(app.exec())