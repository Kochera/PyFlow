# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GIT\nodes\GraphEditor_ui.ui'
#
# Created: Fri Dec 30 15:04:43 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1086, 669)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("AGraphPySide/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontal_splitter = QtGui.QSplitter(self.centralwidget)
        self.horizontal_splitter.setStyleSheet("")
        self.horizontal_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.horizontal_splitter.setObjectName("horizontal_splitter")
        self.SceneWidget = QtGui.QWidget(self.horizontal_splitter)
        self.SceneWidget.setObjectName("SceneWidget")
        self.gridLayout = QtGui.QGridLayout(self.SceneWidget)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setObjectName("gridLayout")
        self.SceneLayout = QtGui.QGridLayout()
        self.SceneLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.SceneLayout.setContentsMargins(0, 0, 0, 0)
        self.SceneLayout.setObjectName("SceneLayout")
        self.gridLayout.addLayout(self.SceneLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.horizontal_splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1086, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuEdit = QtGui.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtGui.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidgetConsole = QtGui.QDockWidget(MainWindow)
        self.dockWidgetConsole.setEnabled(True)
        self.dockWidgetConsole.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.dockWidgetConsole.setObjectName("dockWidgetConsole")
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.console = QtGui.QTextEdit(self.dockWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.console.sizePolicy().hasHeightForWidth())
        self.console.setSizePolicy(sizePolicy)
        self.console.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.console.setStyleSheet("")
        self.console.setObjectName("console")
        self.gridLayout_2.addWidget(self.console, 0, 0, 1, 1)
        self.dockWidgetConsole.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidgetConsole)
        self.dockWidgetNodeBox = QtGui.QDockWidget(MainWindow)
        self.dockWidgetNodeBox.setFloating(False)
        self.dockWidgetNodeBox.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.dockWidgetNodeBox.setObjectName("dockWidgetNodeBox")
        self.dockWidgetContents_5 = QtGui.QWidget()
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")
        self.gridLayout_5 = QtGui.QGridLayout(self.dockWidgetContents_5)
        self.gridLayout_5.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.NodeBoxLayout = QtGui.QGridLayout()
        self.NodeBoxLayout.setObjectName("NodeBoxLayout")
        self.gridLayout_5.addLayout(self.NodeBoxLayout, 0, 0, 1, 1)
        self.dockWidgetNodeBox.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetNodeBox)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.dockWidgetNodeView = QtGui.QDockWidget(MainWindow)
        self.dockWidgetNodeView.setMinimumSize(QtCore.QSize(200, 100))
        self.dockWidgetNodeView.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidgetNodeView.setObjectName("dockWidgetNodeView")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_4 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_4.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.PropertiesformLayout = QtGui.QFormLayout()
        self.PropertiesformLayout.setContentsMargins(2, 2, 2, 2)
        self.PropertiesformLayout.setObjectName("PropertiesformLayout")
        self.gridLayout_4.addLayout(self.PropertiesformLayout, 0, 0, 1, 1)
        self.dockWidgetNodeView.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidgetNodeView)
        self.actionDelete = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/delete_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon1)
        self.actionDelete.setObjectName("actionDelete")
        self.actionOptions = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/colors_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOptions.setIcon(icon2)
        self.actionOptions.setObjectName("actionOptions")
        self.actionNode_box = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/node_box_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNode_box.setIcon(icon3)
        self.actionNode_box.setObjectName("actionNode_box")
        self.actionSave = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/save_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon4)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/folder_open_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoad.setIcon(icon5)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave_as = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/save_as_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as.setIcon(icon6)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionConsole = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/console_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConsole.setIcon(icon7)
        self.actionConsole.setObjectName("actionConsole")
        self.actionPlot_graph = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/plot_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlot_graph.setIcon(icon8)
        self.actionPlot_graph.setObjectName("actionPlot_graph")
        self.actionGroup_selected = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/comment_selected_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGroup_selected.setIcon(icon9)
        self.actionGroup_selected.setObjectName("actionGroup_selected")
        self.actionClear_scene = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/clear_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClear_scene.setIcon(icon10)
        self.actionClear_scene.setObjectName("actionClear_scene")
        self.actionShadows = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/shadow_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShadows.setIcon(icon11)
        self.actionShadows.setObjectName("actionShadows")
        self.actionMultithreaded = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/multithreaded_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMultithreaded.setIcon(icon12)
        self.actionMultithreaded.setObjectName("actionMultithreaded")
        self.actionDebug = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/debug_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDebug.setIcon(icon13)
        self.actionDebug.setObjectName("actionDebug")
        self.actionScreenshot = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/screenshot_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionScreenshot.setIcon(icon14)
        self.actionScreenshot.setObjectName("actionScreenshot")
        self.actionShortcuts = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/shortcuts_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShortcuts.setIcon(icon15)
        self.actionShortcuts.setObjectName("actionShortcuts")
        self.actionAlignLeft = QtGui.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/alignLeft.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAlignLeft.setIcon(icon16)
        self.actionAlignLeft.setObjectName("actionAlignLeft")
        self.actionAlignUp = QtGui.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/alignright.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAlignUp.setIcon(icon17)
        self.actionAlignUp.setObjectName("actionAlignUp")
        self.actionPropertyView = QtGui.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icons/property_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPropertyView.setIcon(icon18)
        self.actionPropertyView.setObjectName("actionPropertyView")
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addAction(self.actionOptions)
        self.menuEdit.addAction(self.actionClear_scene)
        self.menuEdit.addSeparator()
        self.menuView.addAction(self.actionNode_box)
        self.menuView.addAction(self.actionConsole)
        self.menuView.addAction(self.actionPlot_graph)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave_as)
        self.menuHelp.addAction(self.actionShortcuts)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionNode_box)
        self.toolBar.addAction(self.actionConsole)
        self.toolBar.addAction(self.actionPropertyView)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionShadows)
        self.toolBar.addAction(self.actionMultithreaded)
        self.toolBar.addAction(self.actionDebug)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPlot_graph)
        self.toolBar.addAction(self.actionGroup_selected)
        self.toolBar.addAction(self.actionScreenshot)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAlignLeft)
        self.toolBar.addAction(self.actionAlignUp)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "QtNodes", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidgetConsole.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Console", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidgetNodeBox.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Node Box", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidgetNodeView.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PropertyView", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOptions.setText(QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNode_box.setText(QtGui.QApplication.translate("MainWindow", "Node box", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setText(QtGui.QApplication.translate("MainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setText(QtGui.QApplication.translate("MainWindow", "Save as", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConsole.setText(QtGui.QApplication.translate("MainWindow", "Console", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPlot_graph.setText(QtGui.QApplication.translate("MainWindow", "Plot graph", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGroup_selected.setText(QtGui.QApplication.translate("MainWindow", "Group selected", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear_scene.setText(QtGui.QApplication.translate("MainWindow", "Clear scene", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShadows.setText(QtGui.QApplication.translate("MainWindow", "Shadows", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMultithreaded.setText(QtGui.QApplication.translate("MainWindow", "Multithreaded", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDebug.setText(QtGui.QApplication.translate("MainWindow", "Debug", None, QtGui.QApplication.UnicodeUTF8))
        self.actionScreenshot.setText(QtGui.QApplication.translate("MainWindow", "Screenshot", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShortcuts.setText(QtGui.QApplication.translate("MainWindow", "Shortcuts", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAlignLeft.setText(QtGui.QApplication.translate("MainWindow", "AlignLeft", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAlignLeft.setToolTip(QtGui.QApplication.translate("MainWindow", "Align selected nodes by the left most", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAlignUp.setText(QtGui.QApplication.translate("MainWindow", "AlignUp", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAlignUp.setToolTip(QtGui.QApplication.translate("MainWindow", "Align selected nodes by the up most", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPropertyView.setText(QtGui.QApplication.translate("MainWindow", "PropertyView", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPropertyView.setToolTip(QtGui.QApplication.translate("MainWindow", "toggle property view", None, QtGui.QApplication.UnicodeUTF8))
