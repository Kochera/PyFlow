from nine import str
from Qt import QtCore
from Qt import QtGui
from Qt.QtWidgets import QUndoView
from Qt.QtWidgets import QWidget
from Qt.QtWidgets import QVBoxLayout

from PyFlow.UI.Tool.Tool import DockTool
from PyFlow.UI.Views.VariablesWidget import VariablesWidget


class SecurityRatingTool(DockTool):
    """docstring for Variables tool."""
    def __init__(self):
        super(SecurityRatingTool, self).__init__()
        self.setMinimumSize(QtCore.QSize(200, 50))
        self.varsWidget = None
        self.content = QWidget()
        self.content.setObjectName("SecurityRatingToolContent")
        self.verticalLayout = QVBoxLayout(self.content)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.setWidget(self.content)

    @staticmethod
    def isSingleton():
        return True

    def onShow(self):
        super(SecurityRatingTool, self).onShow()
        #self.varsWidget = VariablesWidget(self.pyFlowInstance)
        #self.pyFlowInstance.fileBeenLoaded.connect(self.varsWidget.actualize)
        #self.verticalLayout.addWidget(self.varsWidget)
        #self.varsWidget.actualize()

    def showEvent(self, event):
        super(SecurityRatingTool, self).showEvent(event)
        if self.varsWidget is not None:
            self.varsWidget.actualize()

    @staticmethod
    def toolTip():
        return "Analyze Security Rating of Protocol"

    @staticmethod
    def name():
        return str("SecurityRating")