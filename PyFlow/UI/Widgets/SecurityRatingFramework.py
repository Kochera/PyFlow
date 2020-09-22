## Copyright 2015-2019 Ilgar Lunin, Pedro Cabrera

## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at

##     http://www.apache.org/licenses/LICENSE-2.0

## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.


from nine import str
from PyFlow.UI.Canvas.UICommon import clearLayout
from PyFlow.UI.Widgets.EditSecurityRatingWidget import EditSecurityRatingTreeWidget
from PyFlow.UI.Widgets.PropertiesFramework import CollapsibleWidget, HeadButton, CollapsibleFormWidget, CollapSibleGoupBox
from Qt import QtWidgets
from Qt import QtCore, QtGui




class SecurityRatingEntry(QtWidgets.QWidget):
    """docstring for PropertyEntry."""
    def __init__(self, label, widget, parent=None, hideLabel=False, maxLabelWidth=None, toolTip=""):
        super(SecurityRatingEntry, self).__init__(parent)
        self.label = label
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(1, 1, 1, 1)
        if not hideLabel:
            label = QtWidgets.QLabel(label + ":")
            label.setStyleSheet("font: bold")
            label.setToolTip(toolTip)
            if not maxLabelWidth:
                label.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred))
            else:
                label.setMaximumWidth(maxLabelWidth)
            self.layout.addWidget(label)
        self.layout.addWidget(widget)
        self.index = -1

    def getLabel(self):
        return self.label




class SecurityRatingWidget(QtWidgets.QWidget):
    """docstring for PropertiesWidget."""
    spawnDuplicate = QtCore.Signal()

    def __init__(self, parent=None, searchByHeaders=False):
        super(SecurityRatingWidget, self).__init__(parent)
        self.setWindowTitle("Security Rating view")
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.mainLayout.setObjectName("SecurityRatingMainLayout")
        self.mainLayout.setContentsMargins(2, 2, 2, 2)
        self.searchBox = QtWidgets.QLineEdit(self)
        self.searchBox.setObjectName("lineEdit")
        self.searchBox.setPlaceholderText(str("search..."))
        self.searchBox.textChanged.connect(self.filterByHeaders if searchByHeaders else self.filterByHeadersAndFields)
        self.searchBoxWidget = QtWidgets.QWidget()
        self.searchBoxLayout = QtWidgets.QHBoxLayout(self.searchBoxWidget)
        self.searchBoxLayout.setContentsMargins(1, 1, 1, 1)
        self.searchBoxLayout.addWidget(self.searchBox)

        # self.settingsButton = QtWidgets.QToolButton()
        # self.settingsButton.setIcon(QtGui.QIcon(":/settings.png"))
        # self.settingsMenu = QtWidgets.QMenu()
        # self.editPropertiesAction = QtWidgets.QAction("Edit Parameter Interface", None)
        # self.settingsMenu.addAction(self.editPropertiesAction)
        # self.settingsButton.setMenu(self.settingsMenu)
        # self.editPropertiesAction.triggered.connect(self.showPropertyEditor)
        #self.settingsButton.clicked.connect(self.spawnDuplicate.emit)
        # self.settingsButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)

        self.lockCheckBox = QtWidgets.QToolButton()
        self.lockCheckBox.setCheckable(True)
        self.lockCheckBox.setIcon(QtGui.QIcon(':/unlocked.png'))
        self.lockCheckBox.toggled.connect(self.changeLockIcon)
        self.searchBoxLayout.addWidget(self.lockCheckBox)
        self.tearOffCopy = QtWidgets.QToolButton()
        self.tearOffCopy.setIcon(QtGui.QIcon(":/tear_off_copy_bw.png"))
        self.tearOffCopy.clicked.connect(self.spawnDuplicate.emit)
        self.searchBoxLayout.addWidget(self.tearOffCopy)
        self.mainLayout.addWidget(self.searchBoxWidget)
        self.searchBoxWidget.hide()
        self.contentLayout = QtWidgets.QVBoxLayout()
        self.contentLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.mainLayout.addLayout(self.contentLayout)
        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addItem(self.spacerItem)
        self.mainLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))

    def changeLockIcon(self,checked):
        if checked:
            self.lockCheckBox.setIcon(QtGui.QIcon(':/locked.png'))
        else:
            self.lockCheckBox.setIcon(QtGui.QIcon(':/unlocked.png'))

    def setLockCheckBoxVisible(self, bVisible):
        self.lockCheckBox.setVisible(bVisible)

    def setTearOffCopyVisible(self, bVisible):
        self.tearOffCopy.setVisible(bVisible)


    def filterByHeaders(self, text):
        count = self.contentLayout.count()
        for i in range(count):
            item = self.contentLayout.itemAt(i)
            w = item.widget()
            if w:
                if text.lower() in w.title().lower():
                    w.show()
                else:
                    w.hide()

    def filterByHeadersAndFields(self, text):
        count = self.contentLayout.count()
        for i in range(count):
            item = self.contentLayout.itemAt(i)
            w = item.widget()
            if w:
                w.filterContent(text)
                if w.isAllWidgetsHidden():
                    w.hide()
                else:
                    w.show()
                    w.setCollapsed(False)

    def isLocked(self):
        return self.lockCheckBox.isChecked() == True

    def clear(self):
        if not self.isLocked():
            clearLayout(self.contentLayout)
            self.searchBoxWidget.hide()
            self.lockCheckBox.setChecked(False)

    def insertWidget(self, collapsibleWidget,index):
        if not self.isLocked():
            if isinstance(collapsibleWidget, CollapsibleFormWidget):
                self.contentLayout.insertWidget(index, collapsibleWidget)
                return True

    def addWidget(self, collapsibleWidget):
        if not self.isLocked():
            if isinstance(collapsibleWidget, CollapsibleFormWidget):
                self.contentLayout.insertWidget(-1, collapsibleWidget)
                return True

    def showPropertyEditor(self):
        tree = EditSecurityRatingTreeWidget()
        count = self.contentLayout.count()
        folders = {}
        for i in range(count):
            item = self.contentLayout.itemAt(i)
            w = item.widget()        
            if w:
                if w.title() in  ["Inputs"]:
                    for key,group in w.groups.items():
                        if key not in folders:
                            folders[key] = {}
                        #for e in range(group.groupLayout.count()):
                        #    w = group.groupLayout.itemAt(e).widget()
                        #    folders[key][w.getLabel()] = group.groupLayout.itemAt(e).widget()

        for fold in folders:
            folder = tree.addFolder(fold)
            #for widg in folders[fold]:
            #    child = tree.addNormal(widg,folder)

        d = QtWidgets.QDialog()
        d.setLayout(QtWidgets.QHBoxLayout())
        d.layout().addWidget(tree)
        d.exec_()
        newOrder = tree.model_to_dict()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    s = QtWidgets.QScrollArea()

    sw = SecurityRatingWidget()

    rootWidget = CollapsibleFormWidget(headName="Settings", noSpacer=True)
    rootWidget.addWidget("test", QtWidgets.QPushButton("ss"))
    rootWidget.addWidget("foo", QtWidgets.QPushButton(""))
    rootWidget.addWidget("bar", QtWidgets.QPushButton(""))

    rootWidget2 = CollapsibleFormWidget(headName="Test", noSpacer=True)
    rootWidget2.addWidget("test2", QtWidgets.QPushButton("aa"))

    sw.addWidget(rootWidget)
    sw.addWidget(rootWidget2)
    s.setWidget(sw)
    s.show()

    sw.clear()

    sys.exit(app.exec_())
