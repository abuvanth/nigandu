# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Apr 18 19:00:48 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainwin(object):
    def setupUi(self, mainwin):
        mainwin.setObjectName("mainwin")
        mainwin.setWindowModality(QtCore.Qt.ApplicationModal)
        mainwin.resize(600, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Documents/appicons/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainwin.setWindowIcon(icon)
        mainwin.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.India))
        self.centralwidget = QtGui.QWidget(mainwin)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 321, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.listView = QtGui.QListView(self.verticalLayoutWidget)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(349, 69, 241, 461))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listView_3 = QtGui.QListView(self.verticalLayoutWidget_2)
        self.listView_3.setObjectName("listView_3")
        self.verticalLayout_2.addWidget(self.listView_3)
        self.listView_2 = QtGui.QListView(self.verticalLayoutWidget_2)
        self.listView_2.setObjectName("listView_2")
        self.verticalLayout_2.addWidget(self.listView_2)
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 571, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.comboBox = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)

        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        mainwin.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainwin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        self.filemenu = QtGui.QMenu(self.menubar)
        self.filemenu.setGeometry(QtCore.QRect(189, 128, 143, 147))
        self.filemenu.setObjectName("filemenu")
        self.menu_Go = QtGui.QMenu(self.menubar)
        self.menu_Go.setObjectName("menu_Go")
        self.menuBook_Marks = QtGui.QMenu(self.menubar)
        self.menuBook_Marks.setObjectName("menuBook_Marks")
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        mainwin.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainwin)
        self.statusbar.setToolTip("")
        self.statusbar.setStatusTip("")
        self.statusbar.setAutoFillBackground(True)
        self.statusbar.setObjectName("statusbar")
        mainwin.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(mainwin)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBar.setSizeIncrement(QtCore.QSize(50, 50))
        self.toolBar.setBaseSize(QtCore.QSize(50, 50))
        self.toolBar.setMouseTracking(True)
        self.toolBar.setIconSize(QtCore.QSize(48, 48))
        self.toolBar.setObjectName("toolBar")
        mainwin.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.go_previous = QtGui.QAction(mainwin)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/prev_50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icons/prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.go_previous.setIcon(icon1)
        self.go_previous.setObjectName("go_previous")
        self.go_next = QtGui.QAction(mainwin)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.go_next.setIcon(icon2)
        self.go_next.setObjectName("go_next")
        self.go_random = QtGui.QAction(mainwin)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/rand.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.go_random.setIcon(icon3)
        self.go_random.setObjectName("go_random")
        self.file_add_word = QtGui.QAction(mainwin)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/add_50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.file_add_word.setIcon(icon4)
        self.file_add_word.setObjectName("file_add_word")
        self.file_options = QtGui.QAction(mainwin)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.file_options.setIcon(icon5)
        self.file_options.setObjectName("file_options")
        self.file_help = QtGui.QAction(mainwin)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.file_help.setIcon(icon6)
        self.file_help.setObjectName("file_help")
        self.mark_favourite = QtGui.QAction(mainwin)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/bookmark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mark_favourite.setIcon(icon7)
        self.mark_favourite.setObjectName("mark_favourite")
        self.bm_viewbookmark = QtGui.QAction(mainwin)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/viewbkm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bm_viewbookmark.setIcon(icon8)
        self.bm_viewbookmark.setObjectName("bm_viewbookmark")
        self.help_about = QtGui.QAction(mainwin)
        self.help_about.setObjectName("help_about")
        self.help_visitblog = QtGui.QAction(mainwin)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/visitblog.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help_visitblog.setIcon(icon9)
        self.help_visitblog.setObjectName("help_visitblog")
        self.help_help = QtGui.QAction(mainwin)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help_help.setIcon(icon10)
        self.help_help.setObjectName("help_help")
        self.actionAbout = QtGui.QAction(mainwin)
        self.actionAbout.setIcon(icon)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAdd_a_word = QtGui.QAction(mainwin)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_a_word.setIcon(icon11)
        self.actionAdd_a_word.setObjectName("actionAdd_a_word")
        self.actionQuit = QtGui.QAction(mainwin)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon12)
        self.actionQuit.setObjectName("actionQuit")
        self.actionHelp = QtGui.QAction(mainwin)
        self.actionHelp.setIcon(icon6)
        self.actionHelp.setObjectName("actionHelp")
        self.filemenu.addAction(self.file_options)
        self.filemenu.addAction(self.file_help)
        self.filemenu.addAction(self.actionAdd_a_word)
        self.filemenu.addSeparator()
        self.filemenu.addAction(self.actionQuit)
        self.menu_Go.addAction(self.go_next)
        self.menu_Go.addAction(self.go_random)
        self.menuBook_Marks.addAction(self.mark_favourite)
        self.menuBook_Marks.addAction(self.bm_viewbookmark)
        self.menu_Help.addAction(self.help_visitblog)
        self.menu_Help.addAction(self.help_help)
        self.menu_Help.addAction(self.actionHelp)
        self.menubar.addAction(self.filemenu.menuAction())
        self.menubar.addAction(self.menu_Go.menuAction())
        self.menubar.addAction(self.menuBook_Marks.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(mainwin)
        QtCore.QMetaObject.connectSlotsByName(mainwin)

    def retranslateUi(self, mainwin):
        mainwin.setWindowTitle(QtGui.QApplication.translate("mainwin", "NJN Dictionary", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("mainwin", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.filemenu.setTitle(QtGui.QApplication.translate("mainwin", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Go.setTitle(QtGui.QApplication.translate("mainwin", "&Go", None, QtGui.QApplication.UnicodeUTF8))
        self.menuBook_Marks.setTitle(QtGui.QApplication.translate("mainwin", "&Book Marks", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("mainwin", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("mainwin", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.go_previous.setText(QtGui.QApplication.translate("mainwin", "&Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.go_previous.setShortcut(QtGui.QApplication.translate("mainwin", "Ctrl+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.go_next.setText(QtGui.QApplication.translate("mainwin", "&Next", None, QtGui.QApplication.UnicodeUTF8))
        self.go_next.setShortcut(QtGui.QApplication.translate("mainwin", "Ctrl+Y", None, QtGui.QApplication.UnicodeUTF8))
        self.go_random.setText(QtGui.QApplication.translate("mainwin", "&Random", None, QtGui.QApplication.UnicodeUTF8))
        self.go_random.setShortcut(QtGui.QApplication.translate("mainwin", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.file_add_word.setText(QtGui.QApplication.translate("mainwin", "&Add new word", None, QtGui.QApplication.UnicodeUTF8))
        self.file_add_word.setToolTip(QtGui.QApplication.translate("mainwin", "Add a word to the dictionary. . . ", None, QtGui.QApplication.UnicodeUTF8))
        self.file_add_word.setStatusTip(QtGui.QApplication.translate("mainwin", "Add a new word to the dictionary. . . ", None, QtGui.QApplication.UnicodeUTF8))
        self.file_add_word.setShortcut(QtGui.QApplication.translate("mainwin", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.file_options.setText(QtGui.QApplication.translate("mainwin", "&Option", None, QtGui.QApplication.UnicodeUTF8))
        self.file_options.setShortcut(QtGui.QApplication.translate("mainwin", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.file_help.setText(QtGui.QApplication.translate("mainwin", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.file_help.setShortcut(QtGui.QApplication.translate("mainwin", "Ctrl+H", None, QtGui.QApplication.UnicodeUTF8))
        self.mark_favourite.setText(QtGui.QApplication.translate("mainwin", "Book &Mark This", None, QtGui.QApplication.UnicodeUTF8))
        self.mark_favourite.setShortcut(QtGui.QApplication.translate("mainwin", "Ctrl+B", None, QtGui.QApplication.UnicodeUTF8))
        self.bm_viewbookmark.setText(QtGui.QApplication.translate("mainwin", "&Book Marks", None, QtGui.QApplication.UnicodeUTF8))
        self.bm_viewbookmark.setShortcut(QtGui.QApplication.translate("mainwin", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.help_about.setText(QtGui.QApplication.translate("mainwin", "A&bout", None, QtGui.QApplication.UnicodeUTF8))
        self.help_about.setShortcut(QtGui.QApplication.translate("mainwin", "Ctrl+I", None, QtGui.QApplication.UnicodeUTF8))
        self.help_visitblog.setText(QtGui.QApplication.translate("mainwin", "&Visit Our Blog", None, QtGui.QApplication.UnicodeUTF8))
        self.help_visitblog.setShortcut(QtGui.QApplication.translate("mainwin", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8))
        self.help_help.setText(QtGui.QApplication.translate("mainwin", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.help_help.setShortcut(QtGui.QApplication.translate("mainwin", "F1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("mainwin", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_a_word.setText(QtGui.QApplication.translate("mainwin", "Add a word", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("mainwin", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("mainwin", "Help", None, QtGui.QApplication.UnicodeUTF8))

import mainwindow_rc